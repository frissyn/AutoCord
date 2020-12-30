from .config import ProConfig
from .config import DevConfig

from flask import Flask
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from threading import Thread

app = Flask(__name__)
app.config.from_object(ProConfig)
#app.config.from_object(DevConfig)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.init_app(app)

# --------------------------------------

from web import login
from web.routes import *
from web import processors


try:
    db.create_all()
    print("SQLAlchemy DB Initialized.")
except Exception:
    pass


server = Thread(
    target=app.run,
    args=(),
    kwargs={
        "host": "0.0.0.0",
        "port": 8080,
        "threaded": True
    }
)
