Bible-Playlist-Generator
========================

This python script generates an m3u playlist of 10 Bible Chapters (represented by 10 mp3 files) to be listened to on any given day _x_, according to [**Professor Grant Horner's Bible-Reading System**](http://www.thevinefellowship.com/10Lists.pdf). The audio Bible is as downloaded from the [_Faith Comes by Hearing®_ website](http://www.bible.is/audiodownloader).

The script also copies the files on the playlist into a new folder
so that you can carry the folder on your USB or any other device and listen anywhere (car, home theatre, phone, tablet, etc).

###Usage

From the commandline, 

```
python scripture_playlist_gen.py x
```

where *x* is an integer that represents the day on the Bible-Reading System, as in day 1, day 2, ... day 365, etc. For example, if you want the playlist for day *37*;

```
python scripture_playlist_gen.py 37
```

###Prerequisites / Assumptions

* Python must be installed on your computer and [added to the PATH](http://superuser.com/questions/143119/how-to-add-python-to-the-windows-path) (the script has been tested on a Windows Computer running Python 2.7).

* The script requires the following files to be in the same directory as the script itself:
  * list1.txt
  * list2.txt
  * list3.txt
  * list4.txt
  * list5.txt
  * list6.txt
  * list7.txt
  * list8.txt
  * list9.txt
  * list10.txt

These text files contain the Bible Chapters in the lists from Professor Grant Horner's Bible-Reading System.

* In addition to the above, it is assumed that the Bible folder is also on the same path as the python script and the above files. If you require a different setup, you can can customize this by editing line 80 in the script. Line 80 is as follows:

```python
BIBLE_DIRECTORY = "ENGESVC2DA\\" # Change this to suit your directory.
```

However, changing this will also affect the copying of files on into a new folder, so you would have to edit line 401;

```python
        tmp[10] = '/' #On Windows, comment out if used on a UNIX system
```

###Important Notes

* This script will only be useful to you if you use Professor Grant Horner's Bible-Reading System as the basis for your Bible Reading Plan.
* The Audio Bible version used is the 2001 ESV dramatized Bible (complete), as freely downloaded from http://www.bible.is/audiodownloader. (The size is over 2Gb)
