import discord
from discord.ext import commands
from discord.utils import get

class VoiceUtilities(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def join(self, ctx):
        channel = ctx.message.author.voice.channel
        voice = get(self.bot.voice_clients, guild=ctx.guild)

        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()

        await ctx.send(f"Joined {channel}")

    @commands.command()
    async def leave(self, ctx):

        voice = get(self.bot.voice_clients, guild=ctx.guild)

        if voice and voice.is_connected():
            await voice.disconnect()
            await ctx.send(f"Left")
        else:
            await ctx.send(f"I'm not in a voice channel")

    @commands.command()
    async def rejoin(self, ctx):
        voice = get(self.bot.voice_clients, guild=ctx.guild)
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

def setup(bot):
    bot.add_cog(VoiceUtilities(bot))