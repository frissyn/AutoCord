import flask

from web import app

from bot import autocord

from flask_login import current_user
from flask_login import login_required

from bot.util import get_bots
from bot.util import permission_map
from web.models import Notification

@app.route("/")
def index():
    return flask.render_template("index.html")


@app.route("/dashboard")
@login_required
def dashboard():
    notifs = Notification.query.filter_by(user_id=current_user.id)
    return flask.render_template("dash.html", notifs=notifs)


@app.route("/info")
def information():
    return flask.render_template("info.html")


@app.route("/library")
def library():
    bots = get_bots(split=False)
    return flask.render_template("library.html", bots=bots)


@app.route("/b/<int:botID>")
def bot_page(botID):
    guild = autocord.get_guild(437048931827056642)
    bot = guild.get_member(botID)

    perms = permission_map(botID)
    permNum = bot.guild_permissions.value

    return flask.render_template("bot.html", bot=bot, perms=perms, permNum=permNum)


@app.route("/rules")
def rules_page():
    return flask.render_template("rules.html")


@app.route("/submit")
def submission_page():
    return flask.render_template("submit.html")
