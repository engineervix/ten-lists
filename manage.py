from flask.cli import FlaskGroup

from tenlists.webapp.ten_lists import create_app

cli = FlaskGroup(create_app=create_app)

if __name__ == "__main__":
    cli()
