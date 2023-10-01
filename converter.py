from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips
import os 

def convert(video, audio, title):
    video_clip = VideoFileClip(video)
    audio_clip = AudioFileClip(audio)

    final_clip = video_clip.set_audio(audio_clip)

    final_clip.write_videofile(title + ".mp4")
