import os

from web import server
from bot import autocord

server.start()
autocord.run(os.environ["BOT_SECRET"])
