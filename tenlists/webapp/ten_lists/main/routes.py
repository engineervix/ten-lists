#!/usr/bin/env python3

"""A Simple RESTful server implemented using the Flask-RESTful extension."""

import sys
import os
import time
from datetime import datetime

from flask import Blueprint, render_template, abort, request

from flask_restful import Resource, reqparse, fields, marshal

import eyed3

project_dir = os.path.abspath(os.path.join(__file__, "../../../../"))
dir_path = os.path.dirname(os.path.realpath(__file__))
relative_project_dir = os.path.relpath(project_dir, dir_path)

sys.path.append(project_dir)

from tenlists.cli.__main__ import reading_list  # noqa: E402

BIBLE_DIR = os.path.join("ten_lists/static/", "ENGESVC2DA")

main = Blueprint("main", __name__)


@main.route("/")
def index():
    now = datetime.utcnow()
    return render_template("home.html", now=now)


mp3s = []


def mp3_duration(seconds):
    """
    Convert seconds into minutes and seconds (%-M:%S)
    """
    return time.strftime("%-M:%S", time.gmtime(seconds))


def generate_playlist(day):
    """
    generates playlist for a particular `day`
    """
    selected_playlist = reading_list(day, BIBLE_DIR)

    if len(mp3s) != 0:
        mp3s.clear()

    for idx, mp3_file in enumerate(selected_playlist, start=1):
        audio = eyed3.load(mp3_file)
        if "New Testament" in audio.tag.album:
            COVER_ART = "static/img/album_art/new_testament_cover_art.jpg"
        else:
            COVER_ART = "static/img/album_art/old_testament_cover_art.jpg"
        mp3s.append(
            {
                "id": idx,
                "name": audio.tag.title,
                "artist": audio.tag.artist,
                "album": audio.tag.album,
                # 'url': "../" + mp3_file,
                "url": mp3_file.replace("ten_lists/static/", "static/"),
                "cover_art_url": COVER_ART,
                "duration": mp3_duration(audio.info.time_secs),
            }
        )


mp3_fields = {
    "name": fields.String,
    "artist": fields.String,
    "album": fields.String,
    "url": fields.String,
    "cover_art_url": fields.String,
    "duration": fields.String
    # 'uri': fields.Url('mp3')
}


class MP3ListAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            "name",
            type=str,
            required=True,
            help="No mp3 name provided",
            location="json",
        )
        self.reqparse.add_argument("artist", type=str, default="", location="json")
        self.reqparse.add_argument("album", type=str, default="", location="json")
        super(MP3ListAPI, self).__init__()

    def get(self):

        # Get `day` from request args
        day = int(request.args.get("day"))
        if day > 600 or day < 1:
            abort(403)
        generate_playlist(day)

        return {"mp3s": [marshal(mp3, mp3_fields) for mp3 in mp3s]}


class MP3API(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("name", type=str, location="json")
        self.reqparse.add_argument("artist", type=str, location="json")
        self.reqparse.add_argument("album", type=str, location="json")
        self.reqparse.add_argument("url", type=str, location="json")
        self.reqparse.add_argument("cover_art_url", type=str, location="json")
        self.reqparse.add_argument("duration", type=str, location="json")
        super(MP3API, self).__init__()

    def get(self, id):
        # Get `day` from request args
        day = int(request.args.get("day"))
        if day > 600 or day < 1:
            abort(403)
        generate_playlist(day)

        mp3 = [mp3 for mp3 in mp3s if mp3["id"] == id]
        if len(mp3) == 0:
            abort(404)
        return {"mp3": marshal(mp3[0], mp3_fields)}


def initialize_routes(api):
    api.add_resource(MP3ListAPI, "/ten-lists/api/v1.0/mp3s", endpoint="mp3s")
    api.add_resource(MP3API, "/ten-lists/api/v1.0/mp3s/<int:id>", endpoint="mp3")
