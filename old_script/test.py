#import asyncio
import discord
import youtube_dl
from discord.ext import commands
from discord.utils import get
import random
import os

bot = commands.Bot(command_prefix='.')
bot_name='Tymbelownia#7917'

#loc = "d:/_Git/DSC"
loc = "."

def read_token():
    with open(f"{loc}/token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

token = read_token()

@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))
    await bot.change_presence(activity=discord.Game('Siup'))

@bot.command()
async def granie(ctx, left: str, right: int):
    txt = '{} DZIŚ GODZINA {}, GRASZ ALBO WYPIERDALASZ'.format(left.upper(), right)
    embed = discord.Embed(title=txt, description="", color=0x00ff00)
    await ctx.send(embed=embed)

@bot.command()
async def add(ctx, *args:float):
    sum = 0
    for x in args:
        sum += x
    await ctx.send(sum)

@bot.command()
async def kurwa(ctx):
    song_there = os.path.isfile(f"{loc}/Res/TymekDrzePizde.mp3")
    voice = get(bot.voice_clients, guild=ctx.guild)
    if song_there:
        voice.play(discord.FFmpegPCMAudio(f"{loc}/Res/TymekDrzePizde.mp3"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 0.50

@bot.command()
async def druzyna(ctx):
    song_there = os.path.isfile(f"{loc}/Res/druzyna.mp3")
    voice = get(bot.voice_clients, guild=ctx.guild)
    if song_there:
        voice.play(discord.FFmpegPCMAudio(f"{loc}/Res/druzyna.mp3"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 0.50

@bot.command()
async def train(ctx):
    song_there = os.path.isfile(f"{loc}/Res/train.mp3")
    voice = get(bot.voice_clients, guild=ctx.guild)
    if song_there:
        voice.play(discord.FFmpegPCMAudio(f"{loc}/Res/train.mp3"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 0.50

@bot.command()
async def dundundun(ctx):
    song_there = os.path.isfile(f"{loc}/Res/dundundun.mp3")
    voice = get(bot.voice_clients, guild=ctx.guild)
    if song_there:
        voice.play(discord.FFmpegPCMAudio(f"{loc}/Res/dundundun.mp3"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 0.50

@bot.command()
async def quack(ctx):
    song_there = os.path.isfile(f"{loc}/Res/quack.mp3")
    voice = get(bot.voice_clients, guild=ctx.guild)
    if song_there:
        voice.play(discord.FFmpegPCMAudio(f"{loc}/Res/quack.mp3"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 0.50

@bot.command()
async def araara(ctx):
    song_there = os.path.isfile(f"{loc}/Res/araara.mp3")
    voice = get(bot.voice_clients, guild=ctx.guild)
    if song_there:
        voice.play(discord.FFmpegPCMAudio(f"{loc}/Res/araara.mp3"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 0.50

@bot.command()
async def itjustworks(ctx):
    song_there = os.path.isfile(f"{loc}/Res/itjustworks.mp3")
    voice = get(bot.voice_clients, guild=ctx.guild)
    if song_there:
        voice.play(discord.FFmpegPCMAudio(f"{loc}/Res/itjustworks.mp3"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 1.00

@bot.command()
async def dialogue(ctx):
    song_there = os.path.isfile(f"{loc}/Res/dialogue.mp3")
    voice = get(bot.voice_clients, guild=ctx.guild)
    if song_there:
        voice.play(discord.FFmpegPCMAudio(f"{loc}/Res/dialogue.mp3"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 0.05

@bot.command()
async def dance(ctx):
    song_there = os.path.isfile(f"{loc}/Res/dance.mp3")
    voice = get(bot.voice_clients, guild=ctx.guild)
    if song_there:
        voice.play(discord.FFmpegPCMAudio(f"{loc}/Res/dance.mp3"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 0.50

@bot.command()
async def doit(ctx):
    song_there = os.path.isfile(f"{loc}/Res/doit.mp3")
    voice = get(bot.voice_clients, guild=ctx.guild)
    if song_there:
        voice.play(discord.FFmpegPCMAudio(f"{loc}/Res/doit.mp3"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 1.00

@bot.command()
async def rece(ctx):
    song_there = os.path.isfile(f"{loc}/Res/rece.mp3")
    voice = get(bot.voice_clients, guild=ctx.guild)
    if song_there:
        voice.play(discord.FFmpegPCMAudio(f"{loc}/Res/rece.mp3"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 1.00

@bot.command()
async def kto_wpierdolil(ctx):
    song_there = os.path.isfile(f"{loc}/Res/kto_wpierdolil.mp3")
    voice = get(bot.voice_clients, guild=ctx.guild)
    if song_there:
        voice.play(discord.FFmpegPCMAudio(f"{loc}/Res/kto_wpierdolil.mp3"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 0.70

@bot.command()
async def heyyou(ctx):
    song_there = os.path.isfile(f"{loc}/Res/heyyou.mp3")
    voice = get(bot.voice_clients, guild=ctx.guild)
    if song_there:
        voice.play(discord.FFmpegPCMAudio(f"{loc}/Res/heyyou.mp3"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 0.70

@bot.command()
async def droga(ctx):
    song_there = os.path.isfile(f"{loc}/Res/droga.mp3")
    voice = get(bot.voice_clients, guild=ctx.guild)
    if song_there:
        voice.play(discord.FFmpegPCMAudio(f"{loc}/Res/droga.mp3"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 0.70

@bot.command()
async def drzewo(ctx):
    song_there = os.path.isfile(f"{loc}/Res/drzewo.mp3")
    voice = get(bot.voice_clients, guild=ctx.guild)
    if song_there:
        voice.play(discord.FFmpegPCMAudio(f"{loc}/Res/drzewo.mp3"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 0.50

@bot.command()
async def halo(ctx):
    song_there = os.path.isfile(f"{loc}/Res/halo.mp3")
    voice = get(bot.voice_clients, guild=ctx.guild)
    if song_there:
        voice.play(discord.FFmpegPCMAudio(f"{loc}/Res/halo.mp3"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 1

@bot.command()
async def bububu(ctx):
    song_there = os.path.isfile(f"{loc}/Res/bububu.mp3")
    voice = get(bot.voice_clients, guild=ctx.guild)
    if song_there:
        voice.play(discord.FFmpegPCMAudio(f"{loc}/Res/bububu.mp3"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 1.00

@bot.command()
async def boomer(ctx):
    song_there = os.path.isfile(f"{loc}/Res/boomer.mp3")
    voice = get(bot.voice_clients, guild=ctx.guild)
    if song_there:
        voice.play(discord.FFmpegPCMAudio(f"{loc}/Res/boomer.mp3"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 0.50

@bot.command()
async def wodka(ctx):
    song_there = os.path.isfile(f"{loc}/Res/wodka.mp3")
    voice = get(bot.voice_clients, guild=ctx.guild)
    if song_there:
        voice.play(discord.FFmpegPCMAudio(f"{loc}/Res/wodka.mp3"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 0.50

@bot.command()
async def dziewczyna(ctx):
    song_there = os.path.isfile(f"{loc}/Res/dziewczyna.mp3")
    voice = get(bot.voice_clients, guild=ctx.guild)
    if song_there:
        voice.play(discord.FFmpegPCMAudio(f"{loc}/Res/dziewczyna.mp3"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 0.80

@bot.command()
async def super(ctx):
    song_there = os.path.isfile(f"{loc}/Res/super.mp3")
    voice = get(bot.voice_clients, guild=ctx.guild)
    if song_there:
        voice.play(discord.FFmpegPCMAudio(f"{loc}/Res/super.mp3"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 0.50

@bot.command()
async def argument(ctx):
    song_there = os.path.isfile(f"{loc}/Res/argument.mp3")
    voice = get(bot.voice_clients, guild=ctx.guild)
    if song_there:
        voice.play(discord.FFmpegPCMAudio(f"{loc}/Res/argument.mp3"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 0.50

@bot.command()
async def jedenosiem(ctx):
    song_there = os.path.isfile(f"{loc}/Res/jedenosiem.mp3")
    voice = get(bot.voice_clients, guild=ctx.guild)
    if song_there:
        voice.play(discord.FFmpegPCMAudio(f"{loc}/Res/jedenosiem.mp3"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 0.07

@bot.command()
async def vape(ctx):
    vape_ = [f"{loc}/Res/vape0.mp3",f"{loc}/Res/vape1.mp3",f"{loc}/Res/vape2.mp3",f"{loc}/Res/vape3.mp3" ]
    vape = random.choice(vape_)
    song_there = os.path.isfile(vape)
    voice = get(bot.voice_clients, guild=ctx.guild)
    if song_there:
        voice.play(discord.FFmpegPCMAudio(vape))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 3.00

@bot.command()
async def aniol(ctx):
    song_there = os.path.isfile(f"{loc}/Res/aniol.mp3")
    voice = get(bot.voice_clients, guild=ctx.guild)
    if song_there:
        voice.play(discord.FFmpegPCMAudio(f"{loc}/Res/aniol.mp3"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 0.60

@bot.command()
async def dziekuje(ctx):
    song_there = os.path.isfile(f"{loc}/Res/dziekuje.mp3")
    voice = get(bot.voice_clients, guild=ctx.guild)
    if song_there:
        voice.play(discord.FFmpegPCMAudio(f"{loc}/Res/dziekuje.mp3"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 0.50

@bot.command()
async def nieprzeszkadzam(ctx):
    song_there = os.path.isfile(f"{loc}/Res/nieprzeszkadzam.mp3")
    voice = get(bot.voice_clients, guild=ctx.guild)
    if song_there:
        voice.play(discord.FFmpegPCMAudio(f"{loc}/Res/nieprzeszkadzam.mp3"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 0.50

@bot.command()
async def jakto(ctx):
    song_there = os.path.isfile(f"{loc}/Res/jakto.mp3")
    voice = get(bot.voice_clients, guild=ctx.guild)
    if song_there:
        voice.play(discord.FFmpegPCMAudio(f"{loc}/Res/jakto.mp3"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 0.50

@bot.command()
async def szybko(ctx):
    song_there = os.path.isfile(f"{loc}/Res/szybko.mp3")
    voice = get(bot.voice_clients, guild=ctx.guild)
    if song_there:
        voice.play(discord.FFmpegPCMAudio(f"{loc}/Res/szybko.mp3"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 0.50

@bot.command()
async def mammalego(ctx):
    song_there = os.path.isfile(f"{loc}/Res/mammalego.mp3")
    voice = get(bot.voice_clients, guild=ctx.guild)
    if song_there:
        voice.play(discord.FFmpegPCMAudio(f"{loc}/Res/mammalego.mp3"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 0.50

@bot.command()
async def honkhonk(ctx):
    song_there = os.path.isfile(f"{loc}/Res/honkhonk.mp3")
    voice = get(bot.voice_clients, guild=ctx.guild)
    if song_there:
        voice.play(discord.FFmpegPCMAudio(f"{loc}/Res/honkhonk.mp3"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 0.50

@bot.command()
async def laughing(ctx):
    song_there = os.path.isfile(f"{loc}/Res/whos.mp3")
    voice = get(bot.voice_clients, guild=ctx.guild)
    if song_there:
        voice.play(discord.FFmpegPCMAudio(f"{loc}/Res/whos.mp3"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 0.50

@bot.command()
async def honk(ctx):

    rand = random.randint(0, 2)
    await ctx.send(file=discord.File(f"{loc}honk{rand}.png"))

    song_there = os.path.isfile(f"{loc}/Res/honk.mp3")
    voice = get(bot.voice_clients, guild=ctx.guild)
    if song_there:
        voice.play(discord.FFmpegPCMAudio(f"{loc}/Res/honk.mp3"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 0.07

    # voice.play(discord.FFmpegPCMAudio("honk.mp3"), after=lambda e: print(f"{name} has finished playing"))
    # voice.source = discord.PCMVolumeTransformer(voice.source)
    # voice.source.volume = 0.07

@bot.command()
async def RandomNum(ctx, bottom, top):
    number = random.randrange(int(bottom), int(top))
    await ctx.send(number)

@bot.command()
async def choose(ctx, *args:str):
    choice = random.choice(args)
    await ctx.send(choice)


@bot.command()
async def multiply(ctx, *args:float):
    result = 1
    for x in args:
        result *= x
    await ctx.send(result)

@bot.command()
async def divide(ctx, *args:float):
    result = args[0]
    for x in args[1:]:
        if x == 0:
            await ctx.send('Nie dziel przez zero debilu')
            return
        else:
            result = result / x
    await ctx.send(result)

@bot.command()
async def sranie(ctx):
    channel = ctx.channel
    randomMember = random.choice(channel.guild.members)
    await channel.send(f'{randomMember.mention} umyj dupę')

@bot.command(aliases=['zapraszam'])
async def join(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    await ctx.send(f"Joined {channel}")

@bot.command(aliases=['wypierdalaj'])
async def leave(ctx):

    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.disconnect()
        await ctx.send(f"Left")
    else:
        await ctx.send(f"I'm not in a voice channel")

@bot.command()
async def rejoin(ctx):
    voice = get(bot.voice_clients, guild=ctx.guild)
    channel = ctx.message.author.voice.channel

    if voice and voice.is_connected():
        await voice.disconnect()
        await ctx.send(f"Left")
    else:
        await ctx.send(f"I'm not in a voice channel")

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    await ctx.send(f"Joined {channel}")

@bot.command()
async def play(ctx, url:str):
    song_there = os.path.isfile("./song.mp3")
    try:
        if song_there:
            os.remove("./song.mp3")
    except PermissionError:
        print("Trying to delete song file, which is played")
        await ctx.send("ERROR: Music playing")
        return

    await ctx.send("Getting ready")

    voice = get(bot.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print("Downloading audio\n")
        ydl.download([url])

    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            name = file
            print(f"Renamed File: {file}\n")
            os.rename(file, "./song.mp3")

    voice.play(discord.FFmpegPCMAudio("./song.mp3"), after=lambda e: print(f"{name} has finished playing"))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.07

    nname = name.rsplit("-", 2)
    await ctx.send(f"Playing: {nname[0]}")
    print("Playing\n")


@bot.event
async def on_message(message):
    if message.content.startswith('.greet'):
        channel = message.channel
        await channel.send('Say hello!')

        def check(m):
            return m.content == 'hello' and m.channel == channel

        msg = await bot.wait_for('message', check=check)
        await channel.send('Hello {.author}!'.format(msg))

    if message.content == 'F' and str(message.author) != bot_name:
        channel = message.channel
        await channel.send('F')

    await bot.process_commands(message)

bot.run(token)