from pytube import YouTube
import os
from moviepy.editor import *

def main():
    link = input("Link:\n>>")
    yt = YouTube(link)
    video = yt.streams.filter(only_audio = True).first()
    name = input("Enter file name (without .mp3): ")
    video.download(output_path='ytVidStorage', filename=name)
    video = AudioFileClip(os.path.join("ytVidStorage/" + name + ".mp4"))
    video.write_audiofile(os.path.join("ytVidStorage/" + name + ".mp3"))
    print("Done")

while True:
    main()