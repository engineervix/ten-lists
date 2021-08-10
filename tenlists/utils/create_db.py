#!/usr/bin/env python3

"""
This python script creates an SQLite Database from 10 text files.
Each text file represents a separate list.
"""

import glob
import os
import sqlite3

CONN = sqlite3.connect("ten_lists.db")

C = CONN.cursor()

# Create tables
for i in range(1, 11):
    C.execute(
        f"""CREATE TABLE "list_{str(i).zfill(2)}" (
        "id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        "mp3_file"	TEXT NOT NULL
        )"""
    )

# Create the 10 lists from the text files in ./data/
THE_TEN_LISTS = []

LIST_DIR = os.path.join(os.getcwd(), "data")
FILELIST = glob.glob(os.path.join(LIST_DIR, "*.txt"))

for fname in sorted(FILELIST):
    with open(fname) as fn:
        THE_TEN_LISTS.append(fn.read().splitlines())

for _list in THE_TEN_LISTS:
    idx = THE_TEN_LISTS.index(_list) + 1
    for item in _list:
        C.execute(
            f"""INSERT INTO "list_{str(idx).zfill(2)}" ("id", "mp3_file")
          VALUES ({_list.index(item) + 1}, "{item}")"""
        )

CONN.commit()
CONN.close()
