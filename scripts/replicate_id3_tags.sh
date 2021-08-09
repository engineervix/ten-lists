#!/usr/bin/env bash

# This script is used to replicate ID3 tags from actual Bible MP3 files to the test files used in this project
# USAGE: Place it at the project root and run it.
# The assumption is that the 2GB+ directory containing the ESV Bible is at the following location:
# ~/Music/BIBLE.ESV/ENGESVC2DA/
# Uses https://github.com/KraYmer/replica

for mp3 in ~/Music/BIBLE.ESV/ENGESVC2DA/*.mp3;
  do replica ~/Music/BIBLE.ESV/ENGESVC2DA/"${mp3}" ENGESVC2DA/"${mp3}";
done
