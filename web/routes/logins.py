import flask
import auth

from web import db
from web import app

from web.models import User
from web.models import is_admin

from flask_login import login_user
from flask_login import logout_user


@app.route("/login")
def login_base():
    dlink = auth.get_request_uri()

    return flask.redirect(dlink)


@app.route("/logout")
def logout():
    logout_user()
    return flask.redirect(flask.url_for("index"))


@app.route("/login/callback")
def login_callback():
    code = flask.request.args.get("code")
    token = auth.parse_token(auth.exchange_code(code))

    d = auth.req("GET", "/users/@me", "Bearer", token)
    user = User.query.filter_by(id=d["id"]).first()

    if not user:
        user = User()
        db.session.add(user)
    else:
        pass

    user.id = d["id"]
    user.id_type = "Discord"
    user.name = d["username"]
    user.pfp = auth.IMG_BASE.format(d["id"], d["avatar"], 128)
    user.is_admin = is_admin(d["id"])

    db.session.commit()
    login_user(user)

    return flask.redirect(flask.url_for("dashboard"))
