from web import db

from datetime import datetime

from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)

    timestamp = db.Column(db.DateTime, default=datetime.utcnow(), nullable=False)

    def __repr__(self):
        return f"<User @id:{self.id}, @name:{self.name}>"
