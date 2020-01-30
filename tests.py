"""tests for the `bible_playlist_generator.py` script"""

import os
from pathlib import Path
import fnmatch
import glob
import timeit
from shutil import copy, rmtree
import pytest
from click.testing import CliRunner
from gtts import gTTS
import eyed3
from tqdm import tqdm
from bible_playlist_generator import (
    ten_lists,
    reading_list,
    create_m3u,
    create_mp3_dir,
    cmd,
)

BIBLE_DIR = "_ENGESVC2DA"


@pytest.fixture(scope="session")
def prepare_data():
    """Prepare sample MP3 files for testing. Delete afterwards"""

    # Setup: Prepare MP3 files
    start = timeit.default_timer()

    bible_directory = os.path.join(os.getcwd(), BIBLE_DIR)

    if not os.path.exists(bible_directory):
        os.makedirs(bible_directory)

    # now we're gonna programmatically create an audio file

    tts = gTTS("audio", lang="en")
    audio_file = os.path.join(os.getcwd(), "audio_file.mp3")
    tts.save(audio_file)

    # add ID3 tag info to the file
    mp3_file = eyed3.load(audio_file)
    mp3_file.initTag()
    mp3_file.tag.artist = "test"
    mp3_file.tag.track_num = 1
    mp3_file.tag.save()

    # we then make multiple copies of the audio file

    for bible_list in tqdm(ten_lists()):
        for mp3 in bible_list:
            new_mp3_file = os.path.join(bible_directory, mp3)
            copy(audio_file, new_mp3_file)

    yield  # This is where the testing happens

    # Teardown : discard the data
    # Cleanup
    m3u_files = glob.glob(os.path.join(os.getcwd(), "*.m3u"))
    generated_mp3_dirs = glob.iglob(os.path.join(os.getcwd(), "day*"))
    try:
        os.remove(audio_file)
        rmtree(os.path.join(os.getcwd(), bible_directory))
        for m3u_file in m3u_files:
            os.remove(m3u_file)
        for path in generated_mp3_dirs:
            if os.path.isdir(path):
                rmtree(path)
    except OSError as ex:  # if failed, report it back to the user
        print("Error: %s - %s." % (ex.filename, ex.strerror))

    stop = timeit.default_timer()
    total_time = stop - start

    print(f"Total running time: {total_time} seconds")


