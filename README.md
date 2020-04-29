# WebradioTest
A live http radio/webradio test, all in python

# You will need
* Python 3, not 2
* FFMPEG
* Pydub, mutagen and Flask
* MP3 files

# Tutorial
First, download the repository onto your computer

Make a "audiofiles" folder and put your mp3 files in there (you can name it 1.mp3, 2.mp3, etc.. to make it play in order)

Make a "chunks" folder in the static folder

Run testradioweb.py (for the HTTP server) and testradio.py (for the radio itself)

Your radio should now be live at /static/radio.m3u8

(For now it only works with ffplay with the command "ffplay -reconnect 1 -http_multiple 1 http://localhost:8081/static/stream.m3u8")

# Optional things to do
* Edit the program to play in random order or add a jingle between musics
