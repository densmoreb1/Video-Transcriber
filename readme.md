# Overview

Program that can take a YouTube link and transcribe the video audio into text.

Must install dependencies. Would also recommend using a virtual enviroment so everything is in one place. Run the user.py to get started.

[Demo Video](http://youtube.link.goes.here)

# Development Environment

Must install the following
* pip3 install pydub
* pip3 install pytube
* pip3 install SpeechReconigtion
* 'brew install ffmpeg' or use your package manager to install ffmpeg

pydub and SpeechReconigtion work together to listen to audio segments

pytube works with YouTube to get all the information from a video

ffmpeg for converting mp4 or mp3 to wav file for the speech reconigtion to work 

# Useful Websites
https://realpython.com/python-speech-recognition/

# Future Work
