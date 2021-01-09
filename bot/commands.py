import web
import json
import discord

from web import db

from discord import Embed

from bot import COLOR
from bot import ADMINS
from bot import autocord

from bot.util import format_cmd
from bot.util import permission_map

from datetime import datetime


with open("web/db/notifs.json", "r") as file:
    notifTemps = json.load(file)


CMD = {
    "categories": {
        "general": "Contains the general command for AutoCord interactions.",
        "reporting": "Contains commands for reporting info to the admins",
        "misc": "Contains commands that don't fit into the other categories."
    },
    "general": {
        "--bot <user>": "Returns the link to a User Bot's information page.",
        "--library": "Returns the link to the index of all User Bots",
        "--permissions": "Returns all permission values for a User Bot.",
        "--status": "Returns number of Online and Offline User Bots."
    },
    "reporting": {
        "--conflict <prefix> <num>": "Report the number of bots that share a prefix.",
    },
    "misc": {
        "--ping": "Pings the AutoCord bot and returns ping latency."
    }
}


@autocord.command(name="bot")
async def bot_page(ctx, m: discord.Member):
    if m.bot:
        em = Embed(
            title=f"{m.display_name}'s InfoPage",
            description=f"You can find **{m.display_name}**'s InfoPage"
            + f"\nhere at https://autocord.repl.co/b/{m.id}",
            color=COLOR,
        )
    else:
        em = Embed(
            title=f"Lookup Error Occurred",
            description=f"**{m.display_name}** is not a Bot User!",
            color=COLOR,
        )

    await ctx.send(embed=em)


@autocord.command(name="conflict")
async def conflict(ctx, prefix: str, count: int):
    for a in ADMINS:
        notif = web.models.Notification()
        temp = notifTemps["conflict"]

        notif.user_id = str(a)
        notif.is_action = True
        notif.title = temp["title"].format(name=ctx.author.name)
        notif.body = temp["body"].format(
            name = ctx.author.name,
            discrim = ctx.author.discriminator,
            timestamp = datetime.now(),
            count = count,
            prefix = prefix,
        )

        db.session.add(notif)
        db.session.commit()
    
    em = Embed(
        title="Prefix Conflict Reported!",
        description=f"A report has been sent to the admins that"
        + f" {count} or more bots have the prefix `{prefix}`.\n"
        + "Thanks for your help!",
        color=COLOR,
    )

    await ctx.send(embed=em)


@autocord.command(name="library")
async def library(ctx):
    em = Embed(
        title="User Bot Library",
        description="You can find the full library of User Bots "
        + "here at https://autocord.repl.co/library",
        color=COLOR,
    )

    await ctx.send(embed=em)


@autocord.command(name="permissions")
async def permissions(ctx, m: discord.Member):
    if m.bot:
        perm_map = permission_map(m.id)
        perm_str = ""

        for k, v in perm_map:
            perm_str += f"**{k}**: {v}\n"

        em = Embed(
            title=f"Permission Map for **{m.display_name}**",
            description=perm_str,
            color=COLOR,
        )

        await ctx.send(embed=em)
    else:
        em = Embed(
            title=f"Lookup Error Occurred",
            description=f"**{m.display_name}** is not a Bot User!",
            color=COLOR,
        )

        await ctx.send(embed=em)


@autocord.command(name="ping")
async def ping(ctx):
    l = round(autocord.latency * 1000, 2)
    em = Embed(title="Pong!", description="", color=COLOR)
    now = datetime.now().strftime("%B %d, %Y\n(%I:%M %p)")

    em.add_field(name="Response Timestamp:", value=f"{now}")
    em.add_field(name="Response Latency:", value=f"{l} ms")

    await ctx.send(embed=em)


@autocord.command(name="status")
async def get_all(ctx):
    guild = autocord.get_guild(437048931827056642)
    bots = guild.get_role(439587658058956811)
    bots = bots.members

    idle = []
    active = []

    for bot in bots:
        flag = str(bot.status)

        if flag == "online" or flag == "idle":
            active.append(bot)
        else:
            print(flag)
            idle.append(bot)

    em = Embed(title="User Bot Statuses", description="", color=COLOR)
    em.add_field(name="Active Bots:", value=str(len(active)), inline=True)
    em.add_field(name="Idle Bots:", value=str(len(idle)), inline=True)

    await ctx.send(embed=em)


# ~-~-~-~-~-~-~-~-~ HELP ~-~-~-~-~-~-~-~-~ #

@autocord.command(name="help")
async def help(ctx, cat=None):
    if not cat:
        c = format_cmd("--help <category>")
        em = Embed(
            name="AutoCord Command Index",
            description=f"Use\n{c}to get help on a category!",
            color=COLOR
        )

        for cat, desc in CMD["categories"].items():
            c = format_cmd(f"--help <{cat}>")
            em.add_field(
                name=f"**{cat.title()} Commands:**",
                value=f"{c}*{desc}*\n",
                inline=False
            )
    else:
        em = Embed(
            name=f"{cat.title()} Commands",
            description=f"",
            color=COLOR
        )

        for cmd, desc in CMD[cat].items():
            em.add_field(
                name=f"{format_cmd(cmd)}",
                value=f"{desc}",
                inline=False
            )
    
    await ctx.send(embed=em)
