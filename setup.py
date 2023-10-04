#   Do not use this file if you dont understand what it does
#   Do not use this file if you dont understand what it does
#   Do not use this file if you dont understand what it does
#   Do not use this file if you dont understand what it does
#   Do not use this file if you dont understand what it does
#   Do not use this file if you dont understand what it does
#   Do not use this file if you dont understand what it does
#   Usage of this file without full knowledge is not recommended
#   Usage of this file without full knowledge is not recommended
#   Usage of this file without full knowledge is not recommended
#   Usage of this file without full knowledge is not recommended
#   Usage of this file without full knowledge is not recommended
#   Usage of this file without full knowledge is not recommended
#   Usage of this file without full knowledge is not recommended
import os
libs = ["pytube", "moviepy", "pathlib"]

for lib in libs:
    os.system("pip install {}".format(lib))
from pathlib import Path

# Get the user directory
user_directory = Path.home()

# Print the user directory
print(user_directory)

innerTube = str(user_directory)+"\AppData\Local\Programs\Python\Python311\Lib\site-packages\pytube\innertube.py"

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
