import os 
import youtube_downloader

urls = (
    'https://www.youtube.com/watch?v=9bZkp7q19f0',                  # PSY - GANGNAM STYLE
    # 'https://www.youtube.com/watch?v=Il0S8BoucSA',                  # Ed Sheeran - Shivers
    # 'https://www.youtube.com/watch?v=ZDrlmlzY7cE',                  # Purple Disco Machine Sophie and the Giants - In The Dark
    # 'https://www.youtube.com/watch?v=MmQa-lLy38o',                  # Yams Clic Clic pan pan pan
    # 'https://www.youtube.com/watch?v=GrLladCx8zA',                  # NOOB SAISON 1 4K
)

playlists = [
    # [url, outdir],
    # ['https://www.youtube.com/watch?v=jYPu61aPHO8&list=PLDIoUOhQQPlU2DoseElwLlKXmV9YSEnKI', "videos\\NRJ HITS 2022"], # NRJ Hits 2022 - Musique 2022 Nouveauté
    # ['https://www.youtube.com/watch?v=apQ2ojJnpkc&list=PL4i3BECG7Wv9uxH5Gq49VCaq8xVXNZkjp', 'videos/Lazy Company S01'], 
    # ['https://www.youtube.com/watch?v=q5sRVrUKLS8&list=PLDZoSKnNh5sb2yf-FPNR8PSvwaqThbSi-', 'videos/Lazy Company S02'],
]




if __name__ == "__main__":
    # pass 

    for url in urls:
        fn = youtube_downloader.download_video_best_resolution(url)

    for playlist in playlists:
        fn = youtube_downloader.download_playlist(playlist[0], playlist[1])