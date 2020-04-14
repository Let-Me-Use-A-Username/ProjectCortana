import discord
from discord.ext import commands


class Manners(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Loading Cog: Manners')
        print('========================')
        print('Game cog loaded successfully.\n')

    global times
    times = {}

    @commands.Cog.listener()
    async def on_message(self, message):
        global times
        member = message.author.name
        if member not in times:
            times[member] = 0
        print(times)
        swear = ['gamw', 'gamo', 'GAMW', 'GAMO', 'panagia', 'PANAGIA', 'malaka', 'MALAKA', 'malakas', 'MALAKAS',
                 'malakia', 'MALAKIA', 'omfg', 'OMFG', 'shit', 'SHIT', 'fuck', 'FUCK']
        in_line = list(message.content.split(' '))
        for word in swear:
            if word in in_line:
                if times[member] == 1:
                    await message.channel.send(message.author.mention + ' Έχεις άλλη μία ευκαιρία στο λέω')
                if times[member] == 2:
                    times[member] = 0
                    roles = []
                    await message.channel.send(message.author.mention + 'Τώρα την γάμησες ρε αρχίδι')
                    for role in message.author.roles:
                        roles.append(role.name)
                    await message.channel.send('Current roles: ' + str(roles))
                    for role in roles:
                        await remove_role(message.author, role) # <-- Needs a fix
                    await message.channel.send('Current roles: ' + str(roles))
                times[member] += 1
                break


def setup(client):
    client.add_cog(Manners(client))
