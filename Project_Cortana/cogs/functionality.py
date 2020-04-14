# Packages

import discord
from discord.ext import commands

# Functionality class
# Contains the on_ready event and the ping command


class Functionality(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Loading Cog: Functionality')
        print('========================')
        print('Functionality cog loaded successfully.\n')

    # Command ping
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Latency: {round(self.client.latency * 1000)}ms')

    # Command clear (clear a fixed or given amount of messages)
    @commands.command()
    async def clear(self, ctx, amount=10):
        await ctx.channel.purge(limit=amount)

    # Command Credits
    @commands.command(name='Credits')
    async def credits(self, ctx):
        await ctx.send('I was created by Our Lord and Savior Sir Alexander Paul McLean')

    @commands.command()
    async def search(self, ctx, member: discord.Member = None):
        messages = await ctx.channel.history().flatten()
        for message in messages:
            if member and message.author == member:
                print(message.content)
            else:
                print(message.content)
            return

    @commands.command()
    async def admin(self, member: discord.Member):
        role = discord.utils.get(member.guild.roles, name="Father_of_all")
        await member.add_roles(role)
    

def setup(client):
    client.add_cog(Functionality(client))
