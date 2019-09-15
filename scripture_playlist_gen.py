#!/usr/bin/env python3

'''
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
'''

import sys
import os
import argparse
from shutil import copy
import eyed3

from colorama import init, Fore, Back, Style

# Initialize the colorma colored command line output
init()

__author__ = "Victor Miti"
__copyright__ = "Copyright (C) 2014-2019, Victor Miti"
__credits__ = ['']
__license__ = "GPL"
__version__ = "0.5"
__maintainer__ = "Victor Miti"
__email__ = "victormiti@umusebo.com"
__status__ = "Production/Stable"

'''-----------------------------Description--------------------------------
This python script generates an m3u playlist of 10 Bible Chapters
(represented by 10 mp3 files) to be listened to on any given day x,
according to Professor Grant Horner's Bible-Reading System
(http://www.thevinefellowship.com/10Lists.pdf)
The audio Bible is as downloaded from the <Faith Comes by Hearing®> website
(http://www.bible.is/audiodownloader)

Has been tested on Python 3.6 & 3.7.

------------------------------------------------------------------------'''

'''-------------------------------Changelog-----------------------------------
version 0.5 (2019-06-22):
- switched to python3

version 0.4 (2015-05-11):
- changed the naming convention of files and directories by enforcing a 3-digit
number by padding with zeroes using the `zfill()` function. This was done
because I noticed that when I was creating a one week playlist from day 96 to
102; `day100` was considered as occuring before `day96` during processing, which
isn't the case. This is because of the `1` after the `day`. Thus, to fix the
problem, we need to have `day096` instead of `day96`.

version 0.3:
- Added the ability to change ID3 tag info in the copied files, so that
whenever you play the files from any device (eg car, home theatre),
the desired order is maintained.
- Added the ability to rename the files so that their sequence follows the
desired reading plan order, instead of the order of appearance in the Bible.
Key Modules: eyed3, os.rename

version 0.2:
-Added the ability to copy the files on the playlist file into a new folder
so that you can carry the folder and listen anywhere (car, home theatre, etc)
Key Module: shutil

version 0.1:
-Initial version
---------------------------------------------------------------------------'''

print(Fore.YELLOW)

parser = argparse.ArgumentParser(
    description='generates an m3u playlist of 10 Bible Chapters for day X of Bible plan.')
parser.add_argument('day', metavar='X', type=int,
                    help='the day of the reading plan, eg 6 for day 6')
args = parser.parse_args()

if args.day < 1:
    parser.error("It's from Day 1 onwards.")
else:
    # x represents the day, as in day x...
    #...This will be passed from the commandline as an argument variable
    x = args.day

print(Style.RESET_ALL)  # reset colorama terminal colour enhancements

# first let us create the 10 lists from the text files
for count in range(1,11):
    exec("list_{} = {}".format(count, open("lists/list"+str(count)+".txt").read().splitlines()))
    exec("list_{}_length = len(list_{})".format(count, count))

#-----------------Now we create a new list(our reading list)-----------------#

BIBLE_DIRECTORY = "ENGESVC2DA/" # Change this to suit your directory. Note the trailing "/"

# redirect stdout to an .m3u file in the same directory
sys.stdout = open("day"+str(x).zfill(3)+".m3u", "w")

SUCCESS_MSG = sys.stderr.write("\nThe playlist for day "+str(x)+" has been created successfully.\n")

try:
    z = x - 1   # for indexing purposes. Remember that the first index is represented by zero!
    exec("reading_list_{} = {}".format(x, ','.join("list_"+str(j)+"["+str(z)+"]" for j in range(1,11))))
    print("#EXTM3U")
    exec("my_reading_list = reading_list_{}".format(x))
    for item in my_reading_list:
        print(BIBLE_DIRECTORY+item)
    SUCCESS_MSG

