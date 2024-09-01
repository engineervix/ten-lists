#!/usr/bin/env python3

"""
This script builds up on the initial `create_json.py` script by
adding appropriate metadata for each mp3 file.

The metadata is retrieved from files in the cloud using ffprobe.
This isn't the best approach, as it takes quite long
(~10min on an 8217.09 Mbps connection). Nonetheless, it's a
good way to test that you can access your files in the cloud
without any issues.

Notwithstanding, it's probably better to have the files locally then
get the metadata using eyeD3.
"""

import glob
import json
import os
import subprocess


def get_audio_metadata(id: int, url: str):
    """
    Use ffprobe to retrieve audio metadata from a url
    """
    result = subprocess.run(
        ["ffprobe", "-v", "quiet", "-print_format", "json", "-show_format", url],
        stdout=subprocess.PIPE,
    )

    if result.stderr:
        raise subprocess.CalledProcessError(returncode=result.returncode, cmd=result.args, stderr=result.stderr)

    if result.stdout:
        output = result.stdout.decode("utf-8")
        data = json.loads(output)

        return {
            "id": str(id),
            "mp3_file": url,
            "title": data.get("format").get("tags").get("title"),
            "artist": data.get("format").get("tags").get("artist"),
            "album": data.get("format").get("tags").get("album"),
            "duration": float(data.get("format").get("duration")),
        }

    print("=======================================================")
    print(f"something went horribly wrong while processing {url}")
    return {}


TENLISTS_MP3_CLOUD_STORAGE_BASE_URL = os.getenv("TENLISTS_MP3_CLOUD_STORAGE_BASE_URL")

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
        print(f"Now processing No. {str(_id)}: {item} ...")
        url = f"{TENLISTS_MP3_CLOUD_STORAGE_BASE_URL}/{item}"
        _temp_list.append(get_audio_metadata(_id, url))

    list_prefix = f"list_{str(idx).zfill(2)}"
    NEW_LIST_OF_TENS.append({list_prefix: _temp_list})

with open("ten_lists.json", "a", encoding="utf-8") as f:
    f.write(json.dumps(NEW_LIST_OF_TENS, sort_keys=False, indent=2 * " ", ensure_ascii=False))
