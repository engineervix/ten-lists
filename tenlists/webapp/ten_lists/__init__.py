import os

from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from flask_mail import Mail
from flask_moment import Moment
from flask_restful import Api

from flask_talisman import DEFAULT_CSP_POLICY, Talisman
from werkzeug.middleware.proxy_fix import ProxyFix

config = {
    "production": "tenlists.webapp.ten_lists.config.ProductionConfig",
    "staging": "tenlists.webapp.ten_lists.config.StagingConfig",
    "development": "tenlists.webapp.ten_lists.config.DevelopmentConfig",
    "default": "tenlists.webapp.ten_lists.config.BaseConfig",
}

moment = Moment()
mail = Mail()
toolbar = DebugToolbarExtension()

TENLISTS_MP3_CLOUD_STORAGE_BASE_URL = os.getenv("TENLISTS_MP3_CLOUD_STORAGE_BASE_URL")


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    config_name = os.getenv("FLASK_CONFIGURATION", "default")

    app.config.from_object(config[config_name])  # object-based default configuration
    app.config.from_pyfile("config.py", silent=True)  # instance-folders configuration

    mail.init_app(app)
    moment.init_app(app)

    if app.debug:
        toolbar.init_app(app)
    else:
        permissions_policy = {
            "accelerometer": "()",
            "ambient-light-sensor": "()",
            "autoplay": '(self "{}")'.format(TENLISTS_MP3_CLOUD_STORAGE_BASE_URL),
            "camera": "()",
            "display-capture": "()",
            "document-domain": "()",
            "encrypted-media": "()",
            "geolocation": "()",
            "gyroscope": "()",
            "interest-cohort": "()",
            "magnetometer": "()",
            "microphone": "()",
            "midi": "()",
            "payment": "()",
            "picture-in-picture": "()",
            "usb": "()",
        }
        Talisman(
            app,
            # strict_transport_security is already set by NGIИX
            strict_transport_security=False,
            content_security_policy=os.getenv("CSP_DIRECTIVES", DEFAULT_CSP_POLICY),
            permissions_policy=permissions_policy,
        )

    api = Api(app)

    from tenlists.webapp.ten_lists.errors.handlers import errors
    from tenlists.webapp.ten_lists.main.routes import initialize_routes, main

    app.register_blueprint(errors)
    app.register_blueprint(main)
    initialize_routes(api)

    app.wsgi_app = ProxyFix(app.wsgi_app)

    return app
