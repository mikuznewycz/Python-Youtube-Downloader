import os 
import youtube_downloader

urls = (
    'https://www.youtube.com/watch?v=9bZkp7q19f0',                  # PSY - GANGNAM STYLE
    'https://www.youtube.com/watch?v=Il0S8BoucSA',                    # Ed Sheeran - Shivers
)

playlists = [
    # [url, outdir],
    # ['https://www.youtube.com/watch?v=jYPu61aPHO8&list=PLDIoUOhQQPlU2DoseElwLlKXmV9YSEnKI', "videos\\NRJ HITS 2022"], # NRJ Hits 2022 - Musique 2022 Nouveauté
]




if __name__ == "__main__":
    # pass 

    for url in urls:
        fn = youtube_downloader.download_video_best_resolution(url)

    for playlist in playlists:
        fn = youtube_downloader.download_playlist(playlist[0], playlist[1])