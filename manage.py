from flask_script import Manager

from tenlists.webapp.ten_lists import create_app

# Setup Flask-Script with command line commands
manager = Manager(create_app)

if __name__ == "__main__":
    # python manage.py                      # shows available commands
    # python manage.py runserver --help     # shows available runserver options
    manager.run()
