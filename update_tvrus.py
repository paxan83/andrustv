try:
    # Рабочий альтернативный поток телеканала TVRUS
    stream_url = "http://315e5a5d.ottrast.com/iptv/8KSD5KFDXA6H88/14022/index.m3u8"
    
    # Формируем структуру плейлиста M3U
    m3u_content = f"#EXTM3U\n#EXTINF:-1 tvg-id=\"TVRUS.de\" tvg-name=\"TVRUS\" group-title=\"International\", TVRUS\n{stream_url}\n"
    
    # Записываем в ваш основной файл плейлиста
    with open("iprustv.m3u", "w", encoding="utf-8") as f:
        f.write(m3u_content)
        
    print("Успех! Файл iprustv.m3u успешно перезаписан.")

except Exception as e:
    print(f"Ошибка при записи файла: {e}")



