#!/bin/bash

############################################################################
# @author Victor Miti <victormiti@umusebo.com>
# @date 2015-Feb-09

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
############################################################################

#This script creates playlists for one week. I created it because I
#wanted to make my playlists in advance and copy the files to my other
#devices and external media only once. Also, I only get to run one
#command and I have as many playlists as I want!

#All you need to do is specify the start day as an argument to the script!
#If you want playlists for a period longer than seven days,
#modify the $END variable accordingly.

start_time=`date +%s`

#Firt let's remove any existing m3u files
printf "\n \nFirst we shall remove any existing m3u files...\n"
rm -v *.m3u


START=$1	#the 1st argument
END=`expr $START + 6`

for (( d=$START; d<=$END; d++ ))
	do python Scripture.py $d;
done

a=0
printf "\n \nRenaming the m3u files...\n"

#For this to work as expected, there shouldn't be any existing m3u files
#other than those created in the operation above
for f in *.m3u;
	do mv -v "$f" "${f%.m3u}_$(date -d "$a days" +"%Y-%b-%d-%a").m3u";
	let a=a+1;
done

b=0
printf "\n \nNow renaming the directories...\n"
#For this to work as expected, there shouldn't be any existing directories
#with a 'day' prefix other than those created in the operation above
for x in `ls | grep day`; do
	if [ -d "$x" ]; then
		mv -v "$x" "${x}_$(date -d "$b days" +"%Y-%b-%d-%a")"
		let b=b+1;
	fi
done

# Now let's move the folders into the "_playlists.current" folder

CURRENT_PLAYLISTS='./_playlists.current'

# (1) First check to see if it exists or not, and (2) whether or not it's empty
if [ ! -d "$CURRENT_PLAYLISTS" ]; then
	printf "\n \nCreating the '$CURRENT_PLAYLISTS' directory"
	mkdir $CURRENT_PLAYLISTS
elif [ "$(ls -A $CURRENT_PLAYLISTS)" ]; then
	printf "\n \nThe '$CURRENT_PLAYLISTS' directory isn't empty, Now deleting existing content ...\n\n"
	rm -rfv $CURRENT_PLAYLISTS/*
fi

printf "\n \nNow moving directories into the '$CURRENT_PLAYLISTS' directory\n"
for dir in `ls | grep day`; do
	if [ -d "$dir" ]; then
		mv -v "$dir" $CURRENT_PLAYLISTS
	fi
done


printf "\n \nProcess completed in $(expr `date +%s` - $start_time) seconds!"
printf "\n-----Soli Deo Gloria-----\n"