except IndexError:
    if list_7_length >= x > list_10_length:
        exec("reading_list_{} = {}".format(x, ','.join("list_"+str(j)+"["+str(z)+"]" for j in range(1,10))))
        print("#EXTM3U")
        exec("my_reading_list = reading_list_{}".format(x))
        for item in my_reading_list:
            print(BIBLE_DIRECTORY+item)
        z = x - 1 - list_10_length
        print(BIBLE_DIRECTORY+list_10[z])
        SUCCESS_MSG

    if list_5_length >= x > list_7_length:
        exec("reading_list_{} = {}".format(x, ','.join("list_"+str(j)+"["+str(z)+"]" for j in range(1,7))))
        print("#EXTM3U")
        exec("my_reading_list = reading_list_{}".format(x))
        for item in my_reading_list:
            print(BIBLE_DIRECTORY+item)
        z = x - 1 - list_7_length
        print(BIBLE_DIRECTORY+list_7[z])
        print(BIBLE_DIRECTORY+list_8[x-1])
        print(BIBLE_DIRECTORY+list_9[x-1])
        z = x - 1 - list_10_length
        while z >= list_10_length:
            z = z - list_10_length
        print(BIBLE_DIRECTORY+list_10[z])
        SUCCESS_MSG

    if list_4_length >= x > list_5_length:
        exec("reading_list_{} = {}".format(x, ','.join("list_"+str(j)+"["+str(z)+"]" for j in range(1,5))))
        print("#EXTM3U")
        exec("my_reading_list = reading_list_{}".format(x))
        for item in my_reading_list:
            print(BIBLE_DIRECTORY+item)
        z = x - 1 - list_5_length
        print(BIBLE_DIRECTORY+list_5[z])
        print(BIBLE_DIRECTORY+list_6[x-1])
        z = x - 1 - list_7_length
        while z >= list_7_length:
            z = z - list_7_length
        print(BIBLE_DIRECTORY+list_7[z])
        print(BIBLE_DIRECTORY+list_8[x-1])
        print(BIBLE_DIRECTORY+list_9[x-1])
        z = x - 1 - list_10_length
        while z >= list_10_length:
            z = z - list_10_length
        print(BIBLE_DIRECTORY+list_10[z])
        SUCCESS_MSG

    if list_3_length >= x > list_4_length:
        exec("reading_list_{} = {}".format(x, ','.join("list_"+str(j)+"["+str(z)+"]" for j in range(1,4))))
        print("#EXTM3U")
        exec("my_reading_list = reading_list_{}".format(x))
        for item in my_reading_list:
            print(BIBLE_DIRECTORY+item)
        z = x - 1 - list_4_length
        print(BIBLE_DIRECTORY+list_4[z])
        z = x - 1 - list_5_length
        while z >= list_5_length:
            z = z - list_5_length
        print(BIBLE_DIRECTORY+list_5[z])
        print(BIBLE_DIRECTORY+list_6[x-1])
        z = x - 1 - list_7_length
        while z >= list_7_length:
            z = z - list_7_length
        print(BIBLE_DIRECTORY+list_7[z])
        print(BIBLE_DIRECTORY+list_8[x-1])
        print(BIBLE_DIRECTORY+list_9[x-1])
        z = x - 1 - list_10_length
        while z >= list_10_length:
            z = z - list_10_length
        print(BIBLE_DIRECTORY+list_10[z])
        SUCCESS_MSG

    if list_1_length >= x > list_3_length:
        exec("reading_list_{} = {}".format(x, ','.join("list_"+str(j)+"["+str(z)+"]" for j in range(1,3))))
        print("#EXTM3U")
        exec("my_reading_list = reading_list_{}".format(x))
        for item in my_reading_list:
            print(BIBLE_DIRECTORY+item)
        z = x - 1 - list_3_length
        print(BIBLE_DIRECTORY+list_3[z])
        z = x - 1 - list_4_length
        while z >= list_4_length:
            z = z - list_4_length
        print(BIBLE_DIRECTORY+list_4[z])
        z = x - 1 - list_5_length
        while z >= list_5_length:
            z = z - list_5_length
        print(BIBLE_DIRECTORY+list_5[z])
        print(BIBLE_DIRECTORY+list_6[x-1])
        z = x - 1 - list_7_length
        while z >= list_7_length:
            z = z - list_7_length
        print(BIBLE_DIRECTORY+list_7[z])
        print(BIBLE_DIRECTORY+list_8[x-1])
        print(BIBLE_DIRECTORY+list_9[x-1])
        z = x - 1 - list_10_length
        while z >= list_10_length:
            z = z - list_10_length
        print(BIBLE_DIRECTORY+list_10[z])
        SUCCESS_MSG

    if list_6_length >= x > list_1_length:
        print("#EXTM3U")
        z = x - 1 - list_1_length
        while z >= list_1_length:
            z = z - list_1_length
        print(BIBLE_DIRECTORY+list_1[z])
        print(BIBLE_DIRECTORY+list_2[x-1])
        z = x - 1 - list_3_length
        while z >= list_3_length:
            z = z - list_3_length
        print(BIBLE_DIRECTORY+list_3[z])
        z = x - 1 - list_4_length
        while z >= list_4_length:
            z = z - list_4_length
        print(BIBLE_DIRECTORY+list_4[z])
        z = x - 1 - list_5_length
        while z >= list_5_length:
            z = z - list_5_length
        print(BIBLE_DIRECTORY+list_5[z])
        print(BIBLE_DIRECTORY+list_6[x-1])
        z = x - 1 - list_7_length
        while z >= list_7_length:
            z = z - list_7_length
        print(BIBLE_DIRECTORY+list_7[z])
        print(BIBLE_DIRECTORY+list_8[x-1])
        print(BIBLE_DIRECTORY+list_9[x-1])
        z = x - 1 - list_10_length
        while z >= list_10_length:
            z = z - list_10_length
        print(BIBLE_DIRECTORY+list_10[z])
        SUCCESS_MSG

    if list_2_length >= x > list_6_length:
        print("#EXTM3U")
        z = x - 1 - list_1_length
        while z >= list_1_length:
            z = z - list_1_length
        print(BIBLE_DIRECTORY+list_1[z])
        print(BIBLE_DIRECTORY+list_2[x-1])
        z = x - 1 - list_3_length
        while z >= list_3_length:
            z = z - list_3_length
        print(BIBLE_DIRECTORY+list_3[z])
        z = x - 1 - list_4_length
        while z >= list_4_length:
            z = z - list_4_length
        print(BIBLE_DIRECTORY+list_4[z])
        z = x - 1 - list_5_length
        while z >= list_5_length:
            z = z - list_5_length
        print(BIBLE_DIRECTORY+list_5[z])
        z = x - 1 - list_6_length
        while z >= list_6_length:
            z = z - list_6_length
        print(BIBLE_DIRECTORY+list_6[z])
        z = x - 1 - list_7_length
        while z >= list_7_length:
            z = z - list_7_length
        print(BIBLE_DIRECTORY+list_7[z])
        print(BIBLE_DIRECTORY+list_8[x-1])
        print(BIBLE_DIRECTORY+list_9[x-1])
        z = x - 1 - list_10_length
        while z >= list_10_length:
            z = z - list_10_length
        print(BIBLE_DIRECTORY+list_10[z])
        SUCCESS_MSG

    if list_8_length >= x > list_2_length:
        print("#EXTM3U")
        z = x - 1 - list_1_length
        while z >= list_1_length:
            z = z - list_1_length
        print(BIBLE_DIRECTORY+list_1[z])
        z = x - 1 - list_2_length
        while z >= list_2_length:
            z = z - list_2_length
        print(BIBLE_DIRECTORY+list_2[z])
        z = x - 1 - list_3_length
        while z >= list_3_length:
            z = z - list_3_length
        print(BIBLE_DIRECTORY+list_3[z])
        z = x - 1 - list_4_length
        while z >= list_4_length:
            z = z - list_4_length
        print(BIBLE_DIRECTORY+list_4[z])
        z = x - 1 - list_5_length
        while z >= list_5_length:
            z = z - list_5_length
        print(BIBLE_DIRECTORY+list_5[z])
        z = x - 1 - list_6_length
        while z >= list_6_length:
            z = z - list_6_length
        print(BIBLE_DIRECTORY+list_6[z])
        z = x - 1 - list_7_length
        while z >= list_7_length:
            z = z - list_7_length
        print(BIBLE_DIRECTORY+list_7[z])
        print(BIBLE_DIRECTORY+list_8[x-1])
        print(BIBLE_DIRECTORY+list_9[x-1])
        z = x - 1 - list_10_length
        while z >= list_10_length:
            z = z - list_10_length
        print(BIBLE_DIRECTORY+list_10[z])
        SUCCESS_MSG

    if list_9_length >= x > list_8_length:
        print("#EXTM3U")
        z = x - 1 - list_1_length
        while z >= list_1_length:
            z = z - list_1_length
        print(BIBLE_DIRECTORY+list_1[z])
        z = x - 1 - list_2_length
        while z >= list_2_length:
            z = z - list_2_length
        print(BIBLE_DIRECTORY+list_2[z])
        z = x - 1 - list_3_length
        while z >= list_3_length:
            z = z - list_3_length
        print(BIBLE_DIRECTORY+list_3[z])
        z = x - 1 - list_4_length
        while z >= list_4_length:
            z = z - list_4_length
        print(BIBLE_DIRECTORY+list_4[z])
        z = x - 1 - list_5_length
        while z >= list_5_length:
            z = z - list_5_length
        print(BIBLE_DIRECTORY+list_5[z])
        z = x - 1 - list_6_length
        while z >= list_6_length:
            z = z - list_6_length
        print(BIBLE_DIRECTORY+list_6[z])
        z = x - 1 - list_7_length
        while z >= list_7_length:
            z = z - list_7_length
        print(BIBLE_DIRECTORY+list_7[z])
        z = x - 1 - list_8_length
        while z >= list_8_length:
            z = z - list_8_length
        print(BIBLE_DIRECTORY+list_8[z])
        print(BIBLE_DIRECTORY+list_9[x-1])
        z = x - 1 - list_10_length
        while z >= list_10_length:
            z = z - list_10_length
        print(BIBLE_DIRECTORY+list_10[z])
        SUCCESS_MSG

    if x > list_9_length:
        print("#EXTM3U")
        z = x - 1 - list_1_length
        while z >= list_1_length:
            z = z - list_1_length
        print(BIBLE_DIRECTORY+list_1[z])
        z = x - 1 - list_2_length
        while z >= list_2_length:
            z = z - list_2_length
        print(BIBLE_DIRECTORY+list_2[z])
        z = x - 1 - list_3_length
        while z >= list_3_length:
            z = z - list_3_length
        print(BIBLE_DIRECTORY+list_3[z])
        z = x - 1 - list_4_length
        while z >= list_4_length:
            z = z - list_4_length
        print(BIBLE_DIRECTORY+list_4[z])
        z = x - 1 - list_5_length
        while z >= list_5_length:
            z = z - list_5_length
        print(BIBLE_DIRECTORY+list_5[z])
        z = x - 1 - list_6_length
        while z >= list_6_length:
            z = z - list_6_length
        print(BIBLE_DIRECTORY+list_6[z])
        z = x - 1 - list_7_length
        while z >= list_7_length:
            z = z - list_7_length
        print(BIBLE_DIRECTORY+list_7[z])
        z = x - 1 - list_8_length
        while z >= list_8_length:
            z = z - list_8_length
        print(BIBLE_DIRECTORY+list_8[z])
        z = x - 1 - list_9_length
        while z >= list_9_length:
            z = z - list_9_length
        print(BIBLE_DIRECTORY+list_9[z])
        z = x - 1 - list_10_length
        while z >= list_10_length:
            z = z - list_10_length
        print(BIBLE_DIRECTORY+list_10[z])
        SUCCESS_MSG

