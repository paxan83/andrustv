import re
import requests

# Пробуем несколько альтернативных путей получения ссылки на поток
PAGE_URL = "https://tvrus.eu"
BACKUP_URL = "https://iptv-org.github.io/channels/de/TVRUS"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "Referer": "https://google.com"
}

def save_m3u(stream_url):
    m3u_content = f"#EXTM3U\n#EXTINF:-1 tvg-id=\"TVRUS.de\" tvg-name=\"TVRUS\" group-title=\"International\", TVRUS\n{stream_url}\n"
    with open("iprustv.m3u", "w", encoding="utf-8") as f:
        f.write(m3u_content)
    print("Файл iprustv.m3u успешно обновлен!")

try:
    # Попытка 1: Основной сайт с полной симуляцией браузера через сессию
    session = requests.Session()
    response = session.get(PAGE_URL, headers=headers, timeout=15)
    html_content = response.text

    match = re.search(r'(https?://[^\s"\']+?\.m3u8[^\s"\']*)', html_content)
    if not match:
        match = re.search(r'(https?:\\/\\/[^\s"\']+?\.m3u8[^\s"\']*)', html_content)

    if match:
        stream_url = match.group(0).replace(r'\/', '/')
        save_m3u(stream_url)
        exit(0)
        
    print("Основной сайт не отдал ссылку, пробуем резервный метод...")
    
    # Попытка 2: Если сайт заблокировал, берем стабильный поток с базы iptv-org
    # (Она парсит их официальное приложение BEMTV)
    stream_url = "http://315e5a5d.ottrast.com/iptv/8KSD5KFDXA6H88/14022/index.m3u8"
    save_m3u(stream_url)

except Exception as e:
    # Попытка 3: Экстренный случай — жестко прописываем рабочий альтернативный поток
    print(f"Ошибка запроса: {e}. Применяем экстренный поток.")
    save_m3u("http://315e5a5d.ottrast.com/iptv/8KSD5KFDXA6H88/14022/index.m3u8")

