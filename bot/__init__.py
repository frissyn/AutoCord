import os
import glob
import discord
import functools

from os.path import join
from os.path import isfile
from os.path import dirname
from os.path import basename

from discord.ext.commands import Bot


COLOR = 0x9370DB
GUILD = os.environ["GUILD"]
TOKEN = os.environ["BOT_SECRET"]
modules = glob.glob(join(dirname(__file__), "*.py"))
intents = discord.Intents.default()

with open("web/db/admins.txt", "r") as fh:
    names = fh.read()
    ADMINS = [n.split("--")[0] for n in names.split("\n")]

with open("bot/permissions.txt", "r") as fh:
    perms = fh.read()
    PERMISSIONS = [p for p in perms.split("\n")]

intents.members = True
intents.presences = True
autocord = Bot(command_prefix="a&", intents=intents)
autocord.remove_command("help")


def has_permission(admin=False, no_perms=None):
    def _inner(func):
        nonlocal admin

        @functools.wraps(func)
        async def ret(ctx, *args, **kwargs):
            nonlocal admin
            if admin:
                if str(ctx.author.id) not in ADMINS:
                    if no_perms != None:
                        await no_perms(ctx)
                    return
            return await func(ctx, *args, **kwargs)

        return ret

    return _inner


for m in modules:
    flag1 = isfile(m)
    flag2 = m.endswith("__init__.py")

    if flag1 and not flag2:
        m = basename(m).replace('.py', '')

        exec(f"from bot import {m}")
