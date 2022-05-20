import os 
from pytube import YouTube, Playlist
from pytube.cli import on_progress #this module contains the built in progress bar
import ffmpeg
import uuid


def gen_temp_finename():
    return f'{uuid.uuid4()}.tmp'

def download_stream(stream):
    fn = gen_temp_finename()
    
    if os.path.exists(fn):
        os.remove(fn)

    print(f'Downloading "{stream.default_filename}" with "{stream}"')
    stream.download('_tmp', filename=fn)
    print("") # pour forcer la ligne de commande à faire une nouvelle ligne 

    return os.path.join('_tmp', fn)


def download_video_best_resolution(url, outdir = 'videos'):

    if not os.path.exists(outdir):
        os.mkdir(outdir)

    yt = YouTube(url, on_progress_callback=on_progress)

    video_stream = yt.streams.filter(progressive=False, type='video', mime_type='video/mp4').order_by('resolution').desc().first()
    audio_stream = yt.streams.filter(only_audio=True, type='audio', mime_type='audio/mp4').order_by('abr').desc().first()
    
    outfile = os.path.join(outdir, video_stream.default_filename)
    full_outfile = os.path.abspath(outfile)

    if not os.path.exists(outfile):

        video_file = download_stream(video_stream)
        audio_file = download_stream(audio_stream)
        
        print(f'Creating File "{video_stream.default_filename}" with FFMEPG')

        video = ffmpeg.input(video_file)
        audio = ffmpeg.input(audio_file)

        ffmpeg.output(audio, video, outfile, vcodec='copy', acodec='copy', loglevel='quiet').run(overwrite_output=True)

        os.remove(video_file)
        os.remove(audio_file)

        print(f'File created : "{full_outfile}"')
    
    return full_outfile

    
def download_playlist(url, outdir):

    p = Playlist(url)

    print(f'>> Downloading playlist "{p.title}" {len(p.video_urls)}')
    for i, video in enumerate(p.video_urls):
        print(f" File {i} / {len(p.video_urls)}")
        download_video_best_resolution(video, outdir=outdir)
    print(f"<< Downloading playlist")

if __name__ == "__main__":
    pass
    # download_video_progressive_best_resolution('https://www.youtube.com/watch?v=Il0S8BoucSA', 'videos')
    # download_video_best_resolution('https://www.youtube.com/watch?v=Il0S8BoucSA', 'videos')
    # download_playlist('https://www.youtube.com/watch?v=jYPu61aPHO8&list=PLDIoUOhQQPlU2DoseElwLlKXmV9YSEnKI', 'videos/NRJ HITS 2022')
    # download_playlist('https://www.youtube.com/watch?v=apQ2ojJnpkc&list=PL4i3BECG7Wv9uxH5Gq49VCaq8xVXNZkjp', 'videos/tests')