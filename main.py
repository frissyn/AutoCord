import os

from web import server
from bot import autocord

# Thread runs first, the Bot run()
# is a blocking method

server.start()
autocord.run(os.environ["BOT_SECRET"])
