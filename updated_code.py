from pytube import YouTube
from tqdm import tqdm # for adding progress bar

def get_url():
    url = input("Enter the YouTube video URL: ")
    return url

def progress_function(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    tqdm.write(f"Downloaded: {percentage_of_completion:.2f}%")

def download_video(url, path):
    try:
        # Create a YouTube object with the given URL
        yt = YouTube(url, on_progress_callback=progress_function)
        
        # Get the highest resolution stream available
        stream = yt.streams.get_highest_resolution()
        
        # Create a tqdm progress bar
        with tqdm(total=stream.filesize, unit='B', unit_scale=True, desc=yt.title) as pbar:
            def tqdm_progress_function(stream, chunk, bytes_remaining):
                total_size = stream.filesize
                bytes_downloaded = total_size - bytes_remaining
                pbar.update(len(chunk))
            
            yt.register_on_progress_callback(tqdm_progress_function)
            
            # Download the video
            print(f"Downloading video: {yt.title}...")
            stream.download(path)
            print("Download completed!")
    except Exception as e:
        print(f"Error downloading video: {e}")

if __name__ == "__main__":
    url = get_url()
    download_video(url, path="//home//zulfiqar//Downloads//youtube_videos")
