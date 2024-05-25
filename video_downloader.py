# youtube_downloader.py

from pytube import YouTube

def get_youtube_url():
    url = input("Enter the YouTube video URL: ")
    return url

def download_video(url, output_path):
    try:
        # Create a YouTube object with the given URL
        yt = YouTube(url)
        
        # Get the highest resolution stream available
        stream = yt.streams.get_highest_resolution()
        
        # Download the video
        print(f"Downloading {yt.title}...")
        stream.download(output_path=output_path)
        print("Download completed!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    url = get_youtube_url()
    download_video(url, output_path = "//home//zulfiqar//Downloads//youtube_videoes" )


