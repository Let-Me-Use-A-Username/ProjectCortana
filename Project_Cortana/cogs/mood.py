import discord
from discord.ext import commands


class Mood(commands.Cog):

    def __init__(self, client, mood):
        self.client = client
        self.mood = mood

    @commands.command()
    async def set_mood(self, ctx, mood):
        if ctx.message.author.name == '_Amen_':
            if self.mood != mood:
                self.mood = mood
                await ctx.channel.send('I am ' + self.mood)
            else:
                await ctx.channel.send('I am already ' + self.mood)
        else:
            await ctx.channel.send('You have no permission to play with me, only daddy has')

    @commands.command()
    async def check(self, ctx):
        await ctx.send('I am feeling ' + self.mood)

    # async def moods(self):
        # if self.mood == 'sad':
            # deadlock
        # if self.mood == 'happy':
            # use every command

    @commands.command()
    async def deadlock(self, ctx):
        if self.mood == 'mad' or self.mood == 'sad' or str(ctx.message.author) == '_Amen_#3904':
            for member in get_all_members():
                if member.enable_tts_command is True:
                    await member.edit_settings(disable_tts_command)
        """
            @commands.Cog.listener()
            async def on_message(self, message):
                if message.author != '_Amen_#3904' and message.content.startswith('>'):
                    await message.channel.send(message.author.mention + ' I am not happy with you')
                else:
                    await message.channel.send('Hello Daddy <3')
        """


def setup(client):
    client.add_cog(Mood(client, mood=None))
