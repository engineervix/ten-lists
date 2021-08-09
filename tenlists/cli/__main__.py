#!/usr/bin/env python3

"""
This python script generates an m3u playlist of 10 Bible Chapters
(represented by 10 mp3 files) to be listened to on any given day x,
according to Professor Grant Horner's Bible-Reading System
(http://www.thevinefellowship.com/10Lists.pdf)
The audio Bible is the `ESV version <https://www.esv.org/>`_ available on
the `Faith Comes by Hearing® website <http://www.bible.is/audiodownloader>`_
"""

import os
import json
import traceback
from shutil import copy
from pathlib import Path
from typing import List
import eyed3
import click
from pyfiglet import figlet_format

try:
    import colorama

    colorama.init()
except ImportError:
    colorama = None

try:
    from termcolor import colored
except ImportError:
    colored = None


def log(string, color, font="mini", figlet=False):
    """
    prints content to stdout
    other cool figlet font options: font='doom', font='mini'
    """
    if colored:
        if not figlet:
            print(colored(string, color))
        else:
            print(colored(figlet_format(string, font=font), color))
    else:
        print(string)


def log_traceback(ex):
    """Logs Errors"""
    tb_lines = traceback.format_exception(ex.__class__, ex, ex.__traceback__)
    tb_text = "".join(tb_lines)
    log(tb_text, "red")


def iterate_lists(collection: List[List], day: int) -> List:
    """
    iterates through the given ``collection``, which is
    a list of lists, and tries to get a particular item
    from each list, based on the given ``day``
    """
    result: List = []
    for lst in collection:
        idx = day - 1
        if idx < len(lst):
            item = lst[idx]
            result.append(item)
        else:
            while idx >= len(lst):
                idx -= len(lst)
            item = lst[idx]
            result.append(item)

    return result


def ten_lists():
    """create the 10 lists from the ten_lists.json file"""
    the_ten_lists = []
    this_file = Path(__file__)
    root_module = this_file.parents[1]
    data_dir = root_module / "data"
    json_file = os.path.join(data_dir, "ten_lists.json")

    with open(json_file, "r") as read_file:
        data = json.load(read_file)

    for idx, _list in enumerate(data, start=1):
        list_of_dicts = _list[f"list_{str(idx).zfill(2)}"]
        mp3_files_list = [item["mp3_file"] for item in list_of_dicts]
        the_ten_lists.append(mp3_files_list)

    return the_ten_lists


def reading_list(day: int, bible_dir: str) -> List:
    """
    The generated reading (or listening) list for the given day.
    bible_dir is the directory containing the mp3 files.
    """

    listening_list = []

    # append trailing slash to bible_dir
    bible_dir += "/"

    for chapter in iterate_lists(ten_lists(), day):
        listening_list.append(bible_dir + chapter)

    return listening_list


def create_m3u(day, bible_dir):
    """creates an m3u playlist based on specified day's listening list"""
    m3u_filename = "day" + str(day).zfill(3) + ".m3u"
    # check if file exists, and if it does, os.remove()
    try:
        os.remove(m3u_filename)
    except OSError:
        pass
    try:
        with open(m3u_filename, "a") as m3u:
            m3u.write("#EXTM3U\n")
            m3u.write("\n".join(reading_list(day, bible_dir)))
    except EnvironmentError as ex:
        log(
            "✗ Oops! Something went wrong while attempting to " + "create a playlist.",
            "red",
        )
        log_traceback(ex)
    else:
        success_msg = f"✓ playlist for day {str(day)} successfully created."
        log(success_msg, "green")


def create_mp3_dir(day, bible_dir):
    """Copies the generated mp3 files into separate directory"""
    # Now we copy the files into a new folder
    out_dir = "day" + str(day).zfill(3)

    try:
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)

        for i in reading_list(day, bible_dir):
            tmp = list(i.strip())
            copy("".join(tmp), out_dir)
        log(
            "✓ Copying of the Bible Chapters into the "
            + out_dir
            + " directory was successful.",
            "green",
        )
    except EnvironmentError as ex:
        log("✗ Oops! Something went wrong while attempting to copy files", "red")
        log_traceback(ex)

    # We now change the ID3 tag information (track number)
    # We also rename the files in the destination directory
    track_number = 1

    try:
        for i in reading_list(day, bible_dir):
            tmp = list(i.strip().replace(bible_dir, out_dir + "/", 1))
            _f = "".join(tmp)
            audiofile = eyed3.load(_f)
            audiofile.tag.track_num = track_number
            audiofile.tag.save()
            filename = _f.replace(out_dir + "/", "")
            # add a filename prefix with leading zeroes
            f_new = out_dir + "/" + str(track_number).zfill(3) + filename[4:]
            os.rename(_f, f_new)
            track_number += 1
        log(
            "✓ ID3 tag info for the generated files in this "
            "directory has been updated.",
            "green",
        )
        log("✓ The files have been renamed in a sequential order.", "green")
        log("\n-----Soli Deo Gloria-----\n", "cyan")
    except EnvironmentError as ex:
        log("Oops! Something went wrong while processing the mp3 files", "red")
        log_traceback(ex)


@click.command()
@click.option(
    "--day",
    "-d",
    required=True,
    type=click.IntRange(1),
    prompt="Please enter the day of the reading plan, as in, " + "eg. day 1, or day 32",
    help="the day of the reading plan, as in, eg. day 1, or day 32",
)
@click.option(
    "--folder",
    "-f",
    default="ENGESVC2DA",
    show_default=True,
    help="the folder containing the Bible mp3 files",
)
def cmd(day, folder):
    """
    Bible Playlist Generator » generates a playlist of 10 Bible Chapters
    for the given day
    """

    log("Bible Playlist Generator", color="magenta", figlet=True)
    log("Welcome to the Bible Playlist Generator", "cyan")
    click.secho(f"\nCreating a playlist for day {str(day)} ...", fg="white")

    create_m3u(day, folder)
    create_mp3_dir(day, folder)


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    cmd()
