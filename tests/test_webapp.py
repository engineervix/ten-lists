from flask import url_for


def test_app(client):
    """
    simple test to get started testing the flask webapp
    """
    assert client.get(url_for("main.index")).status_code == 200
