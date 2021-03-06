import discord
import os
import youtube_dl
from discord.ext import commands
from discord.utils import get

class Music(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def play(self, ctx, url:str):
        song_there = os.path.isfile("./song.mp3")
        try:
            if song_there:
                os.remove("./song.mp3")
        except PermissionError:
            print("Trying to delete song file, which is played")
            await ctx.send("ERROR: Music playing")
            return

        await ctx.send("Getting ready")

        voice = get(self.bot.voice_clients, guild=ctx.guild)

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


    @commands.command()
    async def skip(self, ctx):

        voice = get(self.bot.voice_clients, guild=ctx.guild)

        if not voice or not voice.is_connected():
            return await ctx.send('I\'m not playing anything')

        if voice.is_paused() or voice.is_playing():
            voice.stop()
            await ctx.send('Skipped', delete_after=30)

    @commands.command()
    async def pause(self, ctx):

        voice = get(self.bot.voice_clients, guild=ctx.guild)

        if not voice or not voice.is_connected():
            return await ctx.send('I\'m not playing anything')
        elif voice.is_paused():
            return

        voice.pause()
        await ctx.send('Paused', delete_after=30)

    @commands.command()
    async def resume(self, ctx):
        voice = get(self.bot.voice_clients, guild=ctx.guild)

        if not voice or not voice.is_connected():
            return await ctx.send('I\'m not in voice channel', delete_after=30)
        elif not voice.is_paused():
            return

        voice.resume()
        await ctx.send('Resumed')

def setup(bot):
    bot.add_cog(Music(bot))