sys.stdout.close()

# -----Now we copy the files into a new folder (new feature; since ver 0.2)-----#
out_dir = "day"+str(x).zfill(3)

if not os.path.exists(out_dir):
    os.makedirs(out_dir)

playlist_file = open(r"day"+str(x).zfill(3)+".m3u", "r")

for i in playlist_file.readlines():
    if i.startswith(BIBLE_DIRECTORY):
        tmp = list(i.strip())
        copy("".join(tmp),out_dir)

playlist_file.close()

sys.stderr.write("\nCopying of the Bible Chapters into the "+out_dir+" directory was successful.\n")

# -----We now change the ID3 tag information (track number) [new feature; since ver 0.3]-----#
# -----We also rename the files in the destination directory [new feature; since ver 0.3]-----#
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

sys.stderr.write(f"{Fore.CYAN}\nID3 tag info for the files in this directory has been updated.\n")
sys.stderr.write(f"\nThe files have been renamed in a sequential order.\n\n-----Soli Deo Gloria-----\n{Style.RESET_ALL}")

# ------------------------------------End------------------------------------#
## test to see whether we are getting the correct data from the text files!
## k = 1
## for count in range(0,10):
##     print "\nNow printing list_"+str(k)+": \n"
##     exec "print(BIBLE_DIRECTORY+list_%d," % k
##     print "\n--------------------------------------------------------------------\n"
##     k+=1
