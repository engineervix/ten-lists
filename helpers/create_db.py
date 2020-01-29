#!/usr/bin/env python3

"""
This python script creates an SQLite Database from 10 text files.
Each text file represents a separate list.
"""

import os
import glob
import sqlite3

conn = sqlite3.connect("ten_lists.db")

c = conn.cursor()

# Create tables
for i in range(1, 11):
    c.execute(
        f"""CREATE TABLE "list_{str(i).zfill(2)}" (
        "id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        "mp3_file"	TEXT NOT NULL
        )"""
    )

# Create the 10 lists from the text files in ./data/
the_ten_lists = []

list_dir = os.path.join(os.getcwd(), "data")
filelist = glob.glob(os.path.join(list_dir, "*.txt"))

for fname in sorted(filelist):
    with open(fname) as fn:
        the_ten_lists.append(fn.read().splitlines())

for _list in the_ten_lists:
    idx = the_ten_lists.index(_list) + 1
    for item in _list:
        c.execute(
            f"""INSERT INTO "list_{str(idx).zfill(2)}" ("id", "mp3_file")
          VALUES ({_list.index(item) + 1}, "{item}")"""
        )

conn.commit()
conn.close()
