#!/usr/bin/env python3

"""
This python script creates a JSON file from 10 text files.
Each text file represents a separate list.
"""

import glob
import io
import json
import os

# Create the 10 lists from the text files in ./data/
THE_TEN_LISTS = []

LIST_DIR = os.path.join(os.getcwd(), "data")
FILELIST = glob.glob(os.path.join(LIST_DIR, "*.txt"))

for fname in sorted(FILELIST):
    with open(fname) as fn:
        THE_TEN_LISTS.append(fn.read().splitlines())

NEW_LIST_OF_TENS = []

# we are converting each item in the lists to a dict
for idx, _list in enumerate(THE_TEN_LISTS, start=1):
    idx = THE_TEN_LISTS.index(_list) + 1
    _temp_list = []  # this will be a list of dicts
    for _id, item in enumerate(_list, start=1):
        _temp_list.append({"id": str(_id), "mp3_file": item})

    list_prefix = f"list_{str(idx).zfill(2)}"
    NEW_LIST_OF_TENS.append({list_prefix: _temp_list})

with io.open("ten_lists_slim.json", "a", encoding="utf-8") as f:
    f.write(json.dumps(NEW_LIST_OF_TENS, sort_keys=False, indent=2 * " ", ensure_ascii=False))
