from mutagen.mp3 import MP3
from pathlib import Path
from shutil import copyfile
from pydub import AudioSegment
import time
import glob
import os

print(os.getcwd())

audiolist = glob.glob(os.getcwd() + "/audiofiles/*.mp3")

streaminit = open("./static/stream.m3u8", "w")

streaminit.write("""#EXTM3U
#EXT-X-VERSION:3
#EXT-X-TARGETDURATION:0
#EXT-X-MEDIA-SEQUENCE:0
#EXT-X-PLAYLIST-TYPE:EVENT
""")

streaminit.close()

segmentnumber = 0

while True:
    for i in audiolist:
        print("Now playing " + i + " for " + str(MP3(i).info.length))
        song = AudioSegment.from_mp3(i)
        lengthaudio = MP3(i).info.length
        if not os.path.exists('./static/chunks/' + str(segmentnumber)):
            os.mkdir('./static/chunks/' + str(segmentnumber))
        for i, chunk in enumerate(song[::10000]):
            with open(os.getcwd() + "/static/chunks/" + str(segmentnumber) + "/chunk-%s.mp3" % i, "wb") as f:
                chunk.export(f, format="mp3", bitrate="120k") #Change the Bitrate if you want
                print("Chunk Exported")
                m3ufile = open("./static/stream.m3u8", "a+")
                m3ufile.write("\n#EXTINF:4.00,\n./chunks/" + str(segmentnumber) + "/chunk-%s.mp3" % i)
                print("m3u appended")
                m3ufile.close()
                time.sleep(2) #Change this to whatever you want
        segmentnumber = segmentnumber + 1
