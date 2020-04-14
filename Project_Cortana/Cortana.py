# Packages


import discord
import aiohttp
import os
import youtube_dl
from discord.voice_client import VoiceClient
from discord.ext import commands

client = commands.Bot(command_prefix = '>', case_insensitive=True)

# Load cog
@client.command()
async def load(ctx, extension):
    ''': Loads a given Cog. Note that Cog names are case sensitive, all of them are spelled with lowercase characters.
         If spelled wrong, the Cog will not load and it will return an Error.'''
    client.load_extension(f'cogs.{extension}')
    await ctx.send('Initializing Sequence...')
    await ctx.send('Sequence Complete.\nExtension Loaded')

# Unload cog
@client.command()
async def unload(ctx, extension):
    ''': Unloads a given Cog. Note that Cog names are case sensitive, all of them are spelled with lowercase characters.
         If spelled wrong, the Cog will not unload and it will return an Error.'''
    client.unload_extension(f'cogs.{extension}')
    await ctx.send('Initializing Sequence...')
    await ctx.send('Sequence Complete.\nExtension Unloaded.')
    
# Reload cog
@client.command()
async def reload(ctx, extension):
    ''': Reloads a given Cog. Basically it is equivalent to running load() and then unload()
         If spelled wrong, the Cog will not reload and it will return an Error'''
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send('Initializing sequence...')
    await ctx.send('Sequence Complete.\nExtension Reloaded.')

# in progress
@client.command()
async def yt(ctx, url):
    try:
        author = ctx.message.author
        voice_channel = author.voice.channel
        stand_by = await voice_channel.connect()
    except discord.ClientException:
        for channel in client.voice_clients:
            if channel.guild == ctx.message.guild:
                stand_by = channel
    opts = {}
    with youtube_dl.YoutubeDL(opts) as ydl:
        song_info = ydl.extract_info(url, download=False)
        print(song_info)
        stand_by.play(discord.FFmpegPCMAudio(executable=r'C:\ffmpeg - Python module\ffmpeg-20190614-6f82bf9-win64-static\bin\ffmpeg.exe',source=song_info))
        # player = await stand_by.create_ytdl_player(url)
        # player.start()
        stand_by.is_playing()

# Moves member to channel   
@client.command()
async def move(ctx, member: discord.Member, channel: discord.VoiceChannel):
    m_from = member.voice.channel
    if m_from == channel:
        pass
    else:
        await member.move_to(channel)

# Calls bot to current channel and plays Dog barks
@client.command()
async def dog(ctx):
    try:
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
    except discord.ClientException:
        for channel in client.voice_clients:
            if channel.guild == ctx.message.guild:
                vc = channel
    vc.play(discord.FFmpegPCMAudio(executable=r'C:\ffmpeg - Python module\ffmpeg-20190614-6f82bf9-win64-static\bin\ffmpeg.exe', source='Barking Dogs.mp3'))
    vc.is_playing()

# Calls bot to current channel and plays Dog barks
@client.command()
async def Boi(ctx):
    try:
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
    except discord.ClientException:
        for channel in client.voice_clients:
            if channel.guild == ctx.message.guild:
                vc = channel
    vc.play(discord.FFmpegPCMAudio(
        executable=r'C:\ffmpeg - Python module\ffmpeg-20190614-6f82bf9-win64-static\bin\ffmpeg.exe',
        source='HEHE BOI.mp3'))
    vc.is_playing()

# Adds role to member
@client.command()
async def add_role(self, member: discord.Member, to_add: discord.Role):
    role = discord.utils.get(member.guild.roles, name=to_add.name)
    await member.add_roles(role)
    print('Role ' + str(role) + ' was added to ' + str(member))

# Removes role from member
@client.command()
async def remove_role(self, member: discord.Member, to_remove: discord.Role):
    role = discord.utils.get(member.guild.roles, name=to_remove.name)
    await member.remove_roles(role)
    print('Role ' + str(role) + ' was removed from ' + str(member))

# connects to given channel
@client.command()
async def connect(ctx, voice=None):
    if voice is None:
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        for guild in client.guilds:
            for channel in guild.channels:
                if voice.replace('_', ' ') == channel.name:
                    await channel.connect()

# disconnects from any channel connected to
@client.command()
async def disconnect(ctx):
    for channel in client.voice_clients:
        if channel.guild == ctx.message.guild:
            return await channel.disconnect()


@client.event
async def on_member_join(member):
    channel = general
    for voice.channel in client.guilds:
        if voice.channel.name == 'General':
            await channel.send(member.mention + ' Σήμερα 9 Μάκρη')


"""
@client.event
async def on_message(message):
    if message.author == 'Rythm#3722':
        await message.channel.purge(limit=1)
    for channel in client.voice_clients:
        if channel.guild == message.guild:
            bot = 'Rythm#3722'
            await bot.edit(voice_channel=None)
"""

# Load all cogs
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        if filename == 'troll.py' or filename == 'manners.py':
            print('\nTroll and Manners wont load for convenienve purposes.\nLoad it with command load()\n')
        else:
           client.load_extension(f'cogs.{filename[:-3]}')
        

client.run('NTg3NjMwNjc0MjI0MzQ5MjI0.XP5YMQ.e3gOwFXiSRg1_NIEziJDqShgEDo')

# Roles : [<Role id=324283937440530434 name='@everyone'>,
# <Role id=587638592768311298 name='Cortana'>,
# <Role id=584820108866617470 name='Rythm'>,
# <Role id=519900183752867850 name='ΤΑΦΟΣ'>,
# <Role id=453519913479307269 name='Fox-Bot'>,
# <Role id=397801521225662464 name='DJ'>,
# <Role id=364861344056344577 name='Plebs'>,
# <Role id=393817437772185610 name='Nobles'>,
# <Role id=575063987650035714 name='принцесса'>,
# <Role id=504610702842134538 name='Officers'>,
# <Role id=519894142453809157 name='Streamer'>,
# <Role id=533358410465542144 name='ΣΥΝΔΕΣΜΙΤΕΣ'>,
# <Role id=393836826315718668 name='4 HORSEMEN'>,
# <Role id=364861368647680000 name='Overlord'>]
