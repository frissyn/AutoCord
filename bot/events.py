import os
#import asyncio

from bot import autocord

G = int(os.environ["GUILD"])

@autocord.event
async def on_ready():
    print(f"{autocord.user.name} has connected to Discord!")

    for g in autocord.guilds:
        print("-"*4, f"Guild:: {g}")
