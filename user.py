from downloader import Downloader
from transciber import Transcriber

# downloands the file and converts it to the right format
downloader = Downloader()
file_name = downloader.get_file_name()

if file_name is not None:
    # takes in the file name and transcribes into the transcription file
    transcriber = Transcriber(file_name)
