# pylint: disable=missing-module-docstring
import os
import glob
from shutil import copy, rmtree
import timeit
import pytest
from tqdm import tqdm
from gtts import gTTS
import eyed3
from tenlists.cli.__main__ import ten_lists

BIBLE_DIR = "_ENGESVC2DA"


@pytest.fixture(scope="session")
def prepare_data():
    """Prepare sample MP3 files for testing. Delete afterwards"""

    # Setup: Prepare MP3 files
    start = timeit.default_timer()

    bible_directory = os.path.join(os.getcwd(), BIBLE_DIR)

    os.makedirs(bible_directory, exist_ok=True)

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
        print(f"Error: {ex.filename} - {ex.strerror}.")

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
