import ffmpeg as ffm
import subprocess as sbp

def convert(video, audio, title):
    input_video = ffm.input(video)
    input_audio = ffm.input(audio)
    output_file = f"{title}.mp4"

    try:
        ffm.output(input_video, input_audio, output_file, vcodec='copy', acodec='copy').run()
    except ffm.Error as e:
        print(f"Error occurred during conversion: {e}")
        return -1
    return 0