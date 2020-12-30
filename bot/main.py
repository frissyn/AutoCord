#import json
#import asyncio
import discord

from bot import COLOR
from bot import autocord

from discord import Embed

from datetime import datetime

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


@autocord.command(name="library")
async def library(ctx):
    em = Embed(
        title="User Bot Library",
        description="You can find the full library of User Bots " +
        "here at https://autocord.repl.co/library",
        color=COLOR
    )

    await ctx.send(embed=em)


@autocord.command(name="bot")
async def bot_page(ctx, b: discord.Member):
    if b.bot:
        em = Embed(
            title=f"{b.display_name}'s InfoPage",
            description=f"You can find **{b.display_name}**'s InfoPage" +
            f"\nhere at https://autocord.repl.co/b/{b.id}",
            color=COLOR
        )
    else:
        em = Embed(
            title=f"Lookup Error Occurred",
            description=f"**{b.display_name}** is not a Bot User!",
            color=COLOR
        )

    await ctx.send(embed=em)
