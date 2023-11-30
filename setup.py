import os
import platform as plf
#Check wheather running windows or not
def is_platform_windows():
    return plf.system() == "win"

#Dependencies
libs = ["pytube==15.0.0", "moviepy==1.0.3", "pathlib"]
for lib in libs:
    os.system("pip install {}".format(lib))

from pathlib import Path
innerTube = None

#Python Version
index = str(plf.python_version()).find(".")


#Platform ke according Path
if is_platform_windows() == "win":

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

os.system("rm temp.py")

if is_platform_windows() == "win":
    os.system("cls")
else:
    os.system("clear")

print("Setup Finished !!!")