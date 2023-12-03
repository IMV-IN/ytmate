import ffmpeg as ffm
import subprocess as sbp

def convert(video, audio, title):
    input_video = ffm.input(video)
    input_audio = ffm.input(audio)
    ffm.concat(input_video, input_audio, v=1, a=1).output(title+".mp4").run()