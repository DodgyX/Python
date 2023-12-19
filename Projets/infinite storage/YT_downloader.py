from pytube import YouTube

def download_youtube_video(url, output_path='downloads'):
    try:
        # Create a YouTube object
        yt = YouTube(url)

        # Get the highest resolution stream available
        video_stream = yt.streams.get_highest_resolution()

        # Specify the output path (default is 'downloads' folder)
        video_stream.download(r'C:\Users\yoann.wiss\Desktop\python\Projets\infinite storage\Tests')

        print(f"Video downloaded successfully to {r'C:\Users\yoann.wiss\Desktop\python\Projets\infinite storage\Tests'}")
    except Exception as e:
        print(f"Error downloading video: {e}")

# Example usage:
video_url = "https://www.youtube.com/watch?v=Zdl9AN7viHU"
download_youtube_video(video_url)