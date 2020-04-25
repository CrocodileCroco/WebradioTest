from mutagen.mp3 import MP3
from pathlib import Path
from shutil import copyfile
from pydub import AudioSegment
import time
import glob
import os

print(os.getcwd())

audiolist = glob.glob(os.getcwd() + "/audiofiles/*.mp3")

while True:
    for i in audiolist:
        print("Now playing " + i + " for " + str(MP3(i).info.length))
        song = AudioSegment.from_mp3(i)
        #try:
        #    copyfile(i, os.getcwd() + "/static/radio.mp3")
        #except:
        #    Path(os.getcwd() + '/static/radio.mp3').touch()
        #    copyfile(i, os.getcwd() + "/static/radio.mp3")
        lengthaudio = MP3(i).info.length
        for i, chunk in enumerate(song[::20000]):
            with open(os.getcwd() + "/static/radio.mp3", "wb") as f:
                chunk.export(f, format="mp3")
                print("exported chunk")
                time.sleep(20)