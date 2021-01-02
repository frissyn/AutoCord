import os

basedir = os.path.abspath(os.path.dirname(__file__))


class ProConfig(object):
    DEBUG = False
    TESTING = False
    FLASK_DEBUG = 0
    CACHE_TYPE = "simple"
    CACHE_DEFAULT_TIMEOUT = 300
    SECRET_KEY = os.environ["TOKEN"]
    SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(ProConfig):
    DEBUG = True
    TESTING = True
    FLASK_DEBUG = 1
    CACHE_TYPE = "none"
