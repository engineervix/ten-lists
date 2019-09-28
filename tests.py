import pytest
import os
from shutil import copy
import timeit
from gtts import gTTS
import eyed3
from tqdm import tqdm
from bible_playlist_generator import ten_lists


@pytest.fixture(scope='session')
def prepare_data():
    """Prepare sample MP3 files for testing. Delete afterwards"""

    # Setup: Prepare MP3 files
    start = timeit.default_timer()

    BIBLE_DIRECTORY = "_temp_dir/"

    # now we go programmatically create an audio file

    tts = gTTS('audio', lang='en')
    audio_file = os.path.join(os.getcwd(), "audio_file.mp3")
    tts.save(audio_file)

    # add ID3 tag info to the file
    mp3_file = eyed3.load(audio_file)
    mp3_file.initTag()
    mp3_file.tag.artist = u"test"
    mp3_file.tag.track_num = 1
    mp3_file.tag.save()

    # we then make multiple copies of the audio file

    for bible_list in tqdm(ten_lists):
        for mp3 in bible_list:
            new_mp3_file = os.path.join(BIBLE_DIRECTORY, mp3)
            copy(audio_file, new_mp3_file)

    yield  # This is where the testing happens

    # Teardown : discard the data
    # Cleanup
    try:
        os.remove(audio_file)
    except OSError as e:  # if failed, report it back to the user
        print("Error: %s - %s." % (e.filename, e.strerror))

    stop = timeit.default_timer()
    total_time = stop - start

    print(f"Total running time: {total_time} seconds")
