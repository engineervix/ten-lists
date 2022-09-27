"""tests for the `bible_playlist_generator.py` script"""

import fnmatch
import glob
import os
from pathlib import Path

import eyed3
import pytest
from click.testing import CliRunner

from tenlists.cli.__main__ import (
    cmd,
    create_m3u,
    create_mp3_dir,
    reading_list,
    ten_lists,
)

from .conftest import (
    BASIC_CLI_IDS,
    BIBLE_DIR,
    M3U_CONTENT_IDS,
    M3U_IDS,
    MP3_DIR_COUNT,
    MP3_DIR_IDS,
    MP3S_EXIST_IDS,
    MP3S_FILENAMES_IDS,
    MP3S_ID3_TAGINFO,
    PLAYLIST_IDS,
    TEST_DATA,
)


def test_ten_lists():
    """`ten_lists()` should return a list"""
    assert isinstance(ten_lists(), list)  # nosec


def test_ten_lists_length():
    """`ten_lists()` should have a length of 10"""
    assert len(ten_lists()) == 10  # nosec


def test_ten_lists_chapters():
    """Check the number of chapters in the 10 lists."""
    num_of_chapters = [89, 187, 78, 65, 62, 150, 31, 249, 250, 28]

    for chapters, bible_list in zip(num_of_chapters, ten_lists()):
        assert len(bible_list) == chapters  # nosec


@pytest.mark.parametrize("day, listening_list", TEST_DATA, ids=PLAYLIST_IDS)
def test_reading_list(day, listening_list):
    """test generated reading lists using TEST_DATA"""
    assert reading_list(day, BIBLE_DIR) == listening_list  # nosec


@pytest.mark.usefixtures("prepare_data")
@pytest.mark.parametrize("day", [item[0] for item in TEST_DATA], ids=M3U_IDS)
def test_m3u_creation(day):
    """tests the creation of m3u playlist files"""
    create_m3u(day, BIBLE_DIR)
    m3u_filename = "day" + str(day).zfill(3) + ".m3u"
    assert os.path.exists(m3u_filename)  # nosec


@pytest.mark.usefixtures("prepare_data")
@pytest.mark.parametrize("day, listening_list", TEST_DATA, ids=M3U_CONTENT_IDS)
def test_m3u_content(day, listening_list):
    """checks the content of the generated m3u playlist files"""
    # create_m3u(day, BIBLE_DIR) m3u files already created since scope=session
    # and the m3u file creation function doesn't check if file exists
    m3u_filename = "day" + str(day).zfill(3) + ".m3u"
    listening_list.insert(0, "#EXTM3U")
    with open(m3u_filename, "r") as m3u:
        assert m3u.read().splitlines() == listening_list  # nosec


@pytest.mark.usefixtures("prepare_data")
@pytest.mark.parametrize("day", [item[0] for item in TEST_DATA], ids=MP3_DIR_IDS)
def test_mp3_dir_creation(day):
    """tests the creation of the directory containing mp3 files"""
    create_mp3_dir(day, BIBLE_DIR)
    output_dir = "day" + str(day).zfill(3)
    assert os.path.exists(output_dir)  # nosec


@pytest.mark.usefixtures("prepare_data")
@pytest.mark.parametrize("day", [item[0] for item in TEST_DATA], ids=MP3_DIR_COUNT)
def test_mp3_dir_count(day):
    """tests the presence of 10 files in the created directories"""
    # create_mp3_dir(day, BIBLE_DIR)  already created since scope=session
    output_dir = "day" + str(day).zfill(3)
    assert len(os.listdir(output_dir)) == 10  # nosec


@pytest.mark.usefixtures("prepare_data")
@pytest.mark.parametrize("day", [item[0] for item in TEST_DATA], ids=MP3S_EXIST_IDS)
def test_mp3_files_creation(day):
    """tests the presence of 10 mp3 files in the created directories"""
    # create_mp3_dir(day, BIBLE_DIR)  already created since scope=session
    output_dir = "day" + str(day).zfill(3)
    ext = "*.mp3"
    for entry in os.listdir(output_dir):
        assert fnmatch.fnmatch(entry, ext)  # nosec


@pytest.mark.usefixtures("prepare_data")
@pytest.mark.parametrize("day, listening_list", TEST_DATA, ids=MP3S_FILENAMES_IDS)
def test_mp3_filenames(day, listening_list):
    """checks the filenames of the 10 mp3 files in the created directories"""
    # create_mp3_dir(day, BIBLE_DIR)  already created since scope=session
    output_dir = "day" + str(day).zfill(3)
    filelist = glob.glob(os.path.join(output_dir, "*.mp3"))
    # Here we use pathlib.Path to remove the first folder in a path.
    # See https://stackoverflow.com/a/26724369
    mp3_filelist = [list(Path(mp3_file).parts[1:])[0] for mp3_file in filelist]
    # because of our fixture having session scope, the `listening_list` may
    # have been modified in a previous test by prepending it with "#EXTM3U"
    filenames = [mp3.strip().replace(f"{BIBLE_DIR}", f"{output_dir}/", 1) for mp3 in listening_list if mp3 != "#EXTM3U"]
    files = [item.replace(f"{output_dir}/", "") for item in filenames]
    mp3_files = [str(idx).zfill(3) + mp3[4:] for idx, mp3 in enumerate(files, start=1)]
    assert sorted(mp3_filelist) == mp3_files  # nosec


@pytest.mark.usefixtures("prepare_data")
@pytest.mark.parametrize("day", [item[0] for item in TEST_DATA], ids=MP3S_ID3_TAGINFO)
def test_mp3_id3_tags(day):
    """checks the ID3 tags on the 10 mp3 files in the created directories"""
    # create_mp3_dir(day, BIBLE_DIR)  already created since scope=session
    output_dir = "day" + str(day).zfill(3)
    filelist = glob.glob(os.path.join(output_dir, "*.mp3"))
    for index, entry in enumerate(sorted(filelist), start=1):
        audiofile = eyed3.load(entry)
        # audiofile.tag.track_num is a tuple in the form (1, None)
        assert audiofile.tag.track_num[0] == index  # nosec


@pytest.mark.usefixtures("prepare_data")
@pytest.mark.parametrize("day", [item[0] for item in TEST_DATA], ids=BASIC_CLI_IDS)
def test_cli(day):
    """
    Basic testing of the commandline interface

    TODO: - read https://realpython.com/python-cli-testing/
          - add more realistic tests.
    """
    runner = CliRunner()
    result = runner.invoke(cmd, ["-d", day])
    assert result.exit_code == 0  # nosec
    assert not result.exception  # nosec
