from pytube import YouTube
from pytube.exceptions import RegexMatchError, VideoUnavailable
from tqdm import tqdm
import re

def get_url():
    url = input("Enter the YouTube video URL: ")
    return url

def validate_url(url):
    # Simple regex to validate YouTube URL
    youtube_regex = (
        r'(https?://)?(www\.)?'
        '(youtube|youtu|youtube-nocookie)\.(com|be)/'
        '(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')
    youtube_regex_match = re.match(youtube_regex, url)
    
    if youtube_regex_match:
        return True
    else:
        return False

def progress_function(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    tqdm.write(f"Downloaded: {percentage_of_completion:.2f}%")

def download_video(url, path):
    try:
        if not validate_url(url):
            raise ValueError("Invalid YouTube URL. Please enter a valid URL.")
        
        # Create a YouTube object with the given URL
        yt = YouTube(url)
        
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
            stream.download(output_path=path)
            print("Download completed!")
    except RegexMatchError:
        print("Error: The URL does not match the YouTube format. Please check the URL and try again.")
    except VideoUnavailable:
        print("Error: The video is unavailable. It may have been removed or set to private.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    url = get_url()
    download_video(url, path="//home//zulfiqar//Downloads//youtube_videos")
