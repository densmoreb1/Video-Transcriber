from posixpath import splitext
from pytube import YouTube
import subprocess
import os
import shutil


class Downloader:
    def __init__(self) -> None:
        link = str(input('What is the video link? '))
        video = YouTube(link)
        folder = 'downloads'
        if not os.path.isdir(folder):
            os.mkdir(folder)
        else:
            shutil.rmtree(folder)
            os.mkdir(folder)

        try:
            self.mp4_file = video.streams.get_audio_only('mp4').download(folder)
        except:
            print('Connection error')
        
        self.convert_to_wav()

    def convert_to_wav(self):
    # convert to wav file
        subprocess.call(['ffmpeg', '-i', self.mp4_file, self.mp4_file + '.wav'])

    def get_file_name(self):
        return self.mp4_file + '.wav'

