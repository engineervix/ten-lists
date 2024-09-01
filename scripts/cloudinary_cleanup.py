"""cloudinary_cleanup.py

This script uses the Cloudinary API to rename files uploaded to Cloudinary.
When files are uploaded to Cloudinary, a random duffix is added by default
to avoid duplicates. This script removes that suffix, and works as follows:

1. get file data from cloudinary, save it as a JSON file
2. read the json file, extract the _public_ids_ into a list
3. loop through this list and run `rename_cloudinary_file`

There should be a `.env` file in the root of the project,
with the CLOUDINARY_URL environment variable defined as follows

`CLOUDINARY_URL=cloudinary://<api_key>:<api_secret>@<cloud_name>`
"""

import glob
import json
import os
from itertools import dropwhile

from dotenv import load_dotenv

load_dotenv()

import cloudinary  # noqa: E402
import cloudinary.api  # noqa: E402
import cloudinary.uploader  # noqa: E402

# Set configuration parameter: return "https" URLs by setting secure=True
# =======================================================================
config = cloudinary.config(secure=True)

bible_data = [
    ("Genesis", 50),
    ("Exodus", 40),
    ("Leviticus", 27),
    ("Numbers", 36),
    ("Deuteronomy", 34),
    ("Joshua", 24),
    ("Judges", 21),
    ("Ruth", 4),
    ("1 Samuel", 31),
    ("2 Samuel", 24),
    ("1 Kings", 22),
    ("2 Kings", 25),
    ("1 Chronicles", 29),
    ("2 Chronicles", 36),
    ("Ezra", 10),
    ("Nehemiah", 13),
    ("Esther", 10),
    ("Job", 42),
    ("Psalms", 150),
    ("Proverbs", 31),
    ("Ecclesiastes", 12),
    ("Song of Songs", 8),
    ("Isaiah", 66),
    ("Jeremiah", 52),
    ("Lamentations", 5),
    ("Ezekiel", 48),
    ("Daniel", 12),
    ("Hosea", 14),
    ("Joel", 3),
    ("Amos", 9),
    ("Obadiah", 1),
    ("Jonah", 4),
    ("Micah", 7),
    ("Nahum", 3),
    ("Habakkuk ", 3),
    ("Zephaniah", 3),
    ("Haggai", 2),
    ("Zechariah", 14),
    ("Malachi", 4),
    ("Matthew", 28),
    ("Mark", 16),
    ("Luke", 24),
    ("John", 21),
    ("Acts", 28),
    ("Romans", 16),
    ("1 Corinthians", 16),
    ("2 Corinthians", 13),
    ("Galatians", 6),
    ("Ephesians", 6),
    ("Philippians", 4),
    ("Colossians", 4),
    ("1 Thess", 5),
    ("2 Thess", 3),
    ("1 Timothy", 6),
    ("2 Timothy", 4),
    ("Titus", 3),
    ("Philemon", 1),
    ("Hebrews", 13),
    ("James", 5),
    ("1 Peter", 5),
    ("2 Peter", 3),
    ("1 John", 5),
    ("2 John", 1),
    ("3 John", 1),
    ("Jude", 1),
    ("Revelation", 22),
]

scripts_dir = os.path.join(os.getcwd(), "scripts")

for count, (book, chapters) in enumerate(bible_data, start=1):
    zcount = str(count).zfill(2)
    output = os.path.join(scripts_dir, f"{zcount}_{book}.json")
    print(f"connecting to Cloudinary to retrieve data for {book}")
    file_info = cloudinary.Search().expression(book.replace(" ", "")).max_results(chapters).execute()
    with open(output, "a", encoding="utf-8") as f:
        f.write(json.dumps(file_info, sort_keys=False, indent=2 * " ", ensure_ascii=False))

cloudinary_search_results = []

json_files = glob.glob(os.path.join(scripts_dir, "*.json"))

for fname in sorted(json_files):
    with open(fname) as json_file:
        data = json.load(json_file)
        resources = data.get("resources")
        public_ids = [chapter.get("public_id") for chapter in resources]
        cloudinary_search_results += public_ids


def rename_cloudinary_file(public_id: str):
    """
    trim off the random chars that Cloudinary adds as suffix to uploaded files

    if `public_id` is `ESV_dramatized/A01___50_Genesis_____ENGESVC2DA_euw8ec`, then
    what we want as a result is `ESV_dramatized/A01___50_Genesis_____ENGESVC2DA`
    """
    from_public_id = public_id
    # first, we reverse the `public id`
    reversed_public_id = from_public_id[::-1]
    # we start deleting from the first char and *stop* at the first underscore
    stop = "_"
    # use itertools.takewhile to perform the deletion, stopping at the first underscore
    reversed_public_id_no_suffix = "".join(dropwhile(lambda x: x not in stop, reversed_public_id))
    # reverse the result again
    public_id_no_suffix = reversed_public_id_no_suffix[::-1]
    # remove the last underscore
    to_public_id = public_id_no_suffix[:-1]
    print(f"connecting to Cloudinary to rename {from_public_id}")
    cloudinary.uploader.rename(from_public_id, to_public_id, resource_type="video")


for chapter in cloudinary_search_results:
    rename_cloudinary_file(chapter)
