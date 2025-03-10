from PIL import Image  # Properly import Image before patching

# Patch: Fix for newer Pillow versions where Image.ANTIALIAS was removed
if not hasattr(Image, 'ANTIALIAS'):
    Image.ANTIALIAS = Image.LANCZOS  # Use LANCZOS as the replacement

import os
from moviepy.editor import VideoFileClip, clips_array

# Paths to top and bottom video folders
top_clips_folder = "C:/Users/ilias-k/PycharmProjects/ShortClipAutomation/.venv/Scripts/clips"
bottom_clips_folder = "C:/Users/ilias-k/PycharmProjects/ShortClipAutomation/.venv/Scripts/clips2"
output_folder = "C:/Users/ilias-k/PycharmProjects/ShortClipAutomation/.venv/Scripts/merged_clips"

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Get sorted list of top and bottom video files
top_videos = sorted([f for f in os.listdir(top_clips_folder) if f.endswith(".mp4")])
bottom_videos = sorted([f for f in os.listdir(bottom_clips_folder) if f.endswith(".mp4")])

# If there are more top videos than bottom videos, reuse the bottom videos in a loop
bottom_video_count = len(bottom_videos)

for i, top_video in enumerate(top_videos):
    top_video_path = os.path.join(top_clips_folder, top_video)

    # Select bottom video in a looped manner
    bottom_video = bottom_videos[i % bottom_video_count]
    bottom_video_path = os.path.join(bottom_clips_folder, bottom_video)

    output_video_path = os.path.join(output_folder, f"merged_{top_video}")

    print(f"Merging: {top_video} + {bottom_video} → {output_video_path}")

    # Load and resize clips
    top_clip = VideoFileClip(top_video_path).resize(height=960)
    bottom_clip = VideoFileClip(bottom_video_path).resize(height=960).without_audio()  # 🔹 ALWAYS REMOVE AUDIO

    # Ensure bottom video is long enough (Loop if it's shorter)
    if bottom_clip.duration < top_clip.duration:
        loop_count = int(top_clip.duration // bottom_clip.duration) + 1
        bottom_clip = bottom_clip.loop(n=loop_count).subclip(0, top_clip.duration)

    # Stack top and bottom videos
    final_clip = clips_array([[top_clip], [bottom_clip]])

    # Write final merged video file
    final_clip.write_videofile(output_video_path, codec="libx264", fps=30)

print("✅ Merging process completed successfully!")
