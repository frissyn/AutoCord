from web import db

from bot import ADMINS

from datetime import datetime

from flask_login import UserMixin


def is_admin(i: str):
    for s in ADMINS:
        if i == s:
            return True
        else:
            continue
    
    return False


class User(db.Model, UserMixin):
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    pfp = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)

    timestamp = db.Column(db.DateTime, default=datetime.utcnow(), nullable=False)
    bots = db.relationship("UserBot", backref="user", lazy=True)
    notifications = db.relationship("Notification", backref="owner", lazy=True)

    def __repr__(self):
        return f"<User @id:{self.id}, @name:{self.name}>"


class UserBot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    prefix = db.Column(db.String(4), nullable=False)

    name = db.Column(db.String(64), nullable=False)
    client_id = db.Column(db.String(18), nullable=False)

    user_id = db.Column(db.String, db.ForeignKey("user.id"))

    def __repr__(self):
        return f"<UserBot @name:{self.name}, @user: {self.user_id}>"


class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    body = db.Column(db.String, nullable=False)
    is_action = db.Column(db.Boolean, nullable=False, default=False)

    timestamp = db.Column(db.DateTime, default=datetime.utcnow(), nullable=False)
    user_id = db.Column(db.String, db.ForeignKey("user.id"))

    def __repr__(self):
        return f"<Notification <{self.body}>>"
