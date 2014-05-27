#!/usr/bin/python
# -- coding: utf-8 --

'''
    Scripture Playlist Generator.
    Copyright (C) 2014  Victor Miti

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


import sys, os
from shutil import copy

__doc__ = "This script generates an m3u playlist of 10 Bible Chapters for day x of Bible plan."
__author__ = "Victor Miti <victormiti@umusebo.com>"
__date__ = "May 27 2014"
__version__ = "0.1"

'''-----------------------------Description--------------------------------
This python script generates an m3u playlist of 10 Bible Chapters
(represented by 10 mp3 files) to be listened to on any given day x,
according to Professor Grant Horner's Bible-Reading System
(http://www.thevinefellowship.com/10Lists.pdf)
The audio Bible is as downloaded from the <Faith Comes by Hearing®> website
(http://www.bible.is/audiodownloader)

Has been tested on Python 2.7.

------------------------------------------------------------------------'''

'''------------------------------Changelog---------------------------------
To Do:
Add a feauture to send the playlist to (a) specified email address(es), or 
publish it to your weblog or something, so that you are always reminded
to get into God's word!

version 0.1:
Initial version. Includes the ability to copy the files on the playlist 
file into a new folder so that you can copy the folder  to your USB or 
any other device and thus be able to listen anywhere (car, home theatre, 
mobile phone, tablet, etc).
------------------------------------------------------------------------'''


def _usage():
    """ print the usage message """
    msg = __doc__ + "\n"
    msg += "Usage:  scripture_playlist_gen.py [Option]\n"
    msg += "Option:\n"
    msg += "\n%5s,\t%s\t\%s\n\n" % ("x", "an integer", "enter the day of the reading plan, eg 6 for day 6")

    print msg

if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.stderr.write("The day of the reading plan hasn't been given.\n")
        _usage()
        sys.exit(1)

# x represents the day, as in day x...
#...This will be passed from the commandline as an argument variable
script, x = sys.argv
x = int(x)

#first let us create the 10 lists from the text files
for count in range(1,11):
    exec "list_%d = %s" % (count, open("list"+str(count)+".txt").read().splitlines())
    exec "list_%d_length = len(list_%d)" % (count, count)

#-----------------Now we create a new list(our reading list)-----------------#

BIBLE_DIRECTORY = "ENGESVC2DA\\" # Change this to suit your directory.

#redirect stdout to an .m3u file in the same directory
sys.stdout = open("day"+str(x)+".m3u", "w")

SUCCESS_MSG = sys.stderr.write("The playlist for day "+str(x)+" has been created successfully.\n")

try:
    z = x - 1   #for indexing purposes. Remember that the first index is represented by zero!
    exec "reading_list_%d = %s" % (x, ','.join("list_"+str(j)+"["+str(z)+"]" for j in range(1,11)))
    print "#EXTM3U"
    exec "my_reading_list = reading_list_%d" % x
    for item in my_reading_list:
        print BIBLE_DIRECTORY+item
    SUCCESS_MSG

except IndexError:
    if list_7_length >= x > list_10_length:
        exec "reading_list_%d = %s" % (x, ','.join("list_"+str(j)+"["+str(z)+"]" for j in range(1,10)))
        print "#EXTM3U"
        exec "my_reading_list = reading_list_%d" % x
        for item in my_reading_list:
            print BIBLE_DIRECTORY+item
        z = x - 1 - list_10_length
        print BIBLE_DIRECTORY+list_10[z]
        SUCCESS_MSG

    if list_5_length >= x > list_7_length:
        exec "reading_list_%d = %s" % (x, ','.join("list_"+str(j)+"["+str(z)+"]" for j in range(1,7)))
        print "#EXTM3U"
        exec "my_reading_list = reading_list_%d" % x
        for item in my_reading_list:
            print BIBLE_DIRECTORY+item
        z = x - 1 - list_7_length
        print BIBLE_DIRECTORY+list_7[z]
        print BIBLE_DIRECTORY+list_8[x-1]
        print BIBLE_DIRECTORY+list_9[x-1]
        z = x - 1 - list_10_length
        while z >= list_10_length:
            z = z - list_10_length
        print BIBLE_DIRECTORY+list_10[z]
        SUCCESS_MSG

    if list_4_length >= x > list_5_length:
        exec "reading_list_%d = %s" % (x, ','.join("list_"+str(j)+"["+str(z)+"]" for j in range(1,5)))
        print "#EXTM3U"
        exec "my_reading_list = reading_list_%d" % x
        for item in my_reading_list:
            print BIBLE_DIRECTORY+item
        z = x - 1 - list_5_length
        print BIBLE_DIRECTORY+list_5[z]
        print BIBLE_DIRECTORY+list_6[x-1]
        z = x - 1 - list_7_length
        while z >= list_7_length:
            z = z - list_7_length
        print BIBLE_DIRECTORY+list_7[z]
        print BIBLE_DIRECTORY+list_8[x-1]
        print BIBLE_DIRECTORY+list_9[x-1]
        z = x - 1 - list_10_length
        while z >= list_10_length:
            z = z - list_10_length
        print BIBLE_DIRECTORY+list_10[z]
        SUCCESS_MSG

    if list_3_length >= x > list_4_length:
        exec "reading_list_%d = %s" % (x, ','.join("list_"+str(j)+"["+str(z)+"]" for j in range(1,4)))
        print "#EXTM3U"
        exec "my_reading_list = reading_list_%d" % x
        for item in my_reading_list:
            print BIBLE_DIRECTORY+item
        z = x - 1 - list_4_length
        print BIBLE_DIRECTORY+list_4[z]
        z = x - 1 - list_5_length
        while z >= list_5_length:
            z = z - list_5_length
        print BIBLE_DIRECTORY+list_5[z]
        print BIBLE_DIRECTORY+list_6[x-1]
        z = x - 1 - list_7_length
        while z >= list_7_length:
            z = z - list_7_length
        print BIBLE_DIRECTORY+list_7[z]
        print BIBLE_DIRECTORY+list_8[x-1]
        print BIBLE_DIRECTORY+list_9[x-1]
        z = x - 1 - list_10_length
        while z >= list_10_length:
            z = z - list_10_length
        print BIBLE_DIRECTORY+list_10[z]
        SUCCESS_MSG

    if list_1_length >= x > list_3_length:
        exec "reading_list_%d = %s" % (x, ','.join("list_"+str(j)+"["+str(z)+"]" for j in range(1,3)))
        print "#EXTM3U"
        exec "my_reading_list = reading_list_%d" % x
        for item in my_reading_list:
            print BIBLE_DIRECTORY+item
        z = x - 1 - list_3_length
        print BIBLE_DIRECTORY+list_3[z]
        z = x - 1 - list_4_length
        while z >= list_4_length:
            z = z - list_4_length
        print BIBLE_DIRECTORY+list_4[z]
        z = x - 1 - list_5_length
        while z >= list_5_length:
            z = z - list_5_length
        print BIBLE_DIRECTORY+list_5[z]
        print BIBLE_DIRECTORY+list_6[x-1]
        z = x - 1 - list_7_length
        while z >= list_7_length:
            z = z - list_7_length
        print BIBLE_DIRECTORY+list_7[z]
        print BIBLE_DIRECTORY+list_8[x-1]
        print BIBLE_DIRECTORY+list_9[x-1]
        z = x - 1 - list_10_length
        while z >= list_10_length:
            z = z - list_10_length
        print BIBLE_DIRECTORY+list_10[z]
        SUCCESS_MSG

    if list_6_length >= x > list_1_length:
        print "#EXTM3U"
        z = x - 1 - list_1_length
        while z >= list_1_length:
            z = z - list_1_length
        print BIBLE_DIRECTORY+list_1[z]
        print BIBLE_DIRECTORY+list_2[x-1]
        z = x - 1 - list_3_length
        while z >= list_3_length:
            z = z - list_3_length
        print BIBLE_DIRECTORY+list_3[z]
        z = x - 1 - list_4_length
        while z >= list_4_length:
            z = z - list_4_length
        print BIBLE_DIRECTORY+list_4[z]
        z = x - 1 - list_5_length
        while z >= list_5_length:
            z = z - list_5_length
        print BIBLE_DIRECTORY+list_5[z]
        print BIBLE_DIRECTORY+list_6[x-1]
        z = x - 1 - list_7_length
        while z >= list_7_length:
            z = z - list_7_length
        print BIBLE_DIRECTORY+list_7[z]
        print BIBLE_DIRECTORY+list_8[x-1]
        print BIBLE_DIRECTORY+list_9[x-1]
        z = x - 1 - list_10_length
        while z >= list_10_length:
            z = z - list_10_length
        print BIBLE_DIRECTORY+list_10[z]
        SUCCESS_MSG

    if list_2_length >= x > list_6_length:
        print "#EXTM3U"
        z = x - 1 - list_1_length
        while z >= list_1_length:
            z = z - list_1_length
        print BIBLE_DIRECTORY+list_1[z]
        print BIBLE_DIRECTORY+list_2[x-1]
        z = x - 1 - list_3_length
        while z >= list_3_length:
            z = z - list_3_length
        print BIBLE_DIRECTORY+list_3[z]
        z = x - 1 - list_4_length
        while z >= list_4_length:
            z = z - list_4_length
        print BIBLE_DIRECTORY+list_4[z]
        z = x - 1 - list_5_length
        while z >= list_5_length:
            z = z - list_5_length
        print BIBLE_DIRECTORY+list_5[z]
        z = x - 1 - list_6_length
        while z >= list_6_length:
            z = z - list_6_length
        print BIBLE_DIRECTORY+list_6[z]
        z = x - 1 - list_7_length
        while z >= list_7_length:
            z = z - list_7_length
        print BIBLE_DIRECTORY+list_7[z]
        print BIBLE_DIRECTORY+list_8[x-1]
        print BIBLE_DIRECTORY+list_9[x-1]
        z = x - 1 - list_10_length
        while z >= list_10_length:
            z = z - list_10_length
        print BIBLE_DIRECTORY+list_10[z]
        SUCCESS_MSG

    if list_8_length >= x > list_2_length:
        print "#EXTM3U"
        z = x - 1 - list_1_length
        while z >= list_1_length:
            z = z - list_1_length
        print BIBLE_DIRECTORY+list_1[z]
        z = x - 1 - list_2_length
        while z >= list_2_length:
            z = z - list_2_length
        print BIBLE_DIRECTORY+list_2[z]
        z = x - 1 - list_3_length
        while z >= list_3_length:
            z = z - list_3_length
        print BIBLE_DIRECTORY+list_3[z]
        z = x - 1 - list_4_length
        while z >= list_4_length:
            z = z - list_4_length
        print BIBLE_DIRECTORY+list_4[z]
        z = x - 1 - list_5_length
        while z >= list_5_length:
            z = z - list_5_length
        print BIBLE_DIRECTORY+list_5[z]
        z = x - 1 - list_6_length
        while z >= list_6_length:
            z = z - list_6_length
        print BIBLE_DIRECTORY+list_6[z]
        z = x - 1 - list_7_length
        while z >= list_7_length:
            z = z - list_7_length
        print BIBLE_DIRECTORY+list_7[z]
        print BIBLE_DIRECTORY+list_8[x-1]
        print BIBLE_DIRECTORY+list_9[x-1]
        z = x - 1 - list_10_length
        while z >= list_10_length:
            z = z - list_10_length
        print BIBLE_DIRECTORY+list_10[z]
        SUCCESS_MSG

    if list_9_length >= x > list_8_length:
        print "#EXTM3U"
        z = x - 1 - list_1_length
        while z >= list_1_length:
            z = z - list_1_length
        print BIBLE_DIRECTORY+list_1[z]
        z = x - 1 - list_2_length
        while z >= list_2_length:
            z = z - list_2_length
        print BIBLE_DIRECTORY+list_2[z]
        z = x - 1 - list_3_length
        while z >= list_3_length:
            z = z - list_3_length
        print BIBLE_DIRECTORY+list_3[z]
        z = x - 1 - list_4_length
        while z >= list_4_length:
            z = z - list_4_length
        print BIBLE_DIRECTORY+list_4[z]
        z = x - 1 - list_5_length
        while z >= list_5_length:
            z = z - list_5_length
        print BIBLE_DIRECTORY+list_5[z]
        z = x - 1 - list_6_length
        while z >= list_6_length:
            z = z - list_6_length
        print BIBLE_DIRECTORY+list_6[z]
        z = x - 1 - list_7_length
        while z >= list_7_length:
            z = z - list_7_length
        print BIBLE_DIRECTORY+list_7[z]
        z = x - 1 - list_8_length
        while z >= list_8_length:
            z = z - list_8_length
        print BIBLE_DIRECTORY+list_8[z]
        print BIBLE_DIRECTORY+list_9[x-1]
        z = x - 1 - list_10_length
        while z >= list_10_length:
            z = z - list_10_length
        print BIBLE_DIRECTORY+list_10[z]
        SUCCESS_MSG

    if x > list_9_length:
        print "#EXTM3U"
        z = x - 1 - list_1_length
        while z >= list_1_length:
            z = z - list_1_length
        print BIBLE_DIRECTORY+list_1[z]
        z = x - 1 - list_2_length
        while z >= list_2_length:
            z = z - list_2_length
        print BIBLE_DIRECTORY+list_2[z]
        z = x - 1 - list_3_length
        while z >= list_3_length:
            z = z - list_3_length
        print BIBLE_DIRECTORY+list_3[z]
        z = x - 1 - list_4_length
        while z >= list_4_length:
            z = z - list_4_length
        print BIBLE_DIRECTORY+list_4[z]
        z = x - 1 - list_5_length
        while z >= list_5_length:
            z = z - list_5_length
        print BIBLE_DIRECTORY+list_5[z]
        z = x - 1 - list_6_length
        while z >= list_6_length:
            z = z - list_6_length
        print BIBLE_DIRECTORY+list_6[z]
        z = x - 1 - list_7_length
        while z >= list_7_length:
            z = z - list_7_length
        print BIBLE_DIRECTORY+list_7[z]
        z = x - 1 - list_8_length
        while z >= list_8_length:
            z = z - list_8_length
        print BIBLE_DIRECTORY+list_8[z]
        z = x - 1 - list_9_length
        while z >= list_9_length:
            z = z - list_9_length
        print BIBLE_DIRECTORY+list_9[z]
        z = x - 1 - list_10_length
        while z >= list_10_length:
            z = z - list_10_length
        print BIBLE_DIRECTORY+list_10[z]
        SUCCESS_MSG

sys.stdout.close()

#----------------Now we copy the files into a new folder----------------#
out_dir = "day"+str(x)

if not os.path.exists(out_dir):
    os.makedirs(out_dir)

playlist_file = open(r"day"+str(x)+".m3u", "r")

for i in playlist_file.readlines():
    if i.startswith(BIBLE_DIRECTORY):
        tmp = list(i.strip())
        tmp[10] = '/' #On Windows, comment out if used on UNIX
        copy("".join(tmp),out_dir)

playlist_file.close()

sys.stderr.write("I have also copied the Bible Chapters into the "+out_dir+" folder.\nSoli Deo Gloria")

#------------------------------------End------------------------------------#
##test to see whether we are getting the correct data from the text files!
##k = 1
##for count in range(0,10):
##    print "\nNow printing list_"+str(k)+": \n"
##    exec "print BIBLE_DIRECTORY+list_%d," % k
##    print "\n--------------------------------------------------------------------\n"
##    k+=1
