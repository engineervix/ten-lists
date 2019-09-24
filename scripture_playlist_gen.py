#!/usr/bin/env python3

"""
    Scripture Playlist Generator.
    Copyright (C) 2014-2019  Victor Miti

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import os
import glob
import argparse
from shutil import copy
import eyed3

from colorama import init, Fore, Style

# Initialize the colorama colored command line output
init()

__author__ = "Victor Miti"
__copyright__ = "Copyright (C) 2014-2019, Victor Miti"
__credits__ = ['']
__license__ = "GPL"
__version__ = "0.5"
__maintainer__ = "Victor Miti"
__email__ = "victormiti@umusebo.com"
__status__ = "Production/Stable"

"""
-----------------------------Description--------------------------------
This python script generates an m3u playlist of 10 Bible Chapters
(represented by 10 mp3 files) to be listened to on any given day x,
according to Professor Grant Horner's Bible-Reading System
(http://www.thevinefellowship.com/10Lists.pdf)
The audio Bible is as downloaded from the <Faith Comes by Hearing®> website
(http://www.bible.is/audiodownloader)

Has been tested on Python 3.6 & 3.7.
---------------------------------------------------------------------------
"""

print(Fore.YELLOW)

parser = argparse.ArgumentParser(
    description='generates an m3u playlist of 10 Bible Chapters for day X of \
                 Bible plan.')
parser.add_argument('day', metavar='X', type=int,
                    help='the day of the reading plan, eg 6 for day 6')
args = parser.parse_args()

if args.day < 1:
    parser.error("It's from Day 1 onwards.")
else:
    # x represents the day, as in day x...
    # ...This will be passed from the commandline as an argument variable
    x = args.day

print(Style.RESET_ALL)  # reset colorama terminal colour enhancements

# first let us create the 10 lists from the text files

reading_lists = []

list_dir = os.path.join(os.getcwd(), "lists")
filelist = glob.glob(os.path.join(list_dir, '*.txt'))

for fname in sorted(filelist):
    with open(fname) as f:
        reading_lists.append(f.read().splitlines())

list_1 = reading_lists[0]
list_2 = reading_lists[1]
list_3 = reading_lists[2]
list_4 = reading_lists[3]
list_5 = reading_lists[4]
list_6 = reading_lists[5]
list_7 = reading_lists[6]
list_8 = reading_lists[7]
list_9 = reading_lists[8]
list_10 = reading_lists[9]

# -----------------Now we create a new list(our reading list)-----------------#

# Change this to suit your directory. Note the trailing "/"
BIBLE_DIRECTORY = "ENGESVC2DA/"

SUCCESS_MSG = f"\nThe playlist for day {str(x)} has been created " + \
              "successfully.\n"
ERROR_MSG = f"\nThere was a problem in creating a playlist for day {str(x)}.\n"


def add_to_m3u(content):
    """appends content to an m3u file"""
    with open("day"+str(x).zfill(3)+".m3u", "a") as m3u:
        m3u.write(f"{content}\n")


try:
    # for indexing purposes. Remember that
    # the first index is represented by zero!
    z = x - 1
    current_reading_list = [bible_list[z] for bible_list in reading_lists]
    add_to_m3u("#EXTM3U")
    for item in current_reading_list:
        add_to_m3u(BIBLE_DIRECTORY + item)
    print(SUCCESS_MSG)

except IndexError:
    if len(reading_lists[6]) >= x > len(reading_lists[9]):
        current_reading_list = [bible_list[z]
                                for bible_list in reading_lists[:-1]]
        add_to_m3u("#EXTM3U")
        for item in current_reading_list:
            add_to_m3u(BIBLE_DIRECTORY + item)
        z = x - 1 - len(reading_lists[9])
        add_to_m3u(BIBLE_DIRECTORY + list_10[z])
        print(SUCCESS_MSG)

    if len(reading_lists[4]) >= x > len(reading_lists[6]):
        current_reading_list = [bible_list[z]
                                for bible_list in reading_lists[:-4]]
        add_to_m3u("#EXTM3U")
        for item in current_reading_list:
            add_to_m3u(BIBLE_DIRECTORY + item)
        z = x - 1 - len(reading_lists[6])
        add_to_m3u(BIBLE_DIRECTORY + list_7[z])
        add_to_m3u(BIBLE_DIRECTORY + list_8[x-1])
        add_to_m3u(BIBLE_DIRECTORY + list_9[x-1])
        z = x - 1 - len(reading_lists[9])
        while z >= len(reading_lists[9]):
            z = z - len(reading_lists[9])
        add_to_m3u(BIBLE_DIRECTORY + list_10[z])
        print(SUCCESS_MSG)

    if len(reading_lists[3]) >= x > len(reading_lists[4]):
        current_reading_list = [bible_list[z]
                                for bible_list in reading_lists[:4]]
        add_to_m3u("#EXTM3U")
        for item in current_reading_list:
            add_to_m3u(BIBLE_DIRECTORY+item)
        z = x - 1 - len(reading_lists[4])
        add_to_m3u(BIBLE_DIRECTORY + list_5[z])
        add_to_m3u(BIBLE_DIRECTORY + list_6[x-1])
        z = x - 1 - len(reading_lists[6])
        while z >= len(reading_lists[6]):
            z = z - len(reading_lists[6])
        add_to_m3u(BIBLE_DIRECTORY + list_7[z])
        add_to_m3u(BIBLE_DIRECTORY + list_8[x-1])
        add_to_m3u(BIBLE_DIRECTORY + list_9[x-1])
        z = x - 1 - len(reading_lists[9])
        while z >= len(reading_lists[9]):
            z = z - len(reading_lists[9])
        add_to_m3u(BIBLE_DIRECTORY + list_10[z])
        print(SUCCESS_MSG)

    if len(reading_lists[2]) >= x > len(reading_lists[3]):
        current_reading_list = [bible_list[z]
                                for bible_list in reading_lists[:3]]
        add_to_m3u("#EXTM3U")
        for item in current_reading_list:
            add_to_m3u(BIBLE_DIRECTORY + item)
        z = x - 1 - len(reading_lists[3])
        add_to_m3u(BIBLE_DIRECTORY + list_4[z])
        z = x - 1 - len(reading_lists[4])
        while z >= len(reading_lists[4]):
            z = z - len(reading_lists[4])
        add_to_m3u(BIBLE_DIRECTORY + list_5[z])
        add_to_m3u(BIBLE_DIRECTORY + list_6[x-1])
        z = x - 1 - len(reading_lists[6])
        while z >= len(reading_lists[6]):
            z = z - len(reading_lists[6])
        add_to_m3u(BIBLE_DIRECTORY + list_7[z])
        add_to_m3u(BIBLE_DIRECTORY + list_8[x-1])
        add_to_m3u(BIBLE_DIRECTORY + list_9[x-1])
        z = x - 1 - len(reading_lists[9])
        while z >= len(reading_lists[9]):
            z = z - len(reading_lists[9])
        add_to_m3u(BIBLE_DIRECTORY + list_10[z])
        print(SUCCESS_MSG)

    if len(reading_lists[0]) >= x > len(reading_lists[2]):
        current_reading_list = [bible_list[z]
                                for bible_list in reading_lists[:2]]
        add_to_m3u("#EXTM3U")
        for item in current_reading_list:
            add_to_m3u(BIBLE_DIRECTORY+item)
        z = x - 1 - len(reading_lists[2])
        add_to_m3u(BIBLE_DIRECTORY + list_3[z])
        z = x - 1 - len(reading_lists[3])
        while z >= len(reading_lists[3]):
            z = z - len(reading_lists[3])
        add_to_m3u(BIBLE_DIRECTORY + list_4[z])
        z = x - 1 - len(reading_lists[4])
        while z >= len(reading_lists[4]):
            z = z - len(reading_lists[4])
        add_to_m3u(BIBLE_DIRECTORY + list_5[z])
        add_to_m3u(BIBLE_DIRECTORY + list_6[x-1])
        z = x - 1 - len(reading_lists[6])
        while z >= len(reading_lists[6]):
            z = z - len(reading_lists[6])
        add_to_m3u(BIBLE_DIRECTORY + list_7[z])
        add_to_m3u(BIBLE_DIRECTORY + list_8[x-1])
        add_to_m3u(BIBLE_DIRECTORY + list_9[x-1])
        z = x - 1 - len(reading_lists[9])
        while z >= len(reading_lists[9]):
            z = z - len(reading_lists[9])
        add_to_m3u(BIBLE_DIRECTORY + list_10[z])
        print(SUCCESS_MSG)

    if len(reading_lists[5]) >= x > len(reading_lists[0]):
        add_to_m3u("#EXTM3U")
        z = x - 1 - len(reading_lists[0])
        while z >= len(reading_lists[0]):
            z = z - len(reading_lists[0])
        add_to_m3u(BIBLE_DIRECTORY + list_1[z])
        add_to_m3u(BIBLE_DIRECTORY + list_2[x-1])
        z = x - 1 - len(reading_lists[2])
        while z >= len(reading_lists[2]):
            z = z - len(reading_lists[2])
        add_to_m3u(BIBLE_DIRECTORY + list_3[z])
        z = x - 1 - len(reading_lists[3])
        while z >= len(reading_lists[3]):
            z = z - len(reading_lists[3])
        add_to_m3u(BIBLE_DIRECTORY + list_4[z])
        z = x - 1 - len(reading_lists[4])
        while z >= len(reading_lists[4]):
            z = z - len(reading_lists[4])
        add_to_m3u(BIBLE_DIRECTORY + list_5[z])
        add_to_m3u(BIBLE_DIRECTORY + list_6[x-1])
        z = x - 1 - len(reading_lists[6])
        while z >= len(reading_lists[6]):
            z = z - len(reading_lists[6])
        add_to_m3u(BIBLE_DIRECTORY + list_7[z])
        add_to_m3u(BIBLE_DIRECTORY + list_8[x-1])
        add_to_m3u(BIBLE_DIRECTORY + list_9[x-1])
        z = x - 1 - len(reading_lists[9])
        while z >= len(reading_lists[9]):
            z = z - len(reading_lists[9])
        add_to_m3u(BIBLE_DIRECTORY + list_10[z])
        print(SUCCESS_MSG)

    if len(reading_lists[1]) >= x > len(reading_lists[5]):
        add_to_m3u("#EXTM3U")
        z = x - 1 - len(reading_lists[0])
        while z >= len(reading_lists[0]):
            z = z - len(reading_lists[0])
        add_to_m3u(BIBLE_DIRECTORY + list_1[z])
        add_to_m3u(BIBLE_DIRECTORY + list_2[x-1])
        z = x - 1 - len(reading_lists[2])
        while z >= len(reading_lists[2]):
            z = z - len(reading_lists[2])
        add_to_m3u(BIBLE_DIRECTORY + list_3[z])
        z = x - 1 - len(reading_lists[3])
        while z >= len(reading_lists[3]):
            z = z - len(reading_lists[3])
        add_to_m3u(BIBLE_DIRECTORY + list_4[z])
        z = x - 1 - len(reading_lists[4])
        while z >= len(reading_lists[4]):
            z = z - len(reading_lists[4])
        add_to_m3u(BIBLE_DIRECTORY + list_5[z])
        z = x - 1 - len(reading_lists[5])
        while z >= len(reading_lists[5]):
            z = z - len(reading_lists[5])
        add_to_m3u(BIBLE_DIRECTORY + list_6[z])
        z = x - 1 - len(reading_lists[6])
        while z >= len(reading_lists[6]):
            z = z - len(reading_lists[6])
        add_to_m3u(BIBLE_DIRECTORY + list_7[z])
        add_to_m3u(BIBLE_DIRECTORY + list_8[x-1])
        add_to_m3u(BIBLE_DIRECTORY + list_9[x-1])
        z = x - 1 - len(reading_lists[9])
        while z >= len(reading_lists[9]):
            z = z - len(reading_lists[9])
        add_to_m3u(BIBLE_DIRECTORY + list_10[z])
        print(SUCCESS_MSG)

    if len(reading_lists[7]) >= x > len(reading_lists[1]):
        add_to_m3u("#EXTM3U")
        z = x - 1 - len(reading_lists[0])
        while z >= len(reading_lists[0]):
            z = z - len(reading_lists[0])
        add_to_m3u(BIBLE_DIRECTORY + list_1[z])
        z = x - 1 - len(reading_lists[1])
        while z >= len(reading_lists[1]):
            z = z - len(reading_lists[1])
        add_to_m3u(BIBLE_DIRECTORY + list_2[z])
        z = x - 1 - len(reading_lists[2])
        while z >= len(reading_lists[2]):
            z = z - len(reading_lists[2])
        add_to_m3u(BIBLE_DIRECTORY + list_3[z])
        z = x - 1 - len(reading_lists[3])
        while z >= len(reading_lists[3]):
            z = z - len(reading_lists[3])
        add_to_m3u(BIBLE_DIRECTORY + list_4[z])
        z = x - 1 - len(reading_lists[4])
        while z >= len(reading_lists[4]):
            z = z - len(reading_lists[4])
        add_to_m3u(BIBLE_DIRECTORY + list_5[z])
        z = x - 1 - len(reading_lists[5])
        while z >= len(reading_lists[5]):
            z = z - len(reading_lists[5])
        add_to_m3u(BIBLE_DIRECTORY + list_6[z])
        z = x - 1 - len(reading_lists[6])
        while z >= len(reading_lists[6]):
            z = z - len(reading_lists[6])
        add_to_m3u(BIBLE_DIRECTORY + list_7[z])
        add_to_m3u(BIBLE_DIRECTORY + list_8[x-1])
        add_to_m3u(BIBLE_DIRECTORY + list_9[x-1])
        z = x - 1 - len(reading_lists[9])
        while z >= len(reading_lists[9]):
            z = z - len(reading_lists[9])
        add_to_m3u(BIBLE_DIRECTORY + list_10[z])
        print(SUCCESS_MSG)

    if len(reading_lists[8]) >= x > len(reading_lists[7]):
        add_to_m3u("#EXTM3U")
        z = x - 1 - len(reading_lists[0])
        while z >= len(reading_lists[0]):
            z = z - len(reading_lists[0])
        add_to_m3u(BIBLE_DIRECTORY + list_1[z])
        z = x - 1 - len(reading_lists[1])
        while z >= len(reading_lists[1]):
            z = z - len(reading_lists[1])
        add_to_m3u(BIBLE_DIRECTORY + list_2[z])
        z = x - 1 - len(reading_lists[2])
        while z >= len(reading_lists[2]):
            z = z - len(reading_lists[2])
        add_to_m3u(BIBLE_DIRECTORY + list_3[z])
        z = x - 1 - len(reading_lists[3])
        while z >= len(reading_lists[3]):
            z = z - len(reading_lists[3])
        add_to_m3u(BIBLE_DIRECTORY + list_4[z])
        z = x - 1 - len(reading_lists[4])
        while z >= len(reading_lists[4]):
            z = z - len(reading_lists[4])
        add_to_m3u(BIBLE_DIRECTORY + list_5[z])
        z = x - 1 - len(reading_lists[5])
        while z >= len(reading_lists[5]):
            z = z - len(reading_lists[5])
        add_to_m3u(BIBLE_DIRECTORY + list_6[z])
        z = x - 1 - len(reading_lists[6])
        while z >= len(reading_lists[6]):
            z = z - len(reading_lists[6])
        add_to_m3u(BIBLE_DIRECTORY + list_7[z])
        z = x - 1 - len(reading_lists[7])
        while z >= len(reading_lists[7]):
            z = z - len(reading_lists[7])
        add_to_m3u(BIBLE_DIRECTORY + list_8[z])
        add_to_m3u(BIBLE_DIRECTORY + list_9[x-1])
        z = x - 1 - len(reading_lists[9])
        while z >= len(reading_lists[9]):
            z = z - len(reading_lists[9])
        add_to_m3u(BIBLE_DIRECTORY + list_10[z])
        print(SUCCESS_MSG)

    if x > len(reading_lists[8]):
        add_to_m3u("#EXTM3U")
        z = x - 1 - len(reading_lists[0])
        while z >= len(reading_lists[0]):
            z = z - len(reading_lists[0])
        add_to_m3u(BIBLE_DIRECTORY + list_1[z])
        z = x - 1 - len(reading_lists[1])
        while z >= len(reading_lists[1]):
            z = z - len(reading_lists[1])
        add_to_m3u(BIBLE_DIRECTORY + list_2[z])
        z = x - 1 - len(reading_lists[2])
        while z >= len(reading_lists[2]):
            z = z - len(reading_lists[2])
        add_to_m3u(BIBLE_DIRECTORY + list_3[z])
        z = x - 1 - len(reading_lists[3])
        while z >= len(reading_lists[3]):
            z = z - len(reading_lists[3])
        add_to_m3u(BIBLE_DIRECTORY + list_4[z])
        z = x - 1 - len(reading_lists[4])
        while z >= len(reading_lists[4]):
            z = z - len(reading_lists[4])
        add_to_m3u(BIBLE_DIRECTORY + list_5[z])
        z = x - 1 - len(reading_lists[5])
        while z >= len(reading_lists[5]):
            z = z - len(reading_lists[5])
        add_to_m3u(BIBLE_DIRECTORY + list_6[z])
        z = x - 1 - len(reading_lists[6])
        while z >= len(reading_lists[6]):
            z = z - len(reading_lists[6])
        add_to_m3u(BIBLE_DIRECTORY + list_7[z])
        z = x - 1 - len(reading_lists[7])
        while z >= len(reading_lists[7]):
            z = z - len(reading_lists[7])
        add_to_m3u(BIBLE_DIRECTORY + list_8[z])
        z = x - 1 - len(reading_lists[8])
        while z >= len(reading_lists[8]):
            z = z - len(reading_lists[8])
        add_to_m3u(BIBLE_DIRECTORY + list_9[z])
        z = x - 1 - len(reading_lists[9])
        while z >= len(reading_lists[9]):
            z = z - len(reading_lists[9])
        add_to_m3u(BIBLE_DIRECTORY + list_10[z])
        print(SUCCESS_MSG)

# Now we copy the files into a new folder
out_dir = "day"+str(x).zfill(3)

if not os.path.exists(out_dir):
    os.makedirs(out_dir)

playlist_file = open(r"day"+str(x).zfill(3)+".m3u", "r")

for i in playlist_file.readlines():
    if i.startswith(BIBLE_DIRECTORY):
        tmp = list(i.strip())
        copy("".join(tmp), out_dir)

playlist_file.close()

print("\nCopying of the Bible Chapters into the " +
      out_dir + " directory was successful.\n")

# We now change the ID3 tag information (track number)
# We also rename the files in the destination directory
track_number = 1

playlist_file = open(r"day"+str(x).zfill(3)+".m3u", "r")

for i in playlist_file.readlines():
    if i.startswith(BIBLE_DIRECTORY):
        tmp = list(i.strip().replace(BIBLE_DIRECTORY, out_dir+'/', 1))
        f = "".join(tmp)
        audiofile = eyed3.load(f)
        audiofile.tag.track_num = track_number
        audiofile.tag.save()
        filename = f.replace(out_dir+'/', '')
        # add a filename prefix with leading zeroes
        f_new = out_dir+'/'+str(track_number).zfill(3) + filename[3:]
        os.rename(f, f_new)
        track_number += 1

playlist_file.close()

print(f"{Fore.CYAN}\nID3 tag info for the files in this "
      "directory has been updated.\n")
print("\nThe files have been renamed in a sequential order."
      f"\n\n-----Soli Deo Gloria-----\n{Style.RESET_ALL}")
