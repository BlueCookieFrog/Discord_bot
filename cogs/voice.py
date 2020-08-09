import discord
import os
import random
from discord.ext import commands
from discord.utils import get
loc = "."

class Voice(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def kurwa(self, ctx):
        song_there = os.path.isfile(f"{loc}/Res/TymekDrzePizde.mp3")
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if song_there:
            voice.play(discord.FFmpegPCMAudio(
                f"{loc}/Res/TymekDrzePizde.mp3"))
            voice.source = discord.PCMVolumeTransformer(voice.source)
            voice.source.volume = 0.50

    @commands.command()
    async def dundundun(self, ctx):
        song_there = os.path.isfile(f"{loc}/Res/dundundun.mp3")
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if song_there:
            voice.play(discord.FFmpegPCMAudio(f"{loc}/Res/dundundun.mp3"))
            voice.source = discord.PCMVolumeTransformer(voice.source)
            voice.source.volume = 0.50

    @commands.command()
    async def quack(self, ctx):
        song_there = os.path.isfile(f"{loc}/Res/quack.mp3")
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if song_there:
            voice.play(discord.FFmpegPCMAudio(f"{loc}/Res/quack.mp3"))
            voice.source = discord.PCMVolumeTransformer(voice.source)
            voice.source.volume = 0.50

    @commands.command(hidden=True)
    async def araara(self, ctx):
        song_there = os.path.isfile(f"{loc}/Res/araara.mp3")
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if song_there:
            voice.play(discord.FFmpegPCMAudio(f"{loc}/Res/araara.mp3"))
            voice.source = discord.PCMVolumeTransformer(voice.source)
            voice.source.volume = 0.50

    @commands.command(hidden=True)
    async def itjustworks(self, ctx):
        song_there = os.path.isfile(f"{loc}/Res/itjustworks.mp3")
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if song_there:
            voice.play(discord.FFmpegPCMAudio(f"{loc}/Res/itjustworks.mp3"))
            voice.source = discord.PCMVolumeTransformer(voice.source)
            voice.source.volume = 1.00

    @commands.command()
    async def dialogue(self, ctx):
        song_there = os.path.isfile(f"{loc}/Res/dialogue.mp3")
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if song_there:
            voice.play(discord.FFmpegPCMAudio(f"{loc}/Res/dialogue.mp3"))
            voice.source = discord.PCMVolumeTransformer(voice.source)
            voice.source.volume = 0.05

    @commands.command()
    async def doit(self, ctx):
        song_there = os.path.isfile(f"{loc}/Res/doit.mp3")
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if song_there:
            voice.play(discord.FFmpegPCMAudio(f"{loc}/Res/doit.mp3"))
            voice.source = discord.PCMVolumeTransformer(voice.source)
            voice.source.volume = 1.00

    @commands.command()
    async def rece(self, ctx):
        song_there = os.path.isfile(f"{loc}/Res/rece.mp3")
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if song_there:
            voice.play(discord.FFmpegPCMAudio(f"{loc}/Res/rece.mp3"))
            voice.source = discord.PCMVolumeTransformer(voice.source)
            voice.source.volume = 1.00

    @commands.command()
    async def kto_wpierdolil(self, ctx):
        song_there = os.path.isfile(f"{loc}/Res/kto_wpierdolil.mp3")
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if song_there:
            voice.play(discord.FFmpegPCMAudio(f"{loc}/Res/kto_wpierdolil.mp3"))
            voice.source = discord.PCMVolumeTransformer(voice.source)
            voice.source.volume = 0.70

    @commands.command(hidden=True)
    async def heyyou(self, ctx):
        song_there = os.path.isfile(f"{loc}/Res/heyyou.mp3")
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if song_there:
            voice.play(discord.FFmpegPCMAudio(f"{loc}/Res/heyyou.mp3"))
            voice.source = discord.PCMVolumeTransformer(voice.source)
            voice.source.volume = 0.70

    @commands.command(hidden=True)
    async def droga(self, ctx):
        song_there = os.path.isfile(f"{loc}/Res/droga.mp3")
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if song_there:
            voice.play(discord.FFmpegPCMAudio(f"{loc}/Res/droga.mp3"))
            voice.source = discord.PCMVolumeTransformer(voice.source)
            voice.source.volume = 0.70

    @commands.command()
    async def drzewo(self, ctx):
        song_there = os.path.isfile(f"{loc}/Res/drzewo.mp3")
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if song_there:
            voice.play(discord.FFmpegPCMAudio(f"{loc}/Res/drzewo.mp3"))
            voice.source = discord.PCMVolumeTransformer(voice.source)
            voice.source.volume = 0.50

    @commands.command()
    async def halo(self, ctx):
        song_there = os.path.isfile(f"{loc}/Res/halo.mp3")
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if song_there:
            voice.play(discord.FFmpegPCMAudio(f"{loc}/Res/halo.mp3"))
            voice.source = discord.PCMVolumeTransformer(voice.source)
            voice.source.volume = 1

    @commands.command()
    async def bububu(self, ctx):
        song_there = os.path.isfile(f"{loc}/Res/bububu.mp3")
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if song_there:
            voice.play(discord.FFmpegPCMAudio(f"{loc}/Res/bububu.mp3"))
            voice.source = discord.PCMVolumeTransformer(voice.source)
            voice.source.volume = 1.00

    @commands.command(hidden=True)
    async def boomer(self, ctx):
        song_there = os.path.isfile(f"{loc}/Res/boomer.mp3")
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if song_there:
            voice.play(discord.FFmpegPCMAudio(f"{loc}/Res/boomer.mp3"))
            voice.source = discord.PCMVolumeTransformer(voice.source)
            voice.source.volume = 0.50

    @commands.command()
    async def wodka(self, ctx):
        song_there = os.path.isfile(f"{loc}/Res/wodka.mp3")
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if song_there:
            voice.play(discord.FFmpegPCMAudio(f"{loc}/Res/wodka.mp3"))
            voice.source = discord.PCMVolumeTransformer(voice.source)
            voice.source.volume = 0.50

    @commands.command()
    async def dziewczyna(self, ctx):
        song_there = os.path.isfile(f"{loc}/Res/dziewczyna.mp3")
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if song_there:
            voice.play(discord.FFmpegPCMAudio(f"{loc}/Res/dziewczyna.mp3"))
            voice.source = discord.PCMVolumeTransformer(voice.source)
            voice.source.volume = 0.80

    @commands.command(hidden=True)
    async def super(self, ctx):
        song_there = os.path.isfile(f"{loc}/Res/super.mp3")
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if song_there:
            voice.play(discord.FFmpegPCMAudio(f"{loc}/Res/super.mp3"))
            voice.source = discord.PCMVolumeTransformer(voice.source)
            voice.source.volume = 0.50

    @commands.command(hidden=True)
    async def argument(self, ctx):
        song_there = os.path.isfile(f"{loc}/Res/argument.mp3")
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if song_there:
            voice.play(discord.FFmpegPCMAudio(f"{loc}/Res/argument.mp3"))
            voice.source = discord.PCMVolumeTransformer(voice.source)
            voice.source.volume = 0.50

    @commands.command()
    async def jedenosiem(self, ctx):
        song_there = os.path.isfile(f"{loc}/Res/jedenosiem.mp3")
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if song_there:
            voice.play(discord.FFmpegPCMAudio(f"{loc}/Res/jedenosiem.mp3"))
            voice.source = discord.PCMVolumeTransformer(voice.source)
            voice.source.volume = 0.07

    @commands.command(hidden = True)
    async def aniol(self, ctx):
        song_there = os.path.isfile(f"{loc}/Res/aniol.mp3")
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if song_there:
            voice.play(discord.FFmpegPCMAudio(f"{loc}/Res/aniol.mp3"))
            voice.source = discord.PCMVolumeTransformer(voice.source)
            voice.source.volume = 0.60

    @commands.command(hidden=True)
    async def dziekuje(self, ctx):
        song_there = os.path.isfile(f"{loc}/Res/dziekuje.mp3")
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if song_there:
            voice.play(discord.FFmpegPCMAudio(f"{loc}/Res/dziekuje.mp3"))
            voice.source = discord.PCMVolumeTransformer(voice.source)
            voice.source.volume = 0.50

    @commands.command(hidden=True)
    async def nieprzeszkadzam(self, ctx):
        song_there = os.path.isfile(f"{loc}/Res/nieprzeszkadzam.mp3")
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if song_there:
            voice.play(discord.FFmpegPCMAudio(
                f"{loc}/Res/nieprzeszkadzam.mp3"))
            voice.source = discord.PCMVolumeTransformer(voice.source)
            voice.source.volume = 0.50

    @commands.command(hidden=True)
    async def jakto(self, ctx):
        song_there = os.path.isfile(f"{loc}/Res/jakto.mp3")
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if song_there:
            voice.play(discord.FFmpegPCMAudio(f"{loc}/Res/jakto.mp3"))
            voice.source = discord.PCMVolumeTransformer(voice.source)
            voice.source.volume = 0.50

    @commands.command()
    async def szybko(self, ctx):
        song_there = os.path.isfile(f"{loc}/Res/szybko.mp3")
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if song_there:
            voice.play(discord.FFmpegPCMAudio(f"{loc}/Res/szybko.mp3"))
            voice.source = discord.PCMVolumeTransformer(voice.source)
            voice.source.volume = 0.50

    @commands.command()
    async def mammalego(self, ctx):
        song_there = os.path.isfile(f"{loc}/Res/mammalego.mp3")
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if song_there:
            voice.play(discord.FFmpegPCMAudio(f"{loc}/Res/mammalego.mp3"))
            voice.source = discord.PCMVolumeTransformer(voice.source)
            voice.source.volume = 0.50

    @commands.command()
    async def honkhonk(self, ctx):
        song_there = os.path.isfile(f"{loc}/Res/honkhonk.mp3")
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if song_there:
            voice.play(discord.FFmpegPCMAudio(f"{loc}/Res/honkhonk.mp3"))
            voice.source = discord.PCMVolumeTransformer(voice.source)
            voice.source.volume = 0.50

    @commands.command()
    async def laughing(self, ctx):
        song_there = os.path.isfile(f"{loc}/Res/whos.mp3")
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if song_there:
            voice.play(discord.FFmpegPCMAudio(f"{loc}/Res/whos.mp3"))
            voice.source = discord.PCMVolumeTransformer(voice.source)
            voice.source.volume = 0.50

    @commands.command()
    async def vape(self, ctx):
        vape_ = [f"{loc}/Res/vape0.mp3", f"{loc}/Res/vape1.mp3",
                 f"{loc}/Res/vape2.mp3", f"{loc}/Res/vape3.mp3"]
        vape = random.choice(vape_)
        song_there = os.path.isfile(vape)
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if song_there:
            voice.play(discord.FFmpegPCMAudio(vape))
            voice.source = discord.PCMVolumeTransformer(voice.source)
            voice.source.volume = 3.00

    @commands.command()
    async def honk(self, ctx):

        rand = random.randint(0, 3)
        await ctx.send(file=discord.File(f"{loc}/Res/honk{rand}.png"))

        song_there = os.path.isfile(f"{loc}/Res/honk.mp3")
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if song_there:
            voice.play(discord.FFmpegPCMAudio(f"{loc}/Res/honk.mp3"))
            voice.source = discord.PCMVolumeTransformer(voice.source)
            voice.source.volume = 0.07

def setup(bot):
    bot.add_cog(Voice(bot))