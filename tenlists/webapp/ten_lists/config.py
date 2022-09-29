import os
from pathlib import Path

import sentry_sdk
from dotenv import load_dotenv
from sentry_sdk.integrations.flask import FlaskIntegration

# APP_ROOT = os.path.join(os.path.dirname(__file__), "..")  # refers to webapp dir
PROJECT_ROOT = Path(__file__).parents[3]  # 4 levels up


class BaseConfig(object):
    """
    Default Configuration
    """

    DEBUG = False
    TESTING = False

    TIMEZONE = "Africa/Lusaka"

    # This is rather redundant, as it is handled in create_app()
    if os.environ.get("FLASK_CONFIGURATION") == "default":
        env_path = os.path.join(PROJECT_ROOT, "env/.default.env")
        load_dotenv(dotenv_path=env_path)

    # Secret key for generating tokens
    SECRET_KEY = os.getenv("TENLISTS_SECRET_KEY")

    # Mail Configuration
    MAIL_SERVER = os.getenv("MAIL_SERVER")
    MAIL_PORT = os.getenv("MAIL_PORT")
    MAIL_USE_TLS = os.getenv("MAIL_USE_TLS")
    MAIL_USERNAME = os.getenv("TENLISTS_EMAIL_USER")
    MAIL_PASSWORD = os.getenv("TENLISTS_EMAIL_PWD")
    MAIL_DEFAULT_SENDER = os.getenv("MAIL_DEFAULT_SENDER")

    TENLISTS_API_BASE = os.getenv("TENLISTS_API_BASE")


class DevelopmentConfig(BaseConfig):
    """
    Development Configuration
    """

    # DEBUG can only be set to True in a development environment for security reasons
    DEBUG = True

    # This is rather redundant, as it is handled in create_app()
    if os.environ.get("FLASK_CONFIGURATION") == "development":
        env_path = os.path.join(PROJECT_ROOT, "env/.dev.env")
        load_dotenv(dotenv_path=env_path, override=True, verbose=True)

    # Secret key for generating tokens
    SECRET_KEY = os.getenv("TENLISTS_SECRET_KEY_DEV")

    # Flask Debug Toolbar Settings
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    # Mail Configuration
    MAIL_SERVER = os.getenv("MAIL_SERVER_DEV")
    MAIL_PORT = os.getenv("MAIL_PORT_DEV")
    MAIL_USERNAME = os.getenv("TENLISTS_EMAIL_USER_DEV")
    MAIL_PASSWORD = os.getenv("TENLISTS_EMAIL_PWD_DEV")
    MAIL_USE_TLS = os.getenv("MAIL_USE_TLS")
    MAIL_USE_SSL = os.getenv("MAIL_USE_SSL")
    MAIL_DEFAULT_SENDER = "Ten Lists App <noreply@example.com>"

    # Other
    EXPLAIN_TEMPLATE_LOADING = True

    TENLISTS_API_BASE = os.getenv("TENLISTS_API_BASE")


class StagingConfig(BaseConfig):
    """
    Staging Configuration
    """

    DEBUG = False

    # This is rather redundant, as it is handled in create_app()
    if os.environ.get("FLASK_CONFIGURATION") == "staging":
        env_path = os.path.join(PROJECT_ROOT, "env/.stage.env")
        load_dotenv(dotenv_path=env_path, override=True)

    # Secret key for generating tokens
    SECRET_KEY = os.getenv("TENLISTS_SECRET_KEY")

    # Mail Configuration
    MAIL_SERVER = os.getenv("MAIL_SERVER")
    MAIL_PORT = os.getenv("MAIL_PORT")
    MAIL_USE_TLS = os.getenv("MAIL_USE_TLS")
    MAIL_USERNAME = os.getenv("TENLISTS_EMAIL_USER")
    MAIL_PASSWORD = os.getenv("TENLISTS_EMAIL_PWD")
    MAIL_DEFAULT_SENDER = os.getenv("MAIL_DEFAULT_SENDER")

    TENLISTS_API_BASE = os.getenv("TENLISTS_API_BASE")


class ProductionConfig(BaseConfig):
    """
    Production Configuration
    """

    sentry_sdk.init(dsn=os.getenv("SENTRY_DSN"), integrations=[FlaskIntegration()])

    DEBUG = False
    SESSION_COOKIE_SECURE = True

    # =========================================================== #

    # skip loading .prod.env file since we're running in docker container

    # Also, this is rather redundant, as it is handled in create_app()
    # if os.environ.get("FLASK_CONFIGURATION") == "production":
    #     env_path = os.path.join(PROJECT_ROOT, "env/.prod.env")
    #     load_dotenv(dotenv_path=env_path, override=True)

    # =========================================================== #

    # Secret key for generating tokens
    SECRET_KEY = os.getenv("TENLISTS_SECRET_KEY")

    # Mail Configuration
    MAIL_SERVER = os.getenv("MAIL_SERVER")
    MAIL_PORT = os.getenv("MAIL_PORT")
    MAIL_USE_TLS = os.getenv("MAIL_USE_TLS")
    MAIL_USERNAME = os.getenv("TENLISTS_EMAIL_USER")
    MAIL_PASSWORD = os.getenv("TENLISTS_EMAIL_PWD")
    MAIL_DEFAULT_SENDER = os.getenv("MAIL_DEFAULT_SENDER")

    SERVER_NAME = os.getenv("SERVER_NAME")

    TENLISTS_API_BASE = os.getenv("TENLISTS_API_BASE")
