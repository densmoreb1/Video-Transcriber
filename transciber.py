from posixpath import abspath
from pydub.audio_segment import AudioSegment
from pydub.silence import split_on_silence
import speech_recognition as sr
import os
import shutil


class Transcriber:
    def __init__(self, file_name) -> None:
        """
        The init calls the other functions in the class.
        It takes in the file path and transcribes audio.
        It creates a directory for the class to work in which is audio-chunks which is replaced everytime the function is run.
        """
        self.file_name = file_name
        path = os.path.abspath(self.file_name)
        self.transcribe(path)
        self.writer()

    def transcribe(self, file_path):
        r = sr.Recognizer()
        # getting the sound from file
        sound = AudioSegment.from_wav(file_path)
        
        # splitting the sound into chunks for long videos
        chunks = split_on_silence(sound, min_silence_len=500, silence_thresh = sound.dBFS-14, keep_silence=500,)
        
        # make a folder to hold the audio
        folder = 'audio-chunks'
        if not os.path.isdir(folder):
            os.mkdir(folder)
        else:
            shutil.rmtree(folder)
            os.mkdir(folder)
        
        # looping through chunk and transcribing them
        self.whole_text = ""
        for i, audio_chunk in enumerate(chunks, start=1):
            chunk_filename = os.path.join(folder, f"chunk{i}.wav")
            audio_chunk.export(chunk_filename, format="wav")
            with sr.AudioFile(chunk_filename) as source:
                audio_listened = r.record(source)
                try:
                    text = r.recognize_google(audio_listened)
                except sr.UnknownValueError as e:
                    print("Error:", str(e))
                else:
                    text = f"{text.capitalize()}. \n"
                    # print(chunk_filename, ":", text)
                    self.whole_text += text
    # return the text for all chunks detected
        return self.whole_text

    def writer(self):
        file = open('transcription.txt', 'w')
        file.write(self.whole_text)
        file.close()

