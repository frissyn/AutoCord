# import json
# import asyncio
import discord

from bot import COLOR
from bot import autocord

from bot.util import permission_map

from discord import Embed

from datetime import datetime


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
