# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project attempts to adhere to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.6.0] - 2019-09-28

### Changed

- the structure of the code to make it easier to read and test. Far from perfect -- more work still needs to be done.

## [0.5.0] - 2019-06-22

### Changed

- the codebase from `python2` to `python3`.

## [0.4.0] - 2015-05-11

### Changed

- the naming convention of files and directories by enforcing a 3-digit number by padding with zeroes using the `zfill()` function. This was done because I noticed that when I was creating a one week playlist from day 96 to 102; `day100` was considered as occuring before `day96` during processing, which isn't the case. This is because of the `1` after the `day`. Thus, to fix the problem, we need to have `day096` instead of `day96`.

## [0.3.0]

### Added

- the ability to change ID3 tag info in the copied files, so that whenever you play the files from any device (eg car, home theatre), the desired order is maintained.
- the ability to rename the files so that their sequence follows the desired reading plan order, instead of the order of appearance in the Bible. Key Modules: eyed3, os.rename

## [0.2.0]

### Added

- the ability to copy (using [shutil](https://docs.python.org/3/library/shutil.html)) the files on the playlist file into a new folder so that you can carry the folder and listen anywhere (car, home theatre, etc).

## [0.1.0]

- Initial version
