import re
import requests

PAGE_URL = "https://tvrus.eu"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://tvrus.eu"
}

try:
    response = requests.get(PAGE_URL, headers=headers, timeout=15)
    html_content = response.text

    # Новый, более надежный поиск ссылки на поток m3u8
    match = re.search(r'(https?://[^\s"\']+?\.m3u8[^\s"\']*)', html_content)
    
    if not match:
        # Резервный поиск, если ссылка экранирована косыми чертами (например, https:\/\/...)
        match = re.search(r'(https?:\\/\\/[^\s"\']+?\.m3u8[^\s"\']*)', html_content)

    if match:
        stream_url = match.group(0).replace(r'\/', '/') # Очищаем от экранирования, если оно было
        print(f"Успех! Найдена актуальная ссылка: {stream_url}")

        # Формируем правильный M3U файл
        m3u_content = f"#EXTM3U\n#EXTINF:-1 tvg-id=\"TVRUS.de\" tvg-name=\"TVRUS\" group-title=\"International\", TVRUS\n{stream_url}\n"
        
        with open("playlist.m3u", "w", encoding="utf-8") as f:
            f.write(m3u_content)
        print("Файл iprustv.m3u успешно обновлен и сохранен!")
    else:
        print("Ошибка: Код плеера изменился, ссылка на m3u8 не найдена.")
        
except Exception as e:
    print(f"Произошла ошибка при запросе к сайту: {e}")
