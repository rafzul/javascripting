import subprocess
import sys, os


"""
            #####################################
            ##### YOUTUBE TO MP3 SPLITTER  ######
            #####################################
ABOUT:
Have you ever found a good music compilation on youtube and wanted to download a playlist but you
didn't have time to mess around with splitting music into separate songs and do the boring ID3 editing in Audacity?
This script might help you. You just need a youtube link and a tracklist of the songs with their timestamps
(usually already in description or in top comments). Read the comments below for detailed instructions!
PYTHON REQUIREMENTS:
Python 3, pydub and youtube_dl
The script wil try to autoinstall missing dependecies, so if using in virtualenv, remove autoinstalling part or make sure
you already have pydub and youtube_dl installed!
USAGE:
The script itself is already a working example for downloading and splitting a Proleter video, so just modify it
according to your favourite Youtube music compilation. Just edit a SAVE_FOLDER to match your PC and create a textfile called
Proleter.txt next to this script with the following content (found under the Youtube video)
Proleter.txt
0:00:00 - My Melancholy Baby
0:03:58 - Can't Stop Me
0:07:42 - Fat Morris
0:11:32 - Sometimes
0:13:07 - Red Soap
0:16:23 - April Showers
0:20:52 - By The Rivers
0:24:33 - It Don't Mean A Thing
0:28:12 - Queen of Hearts
0:32:09 - U Can Get It
0:36:30 - Not Afraid
0:39:47 - Throw It Back (Instrumental)
0:42:48 - Downtown Irony
0:47:21 - Faidherbe Square
0:50:50 - Muhammad Ali
DISCLAIMER:
This is just a proof of concept. Use at your own risk! Songs might be cut unproperly if provided timestamps don't match
the actual songs in the video! Tested on Linux only.
Year: 2020
Author: Marjan Moderc
github: https://github.com/marjanmo
"""

#YOUR INPUTS GO BELOW!:

# Link of the youtube music video that you want split.
YOUTUBE_LINK = 'https://www.youtube.com/watch?v=MGVyRjPRh3k'

# Info about songs
# Can usually be found in description of in the topmost comments.
# Copy/paste playlist with timestamps in a text file that will reside next to this script.
# You have to change the separator and the order of INFO list to match the original list. Be consistent!
# You might need some text file editing to match given criteria!
# INFO variable must have 2 or 3 elements. Adjust ordering of elements to match the file contents.
# TIME and TITLE are neccessary, ARTIST is optional, if downloading compilation! If not in the file, specifiy artist
# separately

TRACKLIST_FILE = "/mnt/e/rafi/work/repo/Proleter.txt"  #Text file to be put next to the script!
INFO = ["TIME","TITLE"] #what info does the textfile contain and what is the order
SEPARATOR = " - "

# Constants for  ID3 mp3 TAGGING
ARTIST = "Audrie Storme" #Will be obtained from the tracklist if specified.
ALBUM = "songs to start your day 🎵 a lo-fi mix"
YEAR = 2000


#DEMO FOLDER -- Script root
SAVE_FOLDER = os.path.dirname(os.path.realpath(__file__))  #Will be crated if not exist


#DEMO TEXT FILE - will be created for demo purposes, you should create it yourself for your own video.
with open(TRACKLIST_FILE, "w") as f:
    f.write("00:00 - Easy Feet\n 0:02:03 - Before Chill\n 0:04:13 - I Need This\n 0:06:44 - Something in the Air\n 0:08:47 - A Love Waltz\n 0:11:44 - Patience\n 0:13:56 - Lilacs\n 0:16:15 - Golden Navel\n 0:17:35 - 368\n 0:19:55 - Coffee And Unicorns\n 0:22:37 - The Rain\n 0:25:24 - Imaginary Friends\n 0:28:07 - Paper Crane\n 0:31:09 - More Scrubs\n 0:33:41 - Purple Clouds\n 0:35:56 - Cashmere\n 0:38:17 - Corn Dog Connoisseur\n 0:40:32 - Controlled Cruisin\n 0:42:39 - Just Perusing\n 0:45:15 - Warm Water\n 0:47:47 - Flowers\n 0:49:50 - Minor Leagues\n 0:51:53 - Elysian\n 0:54:14 - Amber Lights\n 0:57:44 - So Many Clouds")


##################################################
### Dont (have to) touch anything below this! ####
##################################################


# Try to autoinstall missing modules...
try:
    import youtube_dl
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'youtube_dl'])
    import youtube_dl

try:
    import pydub
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'pydub'])

    import pydub



# Helper function
def time_to_seconds(time_str):
    if len(time_str.split(":")) == 2:
        m, s = time_str.split(':')
        return int(m) * 60 + int(s)
    else:
        h, m, s = time_str.split(':')
        return int(h) * 3600 + int(m) * 60 + int(s)


# 1. Download the video  to temporary file (couldn't make youtube_dl to create mp3 that pydub would eat happily)
ydl_opts = {
    'outtmpl': 'tmp.mp4',
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]'
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    a = ydl.download([YOUTUBE_LINK])

# 2. Read the songs info
with open(TRACKLIST_FILE, "r") as f:
    songs = f.readlines()
    songs = [i.strip("\n").strip("").split(SEPARATOR) for i in songs]

# 3. Read mp4 as AudioSegment
print("Reading source mp3 file ...")
sound = pydub.AudioSegment.from_file("tmp.mp4","mp4")
print("Done.")

# 4. Create a destination folder if doesnt exist
if not os.path.exists(SAVE_FOLDER):
    os.mkdir(SAVE_FOLDER)

INFO = [i.lower() for i in INFO] #idiot proofing

# 5. Extract songs separately.
for i,j in enumerate(songs):
    print("Converting song no.",i,j)

    artist = j[INFO.index("artist")] if "artist" in INFO else ARTIST
    time_start = j[INFO.index("time")]
    title = j[INFO.index("title")]

    time_start = time_to_seconds(time_start)*1000

    # Last one have special treatment...
    if i+1 == len(songs):
        song = sound[time_start:-1]
    else:
        time_finish = time_to_seconds(songs[i+1][INFO.index("time")])*1000-200 #time to the next one!
        song = sound[time_start:time_finish]

    song.export(os.path.join(SAVE_FOLDER,"{} - {}.mp3".format(artist,title)), format="mp3",
                tags={"artist":artist,"album":ALBUM,"title":title, "track": i+1})

# 5. Clean temporary file.
os.remove("tmp.mp4")