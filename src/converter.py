import ffmpeg as ffm
import subprocess as sbp

def convert(video, audio, title):
    input_video = ffm.input(video)
    input_audio = ffm.input(audio)

    try:
        convert = sbp.run(["ffmpeg" ,"-i" ,f"{video}" ,"-i" ,f"{audio}" ,"-c" ,"copy" ,f"{title}" ,"-hide_banner"])
        if convert != 0:
            raise RuntimeError
    except:
        ffm.concat(input_video, input_audio, v=1, a=1).output(title+".mp4").run()
        if convert != 0:
            return -1