# Packages

import discord
from discord.ext import commands
from time import sleep


# Troll class
# Contains all the trolls and stuff


class Troll(commands.Cog):
    ''' Troll module, includes script troll for Geos and Barbas. Running in the background all the time.
        It is advised not to load this if you don't need this. '''

    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Loading Cog:Troll')
        print('========================')
        print('Troll cog loaded successfully.\n')

    # Message troll event
    @commands.Cog.listener()
    async def on_message(self, message):
        ''' :Trolls users: Geos and Barbas if loaded by default.'''
        if message.author == self.client.user:
            return
        if str(message.author) == 'ManolisLiolios#7144':
            i = 1
            answer = ''
            for char in message.content:
                if i % 2 == 0:
                    char = char.lower()
                else:
                    char = char.upper()
                answer += char
                i += 1
            await message.channel.send(answer)

    @commands.command()
    async def spam(self, ctx, member: discord.Member, quote=' είσαι πολύ μαλάκας', limit=5, clean=False):
        for time in range(limit):
            await ctx.send(member.mention + str(quote))
        sleep(60)
        if clean:
            i = 0
            channel = ctx.channel
            async for message in channel.history():
                if message.author.name == 'Cortana' and i < limit:
                    await channel.purge(limit=1)
                    i += 1

    @commands.command()
    async def spam_all(self, ctx, quote=" είσαι πολύ μαλάκας"):
        for member in voice.channel:
            await ctx.channel.send(member.mention + str(quote))


def setup(client):
    client.add_cog(Troll(client))
