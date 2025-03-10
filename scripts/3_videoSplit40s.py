import os
from moviepy.editor import VideoFileClip


def split_video(input_video, output_folder="clips2", clip_length=40):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    video = VideoFileClip(input_video)
    duration = int(video.duration)

    for start_time in range(0, duration, clip_length):
        end_time = min(start_time + clip_length, duration)
        clip = video.subclip(start_time, end_time)
        output_path = f"{output_folder}/clip_{start_time}.mp4"
        clip.write_videofile(output_path, codec="libx264", fps=30)

    print("Video splitting completed.")


# Example Usage
split_video("video3.mp4")
