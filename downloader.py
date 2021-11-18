from posixpath import splitext
from pytube import YouTube
import subprocess
import os
import shutil


class Downloader:
    def __init__(self) -> None:
        """
        The init function runs when the instance of the class in created.
        It will ask the user for a link to a YouTube video, download it, and convert it to the proper format.
        It will also create a directory for downloads, which is erased everytime it is run.
        """
        link = str(input('What is the video link? '))
        video = YouTube(link)
        folder = 'downloads'
        self.mp4_file = None
        if not os.path.isdir(folder):
            os.mkdir(folder)
        else:
            shutil.rmtree(folder)
            os.mkdir(folder)

        try:
            self.mp4_file = video.streams.get_audio_only('mp4').download(folder)
        except:
            print('Connection error')
        
        if self.mp4_file is not None:
            self.convert_to_wav()

    def convert_to_wav(self):
        subprocess.call(['ffmpeg', '-i', self.mp4_file, self.mp4_file + '.wav'])

    def get_file_name(self):
        return self.mp4_file + '.wav'

