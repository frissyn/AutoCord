import flask

from web import app

from bot import autocord
from bot.util import permission_map


@app.route("/")
def index():
    return flask.render_template("index.html")


@app.route("/dashboard")
def dashboard():
    return flask.render_template("dash.html")


@app.route("/info")
def information():
    return flask.render_template("info.html")


@app.route("/library")
def library():
    return flask.render_template("library.html")


@app.route("/b/<int:botID>")
def bot_page(botID):
    guild = autocord.get_guild(437048931827056642)
    bot = guild.get_member(botID)

    perms = permission_map(botID)
    permNum = bot.guild_permissions.value

    return flask.render_template(
        "bot.html", bot=bot, perms=perms, permNum=permNum
    )


@app.route("/rules")
def rules_page():
    return flask.render_template("rules.html")
