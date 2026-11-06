import re
import requests

# URL официального плеера, откуда транслируется поток
IFRAME_URL = "https://t62a.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://tvrus.eu"
}

try:
    # Делаем запрос к плееру
    response = requests.get(IFRAME_URL, headers=headers, timeout=15)
    html = response.text

    # Ищем актуальную ссылку на поток с действующим токеном
    match = re.search(r'(https?://[^\s"\']+?\.m3u8[^\s"\']*)', html)
    
    if match:
        stream_url = match.group(0).replace(r'\/', '/')
        print(f"Поток успешно найден: {stream_url}")

        # Формируем структуру M3U
        m3u_content = f"#EXTM3U\n#EXTINF:-1 tvg-id=\"TVRUS.de\" tvg-name=\"TVRUS\" group-title=\"International\", TVRUS\n{stream_url}\n"
        
        # Перезаписываем ваш плейлист iprustv.m3u
        with open("iprustv.m3u", "w", encoding="utf-8") as f:
            f.write(m3u_content)
        print("Файл iprustv.m3u успешно обновлен!")
    else:
        print("Ошибка: Не удалось найти актуальный токен в коде плеера.")

except Exception as e:
    print(f"Ошибка скрипта: {e}")




