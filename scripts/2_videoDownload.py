import yt_dlp


def download_youtube_video(url, output_path="video3.mp4"):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': output_path,
        'merge_output_format': 'mp4'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    return output_path


# Example Usage
youtube_url = "https://www.youtube.com/watch?v=eX66JFc4pqk"
download_youtube_video(youtube_url)
