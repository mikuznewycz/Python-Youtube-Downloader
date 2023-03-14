import os 
import youtube_downloader

urls = (
    # 'https://www.youtube.com/watch?v=9bZkp7q19f0',                  # PSY - GANGNAM STYLE
    # 'https://www.youtube.com/watch?v=Il0S8BoucSA',                  # Ed Sheeran - Shivers
    # 'https://www.youtube.com/watch?v=PWgvGjAhvIw',
    # 'https://www.youtube.com/watch?v=ZDrlmlzY7cE', 
    # 'https://www.youtube.com/watch?v=jYPu61aPHO8', 
    # 'https://www.youtube.com/watch?v=aQOanjlnkv0', 
    # 'https://www.youtube.com/watch?v=P1LXeJamrLk',
    # 'https://www.youtube.com/watch?v=R6rH4wb0pcQ',
    # 'https://www.youtube.com/watch?v=4NRXx6U8ABQ',
    # 'https://www.youtube.com/watch?v=Ek0SgwWmF9w',
    # "https://www.youtube.com/watch?v=PVzljDmoPVs",
    # "https://www.youtube.com/watch?v=W3q8Od5qJio",
    # "https://www.youtube.com/watch?v=JRfuAukYTKg",
    # "https://www.youtube.com/watch?v=y74UPiaK7u0",
    # "https://www.youtube.com/watch?v=3YxaaGgTQYM",
    # "https://www.youtube.com/watch?v=aU_TQcyGkvY", 
    # "https://www.youtube.com/watch?v=KQ6zr6kCPj8",
    # "https://www.youtube.com/watch?v=rrmsJhf89MY",
)

playlists = [
    # [url, outdir],
    ['https://www.youtube.com/watch?v=90RLzVUuXe4&list=PLDIoUOhQQPlU2DoseElwLlKXmV9YSEnKI', "videos\\NRJ HITS 2023"],
    ['https://www.youtube.com/watch?v=jYPu61aPHO8&list=PLDIoUOhQQPlU2DoseElwLlKXmV9YSEnKI', "videos\\NRJ HITS 2022"], # NRJ Hits 2022 - Musique 2022 Nouveauté
    # ['https://www.youtube.com/watch?v=apQ2ojJnpkc&list=PL4i3BECG7Wv9uxH5Gq49VCaq8xVXNZkjp', 'videos/Lazy Company S01'], 
    # ['https://www.youtube.com/watch?v=q5sRVrUKLS8&list=PLDZoSKnNh5sb2yf-FPNR8PSvwaqThbSi-', 'videos/Lazy Company S02'],
]




if __name__ == "__main__":
    # pass 

    for url in urls:
        fn = youtube_downloader.download_video_best_resolution(url)

    for playlist in playlists:
        fn = youtube_downloader.download_playlist(playlist[0], playlist[1])