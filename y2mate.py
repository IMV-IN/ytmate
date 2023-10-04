import os
import pytube as py
import converter as con

while(True):
    
    os.system("cls")
    print("1. Single Video with link: ")
    print("2. Full Playlist with link of playlist: ")
    print("3. Combine video and audio")
    print("4. Exit ")

    choice = int(input("Choice: "))

    if choice == 1:

        link = str(input("Clean link: "))

        yt = py.YouTube(url=link)
        print(yt.title)

        os.system("pytube {} --list".format(link))
        InputItag = int(input("Enter the itag: "))

        os.system("pytube {} --itag={}".format(link, InputItag))
    
    elif choice == 2 :

        playlist_videos=[]

        playlist=py.Playlist(input("Enter Clean link: "))
        print("")
        
        #Create a folder to put all the videos
        os.system("mkdir {}".format(playlist.title))

        for url in playlist.video_urls:
            playlist_videos.append(url)

        #same Itage function: sameItag[0] flag, and sameItag[1] = value of Itag 
        sameItag = [-1,1]

        #-------------------------------------------------------------
        #No of videos to create indexing when downloading via playlist
        no_of_videos = playlist.length
        index=0
        #-------------------------------------------------------------

        for video in playlist_videos:
            #Indexing at the top of every video
            index=index+1
            print("")
            print("{} of {}".format(index, no_of_videos))

            #Print the title
            yt = py.YouTube(url=video)
            print(yt.title)

            #Checking the sameItag flag
            if sameItag[0] == 1:
                InputItag = sameItag[1]
            elif sameItag[0] == 0:
                os.system("pytube {} --list".format(video))
                InputItag = int(input("Enter the itag(Enter -1 to skip this video): "))
            #use for first time set-up
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
                os.system("cls")
                print("skipping {}".format(yt.title))
                continue
            
            #Downloading the video
            os.system("cd {} && pytube {} --itag={}".format(playlist.title, video, InputItag))
    
    elif choice == 3:
        video = str(input("Enter the video file name with extension: "))
        audio = str(input("Enter the audio file name with extension: "))
        title = str(input("Enter the name of the output file without extension: "))
        con.convert(video, audio, title)

    elif choice == 4:
        os.system("cls")
        print("Thank you!!")
        break
    
    else:

        print("Invalid output!! Try again")
