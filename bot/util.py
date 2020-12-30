from bot import autocord
from bot import PERMISSIONS


def get_bots(split=True):
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
            idle.append(bot)

    if split:
        return (active, idle)
    else:
        return active + idle


def permission_map(i: int):
    perm_map = {}

    guild = autocord.get_guild(437048931827056642)
    bot = guild.get_member(i)
    bot_perms = bot.guild_permissions
    
    for perm in PERMISSIONS:
        p = bot_perms.__getattribute__(perm)
        #print(f"{perm}: {p}")

        perm_map[perm] = p
    
    del perm_map["value"]

    return [(k, v) for k, v in perm_map.items()]
