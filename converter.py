import ffmpeg as ffm
import subprocess as sbp

def convert(video, audio, title):
    title+=".mp4"
    sbp.run(["ffmpeg", "-i", f"{video}", "-i", f"{audio}", "-c", "copy", f"{title}", "-hide_banner"])
