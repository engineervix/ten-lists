# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project attempts to adhere to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [v0.6.2](https://github.com/engineervix/ten-lists/compare/v0.6.1...v0.6.2) (2020-01-29)

### Added

- Windows Support

## [v0.6.1](https://github.com/engineervix/ten-lists/compare/v0.6.0...v0.6.1) (2019-09-29)

### Added

- the script now has tests! I'll still add some more tests

## [v0.6.0](https://github.com/engineervix/ten-lists/compare/v0.5.0...v0.6.0) (2019-09-28)

### Changed

- the structure of the code to make it easier to read and test. Far from perfect -- more work still needs to be done.
- switched from [`argparse`](https://docs.python.org/3/library/argparse.html) to [`Click`](https://click.palletsprojects.com/en/7.x/) for the CLI
- the `BIBLE_DIRECTORY` can now be specified through the CLI as an argument, but a default one is provided

### Added

- some fancy terminal enhancements courtesy of [`colorama`](https://github.com/tartley/colorama), [`termcolor`](https://pypi.org/project/termcolor/) and [`pyfiglet`](https://github.com/pwaller/pyfiglet)

## [v0.5.0](https://github.com/engineervix/ten-lists/compare/v0.4.0...v0.5.0) (2019-06-22)

### Changed

- the codebase from `python2` to `python3`.

## [v0.4.0](https://github.com/engineervix/ten-lists/compare/v0.2.0...v0.4.0) (2015-05-11)

### Added

- the ability to change ID3 tag info in the copied files, so that whenever you play the files from any device (eg car, home theatre), the desired order is maintained.
- the ability to rename the files so that their sequence follows the desired reading plan order, instead of the order of appearance in the Bible. Key Modules: eyed3, os.rename

### Changed

- the naming convention of files and directories by enforcing a 3-digit number by padding with zeroes using the `zfill()` function. This was done because I noticed that when I was creating a one week playlist from day 96 to 102; `day100` was considered as occuring before `day96` during processing, which isn't the case. This is because of the `1` after the `day`. Thus, to fix the problem, we need to have `day096` instead of `day96`.

> NOTE: I don't know what happened for v0.3.0 to be skipped! Anyway, these were my early dev days!

## [v0.2.0](https://github.com/engineervix/ten-lists/compare/v0.1.0...v0.2.0) (2014-05-27)

### Added

- the ability to copy (using [shutil](https://docs.python.org/3/library/shutil.html)) the files on the playlist file into a new folder so that you can carry the folder and listen anywhere (car, home theatre, etc).

## [v0.1.0](https://github.com/engineervix/ten-lists/releases/tag/v0.1.0) (2014-05-27)

- Initial version
