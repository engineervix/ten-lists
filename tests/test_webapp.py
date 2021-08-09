from flask import url_for


def test_app(client):
    """
    simple test to get started testing the flask webapp
    """
    assert client.get(url_for("main.index")).status_code == 200
    # assert client.get("/").status_code == 200


def test_api_valid_route(client):
    """
    test a valid route and check that it works as expected
    """
    res = client.get("/ten-lists/api/v1.0/mp3s?&day=56&format=json")
    mp3_files = [
        "static/ENGESVC2DA/B03___12_Luke________ENGESVC2DA.mp3",
        "static/ENGESVC2DA/A02___06_Exodus______ENGESVC2DA.mp3",
        "static/ENGESVC2DA/B10___05_Ephesians___ENGESVC2DA.mp3",
        "static/ENGESVC2DA/B27___13_Revelation__ENGESVC2DA.mp3",
        "static/ENGESVC2DA/A22___02_SongofSongs_ENGESVC2DA.mp3",
        "static/ENGESVC2DA/A19__056_Psalms______ENGESVC2DA.mp3",
        "static/ENGESVC2DA/A20___25_Proverbs____ENGESVC2DA.mp3",
        "static/ENGESVC2DA/A09___07_1Samuel_____ENGESVC2DA.mp3",
        "static/ENGESVC2DA/A23___56_Isaiah______ENGESVC2DA.mp3",
        "static/ENGESVC2DA/B05___28_Acts________ENGESVC2DA.mp3",
    ]
    lst = [item["url"] for item in res.json["mp3s"]]
    assert lst == mp3_files
    assert res.status_code == 200


def test_api_invalid_day(client):
    """
    a day less than 1 or > 600 should return status code 403
    """
    res = client.get("/ten-lists/api/v1.0/mp3s?&day=0&format=json")
    assert res.status_code == 403


def test_404(client):
    """
    an unknown route should return status code 404
    """
    res = client.get("/foo")
    assert res.status_code == 404
