"""
For Testing Purposes, we'll replicate a typical directory containing the
audio bible. The actual directory is over 2Gb.

What we'll do is programmatically create an mp3 file using the
`gTTS <https://pypi.org/project/gTTS/>`_ library and make copies following
the naming convention used in the 2Gb+ Audio Bible Directory.

Note that the gTTS library requires an internet connection.

"""

import os
import glob
from shutil import copy
import timeit
from gtts import gTTS
import eyed3
from tqdm import tqdm

start = timeit.default_timer()

BIBLE_DIRECTORY = "ENGESVC2DA"

# first let us create the 10 lists from the text files

reading_lists = []

list_dir = os.path.join(os.getcwd(), "lists")
filelist = glob.glob(os.path.join(list_dir, '*.txt'))

for fname in sorted(filelist):
    with open(fname) as f:
        reading_lists.append(f.read().splitlines())

# now we go programmatically create an audio file

tts = gTTS('audio', lang='en')
audio_file = os.path.join(os.getcwd(), "audio_file.mp3")
tts.save(audio_file)

# add ID3 tag info to the file
mp3_file = eyed3.load(audio_file)
mp3_file.initTag()
mp3_file.tag.artist = u"test"
mp3_file.tag.track_num = 1
mp3_file.tag.save()

# we then make multiple copies of the audio file

for bible_list in tqdm(reading_lists):
    for mp3 in bible_list:
        new_mp3_file = os.path.join(BIBLE_DIRECTORY, mp3)
        copy(audio_file, new_mp3_file)

stop = timeit.default_timer()
total_time = stop - start

print(f"Total running time: {total_time} seconds")
