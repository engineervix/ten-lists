# ten-lists

This project provides both a CLI (using [click](https://click.palletsprojects.com/en/7.x/)) and a webapp (using [flask](https://palletsprojects.com/p/flask/)), which generate a playlist of 10 Bible Chapters (represented by 10 mp3 files) to be listened to on any given day _x_, according to [**Professor Grant Horner's Bible-Reading System**](https://sohmer.net/media/professor_grant_horners_bible_reading_system.pdf). The audio Bible is as downloaded from the [_Faith Comes by Hearing®_ website](http://www.bible.is/audiodownloader).

> You can see the webapp in action [here](https://ten.dumela.cc/)

[![python3.8](https://img.shields.io/badge/python-3.8-brightgreen.svg)](https://python.org/)
[![CircleCI](https://circleci.com/gh/engineervix/ten-lists/tree/master.svg?style=svg)](https://circleci.com/gh/engineervix/ten-lists/tree/master)
[![Coverage Status](https://coveralls.io/repos/github/engineervix/ten-lists/badge.svg)](https://coveralls.io/github/engineervix/ten-lists)
[![Maintainability](https://api.codeclimate.com/v1/badges/0f58287b5eaf57213fa2/maintainability)](https://codeclimate.com/github/engineervix/ten-lists/maintainability)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/f566d7c0bd464cb2b17ef9604b61a748)](https://www.codacy.com/gh/engineervix/ten-lists/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=engineervix/ten-lists&amp;utm_campaign=Badge_Grade)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![DeepSource](https://static.deepsource.io/deepsource-badge-light-mini.svg)](https://deepsource.io/gh/engineervix/ten-lists/?ref=repository-badge)
[![Commitizen friendly](https://img.shields.io/badge/commitizen-friendly-brightgreen.svg)](http://commitizen.github.io/cz-cli/)
[![Conventional Changelog](https://img.shields.io/badge/changelog-conventional-brightgreen.svg)](http://conventional-changelog.github.io)
[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg)](https://conventionalcommits.org)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [ten-lists](#ten-lists)
  - [Developer setup 💻](#developer-setup-)
    - [Requirements](#requirements)
      - [Essential](#essential)
      - [Extra](#extra)
    - [Installation](#installation)
      - [You need the MP3 files](#you-need-the-mp3-files)
      - [Concerning the CLI tool](#concerning-the-cli-tool)
    - [Tests](#tests)
  - [Deployment](#deployment)
  - [Notes](#notes)
  - [TODO](#todo)
  - [Credits](#credits)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Developer setup 💻

### Requirements

#### Essential

Start by ensuring that you have [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/):

```sh
# check that you have docker on your machine
docker -v
# check that you have docker-compose on your machine
docker-compose -v
```

If you don't have Docker and Docker Compose, then click the respective links above for installation instructions for your platform.

#### Extra

Good to have if you'd like to hack on the project. Not required if you just wanna run it, in which case Docker and Docker Compose will suffice.

- A [Python](https://www.python.org/) **3.8** virtual environment. You can use any tool of your choice to manage multiple Python versions on your machine.
  - Activate your python virtual environment and `pip install --upgrade pip`
  - Install dependencies: `pip install -r requirements.txt`.
  - Setup [pre-commit](https://pre-commit.com/) by running `pre-commit install` followed by `pre-commit install --hook-type commit-msg`. Optionally run `pre-commit run --all-files` to make sure your pre-commit setup is okay.
- [Node.js](https://nodejs.org/en/) **v14**
  - Install the Node.js dependencies via `npm install`

### Installation

Upon cloning this repository (or forking + cloning your fork), navigate to the cloned project directory.

Then create the required environment variables file (`.env`) by making a copy of the provided sample file `.env.sample` and renaming it to `.dev.env`:

```sh
cp -v .env.sample .env
```

> NOTE: If you're not using a docker-based deployment approach, then, for production, the file should be `.prod.env`, for staging `.stage.dev`

You should be able to run the project without updating anything. If you wanna update the mail settings (which you probably don't really need immediately) -- you could use a service like [mailtrap.io](https://mailtrap.io/) for development. If you choose Mailtrap, then the variables to update are `TENLISTS_EMAIL_USER_DEV` and `TENLISTS_EMAIL_PWD_DEV`. The other settings are for use in production (`SERVER_NAME` and `SENTRY_DSN`).

Build the images and spin up the containers:

```sh
COMPOSE_PROJECT_NAME=tenlists docker-compose up -d --build
```

When you run the above for the first time, it may take a while, depending on your internet connection speed.

Once the build is complete, you can check the logs for the `web` container via

```sh
docker-compose logs web
```

If everything is ok, you should see something like this:

```console
tenlists-web-1  | tenlists :: ready
tenlists-web-1  |  * Serving Flask app "tenlists.webapp.ten_lists" (lazy loading)
tenlists-web-1  |  * Environment: development
tenlists-web-1  |  * Debug mode: on
tenlists-web-1  |  * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
tenlists-web-1  |  * Restarting with stat
tenlists-web-1  |  * Debugger is active!
tenlists-web-1  |  * Debugger PIN: 719-114-836
```

You can also check the logs for the `node` container via

```sh
docker-compose logs node
```

If all's well, you should see something like this:

```console
tenlists-node-1  |
tenlists-node-1  | > ten-lists@0.6.2 start /usr/src/app
tenlists-node-1  | > grunt
tenlists-node-1  |
tenlists-node-1  | Running "clean:dist" (clean) task
tenlists-node-1  | >> 4 paths cleaned.
tenlists-node-1  |
tenlists-node-1  | Running "newer:copy" (newer) task
tenlists-node-1  |
tenlists-node-1  | Running "newer:copy:fa" (newer) task
tenlists-node-1  |
tenlists-node-1  | Running "copy:fa" (copy) task
tenlists-node-1  | Copied 8 files
tenlists-node-1  |
tenlists-node-1  | Running "newer-postrun:copy:fa:1:/usr/src/app/node_modules/grunt-newer/.cache" (newer-postrun) task
tenlists-node-1  |
tenlists-node-1  | Running "newer:copy:bootstrap" (newer) task
tenlists-node-1  |
tenlists-node-1  | Running "copy:bootstrap" (copy) task
tenlists-node-1  | Copied 10 files
tenlists-node-1  |
tenlists-node-1  | Running "newer-postrun:copy:bootstrap:2:/usr/src/app/node_modules/grunt-newer/.cache" (newer-postrun) task
tenlists-node-1  |
tenlists-node-1  | Running "newer:copy:jquery" (newer) task
tenlists-node-1  |
tenlists-node-1  | Running "copy:jquery" (copy) task
tenlists-node-1  | Copied 4 files
tenlists-node-1  |
tenlists-node-1  | Running "newer-postrun:copy:jquery:3:/usr/src/app/node_modules/grunt-newer/.cache" (newer-postrun) task
tenlists-node-1  |
tenlists-node-1  | Running "newer:copy:moment" (newer) task
tenlists-node-1  |
tenlists-node-1  | Running "copy:moment" (copy) task
tenlists-node-1  | Copied 5 files
tenlists-node-1  |
tenlists-node-1  | Running "newer-postrun:copy:moment:4:/usr/src/app/node_modules/grunt-newer/.cache" (newer-postrun) task
tenlists-node-1  |
tenlists-node-1  | Running "newer:cssmin" (newer) task
tenlists-node-1  |
tenlists-node-1  | Running "newer:cssmin:dist" (newer) task
tenlists-node-1  | No newer files to process.
tenlists-node-1  |
tenlists-node-1  | Running "newer:uglify" (newer) task
tenlists-node-1  |
tenlists-node-1  | Running "newer:uglify:dist" (newer) task
tenlists-node-1  | No newer files to process.
tenlists-node-1  |
tenlists-node-1  | Running "browserSync:dev" (browserSync) task
tenlists-node-1  | [Browsersync] Proxying: http://web:5000
tenlists-node-1  | [Browsersync] Access URLs:
tenlists-node-1  |  -----------------------------------
tenlists-node-1  |        Local: http://localhost:3000
tenlists-node-1  |     External: http://151.26.0.3:3000
tenlists-node-1  |  -----------------------------------
tenlists-node-1  |           UI: http://localhost:3001
tenlists-node-1  |  UI External: http://localhost:3001
tenlists-node-1  |  -----------------------------------
tenlists-node-1  | [Browsersync] Watching files...
tenlists-node-1  |
tenlists-node-1  | Running "watch" task
tenlists-node-1  | Waiting...
tenlists-node-1  | [Browsersync] Reloading Browsers...
tenlists-node-1  | [Browsersync] Reloading Browsers...
```

You can access the dev server at <http://127.0.0.1:5000>.

#### You need the MP3 files

Now, at this stage, you probably won't get much from the now running app, because you actually need the MP3 files to work with! So, especially for the CLI tool, you have to download the Audio Bible from the [_Faith Comes by Hearing®_ website](http://www.bible.is/audiodownloader). The 2001 ESV dramatized Bible (size is over 2Gb) formed the basis for this project's code, including the expected filenames. If the file naming convention has changed, then there's a chance everything will break. Anyway, I hope that won't be the case ...

For the web app, we previously would create a directory `ENGESVC2DA` in `tenlists/webapp/ten_lists/static/` and place your downloaded MP3 files in there. See [this line in `tenlists/webapp/ten_lists/main/routes.py`](https://github.com/engineervix/ten-lists/blob/0878900c45e2a2664ea8328562942120ccced2a2/tenlists/webapp/ten_lists/main/routes.py#L23-L25).

However, the code has been rewritten in such a way as to use a cloud service ([s3](https://aws.amazon.com/s3/), [MinIO](https://min.io/), [Backblaze](https://www.backblaze.com/), [Cloudinary](https://cloudinary.com/), etc.) for the files. This should hopefuly simplify both on-boarding and deployment, especially that at the time of writing this the webapp is deployed using [Dokku](https://dokku.com/). You'll therefore have to upload these files to your preferred cloud provider, and set the environment variable `TENLISTS_MP3_CLOUD_STORAGE_BASE_URL` (see that `.env.sample` file for details).

#### Concerning the CLI tool

This project started off initially as a CLI tool to generate these mp3 files on my computer and play them on a USB stick or copy them over to my phone. However, the scope later changed to have a web application that can allow me to listen from anywhere. So lately the focus has been more on the webapp than the CLI.

Notwithstanding, if you wanna use the CLI, you need to firstly ensure that you have a folder containing the required MP3 files, as described above. If you don't specify the folder when running the CLI tool, it'll assumes that there's a directory `ENGESVC2DA` in the project root. Once you've sorted this out, then you can run the CLI tool with the `--help` option so that you see how to use it:

**If you have a setup a python virtual environment and installed the python dependencies as described earlier in this README**

```sh
python tenlists/cli/__main__.py --help
```

So, for _example 1_, if I have my Bible folder `ENGESVC2DA` in the project root, and I run `python tenlists/cli/__main__.py -d 87`, I'll see the following in the console

```console
❯ python tenlists/cli/__main__.py -d 87
 _           _                __
|_)o|_ | _  |_)| _.  |o __|_ /__ _ ._  _ .__._|_ _ ._
|_)||_)|(/_ |  |(_|\/||_> |_ \_|(/_| |(/_|(_| |_(_)|
                   /

Welcome to the Bible Playlist Generator

Creating a playlist for day 87 ...
✓ playlist for day 87 successfully created.
✓ Copying of the Bible Chapters into the day087 directory was successful.
✓ ID3 tag info for the generated files in this directory has been updated.
✓ The files have been renamed in a sequential order.

-----Soli Deo Gloria-----
```

What has happended here? Well,

- I ran a command to generate a playlist for day 87 of the Bible Reading Plan
- The CLI tool has generated an [M3U Playlist](https://en.wikipedia.org/wiki/M3U), `day087.m3u` in the project root
- The CLI tool has created a folder, `day087`, in the project root -- containing the 10 MP3 files in the above playlist

_Example 2_; if I want to use `tenlists/webapp/ten_lists/static/ENGESVC2DA/` as my folder, then I'll go ahead and

```sh
python tenlists/cli/__main__.py -d 87 -f tenlists/webapp/ten_lists/static/ENGESVC2DA/
```

And I'll see the same results!

**If you're using Docker**

```sh
docker-compose exec web python tenlists/cli/__main__.py --help
```

Everything remains the same as the case where you're not using Docker.

### Tests

```sh
docker-compose exec web pytest
```

> WARNING: Running this test will delete the directory `tenlists/webapp/ten_lists/static/ENGESVC2DA/, so please ensure that you have a copy of your MP3 files somewhere. This shouldn't be the case though, and I intend to fix it soon, as you can see it's top on the TODO list. Feel free to submit a PR if this hasn't been fixed!

## Deployment

You can deploy this project using your [preferred choice of deployment](https://flask.palletsprojects.com/en/1.1.x/deploying/) (Docker, Heroku, Linux Server, etc.). However, I am working on setting it up to be ready "out of the box" for deployment to a [VPS](https://cloud.google.com/learn/what-is-a-virtual-private-server) using [Dokku](https://dokku.com/).

If you're gonna use Dokku, feel free to use [@engineervix/pre-dokku-server-setup](https://github.com/engineervix/pre-dokku-server-setup) to setup an Ubuntu Server on your VPS prior to installation of Dokku. You can have a look at [this gist](https://gist.github.com/engineervix/8d1825a7301239e7c4df3af78aaee9a4) for more details of how to deploy an application to Dokku. Other excellent resources:

- [How to deploy Django project to Dokku](https://www.accordbox.com/blog/how-deploy-django-project-dokku/#introduction)
- [Setting up Dokku with DigitalOcean and Namecheap (GitHub gist)](https://gist.github.com/djmbritt/10938092)
- [Deploying an app with Dokku](https://vitobotta.com/2022/02/16/deploying-an-app-with-dokku/)
- [Dokku Docs: Process Management](https://dokku.com/docs/processes/process-management/)
- [Dokku Docs: Zero Downtime Deploys](https://dokku.com/docs/deployment/zero-downtime-deploys/)
- [Dokku with Let's Encrypt behind Cloudflare](https://spiffy.tech/dokku-with-lets-encrypt-behind-cloudflare)
- [Cloudflare certificates + Dokku](https://okhlopkov.com/cloudflare-certificates-dokku/)
- [Securing Dokku with Let's Encrypt TLS Certificates](https://blog.semicolonsoftware.de/securing-dokku-with-lets-encrypt-tls-certificates/)

## Notes

- This project will be most useful to you if you use Professor Grant Horner's Bible-Reading System as the basis for your Bible Reading Plan.
- The Audio Bible version used is the 2001 ESV dramatized Bible (complete), as freely downloaded from http://www.bible.is/audiodownloader. (The size is over 2Gb)

## TODO

- [ ] Fix test to avoid overwriting `tenlists/webapp/ten_lists/static/ENGESVC2DA/` and deleting its contents
- [X] Use [Invoke](https://www.pyinvoke.org/) to encapsulate some tasks. For instance, `docker-compose exec web python tenlists/cli/__main__.py --help` is too long to type!
- [ ] Address [#1](https://github.com/engineervix/ten-lists/issues/1). [`configparser`](https://docs.python.org/3/library/configparser.html) might come in handy here.
- [ ] [Package](https://packaging.python.org/tutorials/packaging-projects/) this project. [This is a must read](https://packaging.python.org/guides/distributing-packages-using-setuptools/#configuring-your-project).
- [ ] [Improve Code Quality](https://codeclimate.com/github/engineervix/ten-lists/issues)
- [x] Rather than using [plain text files](https://github.com/engineervix/ten-lists/tree/v0.6.2/data), find a better way of storing the Bible Chapters ([JSON file](https://www.lucidchart.com/techblog/2018/07/16/why-json-isnt-a-good-configuration-language/), [SQLite database](https://www.sqlite.org/whentouse.html), [TinyDB](https://tinydb.readthedocs.io/en/latest/), etc)
- [x] Create a ~~GUI frontend or~~ web service ~~[to cater for non-tech users](https://www.inc.com/drew-hendricks/building-or-enhancing-software-for-non-technical-users-is-more-important-than-ev.html)~~ in order to not only cater for non-tech users but also to listen on-the-go. See the `webapp` directory for the source code. Also see the `package.json` file.

## Credits

- Bible Icon: <https://www.pngrepo.com/svg/235374/bible>
