import discord
from discord import VoiceChannel, Guild
from discord.ext import commands


class Utilities(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Loading Cog: Utilities')
        print('========================')
        print('Game cog loaded successfully.\n')


#    async def create_chanel(self):
#        return

    @commands.command()
    async def notify_all(self, ctx):
        for channel in ctx.message.server.channels:
            if channel.type == ChannelType.voice:
                for member in channel:
                    await ctx.send(member.Mention + " Wake up, It's adventure time!")


#    async def invite(self, ctx):
#        return


def setup(client):
    client.add_cog(Utilities(client))