TEST_DATA = [
    (
        1,
        [
            f"{BIBLE_DIR}/B01___01_Matthew_____ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A01___01_Genesis_____ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/B06___01_Romans______ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/B13___01_1Thess______ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A18___01_Job_________ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A19__001_Psalms______ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A20___01_Proverbs____ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A06___01_Joshua______ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A23___01_Isaiah______ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/B05___01_Acts________ENGESVC2DA.mp3",
        ],
    ),
    (
        17,
        [
            f"{BIBLE_DIR}/B01___17_Matthew_____ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A01___17_Genesis_____ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/B07___01_1CorinthiansENGESVC2DA.mp3",
            f"{BIBLE_DIR}/B16___03_2Timothy____ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A18___17_Job_________ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A19__017_Psalms______ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A20___17_Proverbs____ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A06___17_Joshua______ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A23___17_Isaiah______ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/B05___17_Acts________ENGESVC2DA.mp3",
        ],
    ),
    (
        29,
        [
            f"{BIBLE_DIR}/B02___01_Mark________ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A01___29_Genesis_____ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/B07___13_1CorinthiansENGESVC2DA.mp3",
            f"{BIBLE_DIR}/B21___02_1Peter______ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A18___29_Job_________ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A19__029_Psalms______ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A20___29_Proverbs____ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A07___05_Judges______ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A23___29_Isaiah______ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/B05___01_Acts________ENGESVC2DA.mp3",
        ],
    ),
    (
        45,
        [
            f"{BIBLE_DIR}/B03___01_Luke________ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A01___45_Genesis_____ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/B08___13_2CorinthiansENGESVC2DA.mp3",
            f"{BIBLE_DIR}/B27___02_Revelation__ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A21___03_EcclesiastesENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A19__045_Psalms______ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A20___14_Proverbs____ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A07___21_Judges______ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A23___45_Isaiah______ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/B05___17_Acts________ENGESVC2DA.mp3",
        ],
    ),
    (
        63,
        [
            f"{BIBLE_DIR}/B03___19_Luke________ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A02___13_Exodus______ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/B12___02_Colossians__ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/B27___20_Revelation__ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A18___01_Job_________ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A19__063_Psalms______ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A20___01_Proverbs____ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A09___14_1Samuel_____ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A23___63_Isaiah______ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/B05___07_Acts________ENGESVC2DA.mp3",
        ],
    ),
    (
        70,
        [
            f"{BIBLE_DIR}/B04___02_John________ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A02___20_Exodus______ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/B19___05_Hebrews_____ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/B13___05_1Thess______ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A18___08_Job_________ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A19__070_Psalms______ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A20___08_Proverbs____ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A09___21_1Samuel_____ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A24___04_Jeremiah____ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/B05___14_Acts________ENGESVC2DA.mp3",
        ],
    ),
    (
        86,
        [
            f"{BIBLE_DIR}/B04___18_John________ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A02___36_Exodus______ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/B06___08_Romans______ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/B17___03_Titus_______ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A18___24_Job_________ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A19__086_Psalms______ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A20___24_Proverbs____ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A10___06_2Samuel_____ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A24___20_Jeremiah____ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/B05___02_Acts________ENGESVC2DA.mp3",
        ],
    ),
    (
        99,
        [
            f"{BIBLE_DIR}/B01___10_Matthew_____ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A03___09_Leviticus___ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/B07___05_1CorinthiansENGESVC2DA.mp3",
            f"{BIBLE_DIR}/B22___02_2Peter______ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A18___37_Job_________ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A19__099_Psalms______ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A20___06_Proverbs____ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A10___19_2Samuel_____ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A24___33_Jeremiah____ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/B05___15_Acts________ENGESVC2DA.mp3",
        ],
    ),
    (
        123,
        [
            f"{BIBLE_DIR}/B02___06_Mark________ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A04___06_Numbers_____ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/B08___13_2CorinthiansENGESVC2DA.mp3",
            f"{BIBLE_DIR}/B27___15_Revelation__ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A22___07_SongofSongs_ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A19__123_Psalms______ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A20___30_Proverbs____ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A11___19_1Kings______ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A25___05_LamentationsENGESVC2DA.mp3",
            f"{BIBLE_DIR}/B05___11_Acts________ENGESVC2DA.mp3",
        ],
    ),
    (
        168,
        [
            f"{BIBLE_DIR}/B04___11_John________ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A05___15_Deuteronomy_ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/B06___12_Romans______ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/B23___03_1John_______ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A21___02_EcclesiastesENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A19__018_Psalms______ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A20___13_Proverbs____ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A13___17_1Chronicles_ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A26___45_Ezekiel_____ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/B05___28_Acts________ENGESVC2DA.mp3",
        ],
    ),
    (
        204,
        [
            f"{BIBLE_DIR}/B01___26_Matthew_____ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A01___17_Genesis_____ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/B09___03_Galatians___ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/B15___01_1Timothy____ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A18___18_Job_________ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A19__054_Psalms______ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A20___18_Proverbs____ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A14___24_2Chronicles_ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A30___04_Amos________ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/B05___08_Acts________ENGESVC2DA.mp3",
        ],
    ),
    (
        237,
        [
            f"{BIBLE_DIR}/B03___15_Luke________ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A01___50_Genesis_____ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/B06___03_Romans______ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/B25___01_3John_______ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A21___09_EcclesiastesENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A19__087_Psalms______ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A20___20_Proverbs____ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A16___11_Nehemiah____ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A38___05_Zechariah___ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/B05___13_Acts________ENGESVC2DA.mp3",
        ],
    ),
    (
        250,
        [
            f"{BIBLE_DIR}/B04___04_John________ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A02___13_Exodus______ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/B06___16_Romans______ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/B27___12_Revelation__ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A18___02_Job_________ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A19__100_Psalms______ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A20___02_Proverbs____ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A06___01_Joshua______ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A39___04_Malachi_____ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/B05___26_Acts________ENGESVC2DA.mp3",
        ],
    ),
    (
        365,
        [
            f"{BIBLE_DIR}/B01___09_Matthew_____ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A05___25_Deuteronomy_ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/B10___02_Ephesians___ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/B23___05_1John_______ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A22___01_SongofSongs_ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A19__065_Psalms______ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A20___24_Proverbs____ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A11___12_1Kings______ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A24___49_Jeremiah____ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/B05___01_Acts________ENGESVC2DA.mp3",
        ],
    ),
    (
        800,
        [
            f"{BIBLE_DIR}/B04___20_John________ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A02___02_Exodus______ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/B07___04_1CorinthiansENGESVC2DA.mp3",
            f"{BIBLE_DIR}/B17___02_Titus_______ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A22___02_SongofSongs_ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A19__050_Psalms______ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A20___25_Proverbs____ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A09___04_1Samuel_____ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/A23___50_Isaiah______ENGESVC2DA.mp3",
            f"{BIBLE_DIR}/B05___16_Acts________ENGESVC2DA.mp3",
        ],
    ),
]

