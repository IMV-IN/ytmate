import subprocess as sbp
import platform as plf
#Check wheather running windows or not
def is_platform_windows():
    return plf.system() == "Windows"

#Dependencies
libs = ["pytube==15.0.0", "ffmpeg-python", "pathlib"]
for lib in libs:
    sbp.run(["pip", "install", "{}".format(lib)])

if is_platform_windows():
    sbp.run(["winget", "install", "ffmpeg"])
else:
    #Not very comfortable with having used sudo
    sbp.run(["sudo", "apt", "update", "/n"])
    sbp.run(["sudo", "apt", "install", "ffmpeg"])


from pathlib import Path
innerTube = None

#Python Version
index = str(plf.python_version()).find(".")

#Platform ke according Path
if is_platform_windows():

    # Get the user directory
    user_directory = Path.home()
    pyVersion = str(plf.python_version())[:index]+str(plf.python_version())[index+1:index+3]
    innerTube = str(user_directory)+"\AppData\Local\Programs\Python\Python{}\Lib\site-packages\pytube\innertube.py".format(pyVersion)
else:
    
    pyVersion = str(plf.python_version())[:index+3]
    innerTube = "/usr/local/python/{}/lib/python{}/site-packages/pytube/innertube.py".format(plf.python_version(),pyVersion)

file = open(innerTube, "r")
lines = file.readlines()
file_new = open("temp.py","w")
index=0
for line in lines:
    index=index+1
    if index == 223:
        file_new.write("    def __init__(self, client='ANDROID', use_oauth=False, allow_cache=True):\n")
        continue
    file_new.write(line)

file.close()
file_new.close()

fileOut = open(innerTube, "w")
fileIn = open("temp.py","r")

lines = fileIn.readlines()
for line in lines:
    fileOut.write(line)

fileIn.close()
fileOut.close()

sbp.run(["rm", "temp.py"])

if is_platform_windows():
    sbp.run("cls")
else:
    sbp.run("clear")
print("Setup Finished !!!")
