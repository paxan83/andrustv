
import re
import requests

PAGE_URL = "https://tvrus.eu"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

try:
    response = requests.get(PAGE_URL, headers=headers, timeout=10)
    match = re.search(r'https://[^\s"\']+\.m3u8', response.text)
    if match:
        stream_url = match.group(0)
        # ВАЖНО: Каждая команда пишется строго с новой строки с правильными заголовками
        m3u_content = f"#EXTM3U\n#EXTINF:-1 tvg-id=\"TVRUS.de\" tvg-name=\"TVRUS\" group-title=\"International\", TVRUS\n{stream_url}\n"
        
        with open("playlist.m3u", "w", encoding="utf-8") as f:
            f.write(m3u_content)
        print("Плейлист playlist.m3u успешно обновлен!")
    else:
        print("Ссылка на поток не найдена.")
except Exception as e:
    print(f"Ошибка: {e}")

