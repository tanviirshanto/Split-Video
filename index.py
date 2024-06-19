#"Q:\Web\VIDEO\input.mp4"
import cmd
import subprocess,os
VideoPath=input("\n\n\tEnter Your Video Path:\t")
folder=os.path.basename(VideoPath)
folder=folder.replace('.mp4','')
VideoPath=VideoPath.replace('"','')

with open("cuts.txt") as f:
    for line in f.readlines():
        filename, start, end = line.strip().split(' ')
        cmd=["ffmpeg", "-i", VideoPath, "-ss", start, "-to", end, "-c", "copy", f"{folder}\{filename}"  ]
        subprocess.run(cmd, stderr=subprocess.STDOUT)