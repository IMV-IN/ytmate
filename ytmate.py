import os
import pytube as py
from pytube import YouTube
import converter as con

os.system("clear")

while(True):
    
    #menu
    print("1. Quick download(Most friendly, however may or may not work)")
    print("2. Single Video with link: ")
    print("3. Full Playlist with link of playlist: ")
    print("4. Combine video and audio")
    print("5. Test ")
    print("6. Exit")

    choice = int(input("Choice: "))

    #Single Video
    if choice == 2:

        video = str(input("Clean link: "))

        yt = py.YouTube(url=video)
        print(yt.title)

        #List all formats
        os.system("pytube {} --list".format(video))
        InputItag = int(input("Enter the itag: "))

        #Download video
        os.system("pytube {} --itag={}".format(video, InputItag))
    
    #Playlist Download
    elif choice == 3:

        #Get the playlist link
        playlist=py.Playlist(input("Enter Clean link: "))

        #Create a folder to put all the videos
        print("")
        os.system("mkdir \"{}\"".format(playlist.title))

        #Get the links to all the videos in the playlist
        playlist_videos = []
        for url in playlist.video_urls:
            playlist_videos.append(url)

        #same Itage function: sameItag[0] = flag, and sameItag[1] = value of Itag 
        sameItag = [-1,1]

        #No of videos to create indexing when downloading via playlist
        no_of_videos = playlist.length
        index=0

        for video in playlist_videos:

            #Indexing at the top of every video
            index=index+1
            print("\n{} of {}".format(index, no_of_videos))

            #Print the title
            yt = py.YouTube(url=video)
            print(yt.title)

            #Checking the sameItag flag
            if sameItag[0] == 1:

                InputItag = sameItag[1]
            elif sameItag[0] == 0:
                
                os.system("pytube {} --list".format(video))
                InputItag = int(input("Enter the itag(Enter -1 to skip this video): "))

            #used for first time set-up
            if sameItag[0] == -1:
                sameItag[0] = int(input("Do you want to keep this setting for all the videos(1-Yes/0-No)"))

                if sameItag[0] == 1:
                
                    os.system("pytube {} --list".format(video))
                    sameItag[1] = InputItag = int(input("Enter the itag: "))
                elif sameItag[0] == 0:
                
                    os.system("pytube {} --list".format(video))
                    InputItag = int(input("Enter the itag(Enter -1 to skip this video): "))

            #Option to skip a video normally without raising an error
            if InputItag == -1:

                os.system("clear")
                print("skipping {} ....".format(yt.title))
                continue
            
            #Downloading the video
            os.system("pytube {} --itag={} --target \"{}\"".format(video, InputItag, playlist.title))
            os.system("pytube {} --itag={} --target \"{}\" -a ".format(video, InputItag, playlist.title))

            #Alert:- You have used a OS specific symbol to fix this# You are forcing mp4 for audio and webm for video
            #Alert:- You have used a OS specific symbol to fix this# You are forcing mp4 for audio and webm for video
            #Alert:- You have used a OS specific symbol to fix this# You are forcing mp4 for audio and webm for video
            con.convert(playlist.title+"//"+yt.title+".webm", playlist.title+"//"+yt.title+".mp4", playlist.title+"/"+yt.title)
            #Alert:- You have used a OS specific symbol to fix this# You are forcing mp4 for audio and webm for video
            #Alert:- You have used a OS specific symbol to fix this# You are forcing mp4 for audio and webm for video
            #Alert:- You have used a OS specific symbol to fix this# You are forcing mp4 for audio and webm for video
    elif choice == 4:

        #Get the video and audio files and the title of the output file
        video = str(input("Enter the video file name with extension: "))
        audio = str(input("Enter the audio file name with extension: "))
        title = str(input("Enter the name of the output file without extension: "))
        
        #Convert
        con.convert(video, audio, title)
    
    #Quick testing to check if the restricted videos are also downloading
    elif choice == 5:
        print("Testing with restricted mode ON")
        testLinkRestrictOn = "https://youtu.be/O-Ht8U9Q-5U?si=fS0IwB1M9a3ZOpTo"
        yt = YouTube(testLinkRestrictOn)
        if (yt.streams.filter(progressive=True, file_extension="mp4").order_by('resolution').desc().first().download()):
            os.system("clear")
            print("All Setup")
        else:
            os.system("clear")
            print("Please refer to README.md for setting up the script")

    #New feature of Quick download
    elif choice == 1:
        link = str(input("Enter Clean Link: "))
        yt = YouTube(link)
        yt.streams.filter(progressive=True, file_extension="mp4").desc().first().download()
    
    elif choice == 6:

        os.system("clear")
        print("Thank you!!")
        break
    
    else:

        os.system("clear")
        print("Invalid output!! Try again")