PLAYLIST_IDS = [f"day_{str(data[0])}_playlist" for data in TEST_DATA]
M3U_IDS = [f"day_{str(data[0])}_m3u_file" for data in TEST_DATA]
M3U_CONTENT_IDS = [f"day_{str(data[0])}_m3u_content" for data in TEST_DATA]
MP3_DIR_IDS = [f"day_{str(data[0])}_mp3_dir" for data in TEST_DATA]
MP3_DIR_COUNT = [f"day_{str(data[0])}_mp3_dir_has_10_items" for data in TEST_DATA]
MP3S_EXIST_IDS = [f"day_{str(data[0])}_mp3s_exist" for data in TEST_DATA]
MP3S_FILENAMES_IDS = [f"day_{str(data[0])}_mp3_filenames" for data in TEST_DATA]
MP3S_ID3_TAGINFO = [f"day_{str(data[0])}_mp3_ID3_tagcheck" for data in TEST_DATA]
BASIC_CLI_IDS = [f"day_{str(data[0])}_basic_CLI_check" for data in TEST_DATA]


def test_ten_lists():
    """`ten_lists()` should return a list"""
    assert isinstance(ten_lists(), list)


def test_ten_lists_length():
    """`ten_lists()` should have a length of 10"""
    assert len(ten_lists()) == 10


def test_ten_lists_chapters():
    """Check the number of chapters in the 10 lists."""
    num_of_chapters = [89, 187, 78, 65, 62, 150, 31, 249, 250, 28]

    for chapters, bible_list in zip(num_of_chapters, ten_lists()):
        assert len(bible_list) == chapters


@pytest.mark.parametrize("day, listening_list", TEST_DATA, ids=PLAYLIST_IDS)
def test_reading_list(day, listening_list):
    """test generated reading lists using TEST_DATA"""
    assert reading_list(day, BIBLE_DIR) == listening_list


@pytest.mark.usefixtures("prepare_data")
@pytest.mark.parametrize("day", [item[0] for item in TEST_DATA], ids=M3U_IDS)
def test_m3u_creation(day):
    """tests the creation of m3u playlist files"""
    create_m3u(day, BIBLE_DIR)
    m3u_filename = "day" + str(day).zfill(3) + ".m3u"
    assert os.path.exists(m3u_filename)


@pytest.mark.usefixtures("prepare_data")
@pytest.mark.parametrize("day, listening_list", TEST_DATA, ids=M3U_CONTENT_IDS)
def test_m3u_content(day, listening_list):
    """checks the content of the generated m3u playlist files"""
    # create_m3u(day, BIBLE_DIR) m3u files already created since scope=session
    # and the m3u file creation function doesn't check if file exists
    m3u_filename = "day" + str(day).zfill(3) + ".m3u"
    listening_list.insert(0, "#EXTM3U")
    with open(m3u_filename, "r") as m3u:
        assert m3u.read().splitlines() == listening_list


@pytest.mark.usefixtures("prepare_data")
@pytest.mark.parametrize("day", [item[0] for item in TEST_DATA], ids=MP3_DIR_IDS)
def test_mp3_dir_creation(day):
    """tests the creation of the directory containing mp3 files"""
    create_mp3_dir(day, BIBLE_DIR)
    output_dir = "day" + str(day).zfill(3)
    assert os.path.exists(output_dir)


@pytest.mark.usefixtures("prepare_data")
@pytest.mark.parametrize("day", [item[0] for item in TEST_DATA], ids=MP3_DIR_COUNT)
def test_mp3_dir_count(day):
    """tests the presence of 10 files in the created directories"""
    # create_mp3_dir(day, BIBLE_DIR)  already created since scope=session
    output_dir = "day" + str(day).zfill(3)
    assert len(os.listdir(output_dir)) == 10


@pytest.mark.usefixtures("prepare_data")
@pytest.mark.parametrize("day", [item[0] for item in TEST_DATA], ids=MP3S_EXIST_IDS)
def test_mp3_files_creation(day):
    """tests the presence of 10 mp3 files in the created directories"""
    # create_mp3_dir(day, BIBLE_DIR)  already created since scope=session
    output_dir = "day" + str(day).zfill(3)
    ext = "*.mp3"
    for entry in os.listdir(output_dir):
        assert fnmatch.fnmatch(entry, ext)


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
    filenames = [
        mp3.strip().replace(f"{BIBLE_DIR}", f"{output_dir}/", 1)
        for mp3 in listening_list
        if mp3 != "#EXTM3U"
    ]
    files = [item.replace(f"{output_dir}/", "") for item in filenames]
    mp3_files = [str(idx).zfill(3) + mp3[4:] for idx, mp3 in enumerate(files, start=1)]
    assert sorted(mp3_filelist) == mp3_files


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
        assert audiofile.tag.track_num[0] == index


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
    assert result.exit_code == 0
    assert not result.exception
