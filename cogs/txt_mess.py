import discord
from discord.ext import commands

bot_name='Tymbelownia#7917'

class TextMessages(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content == 'F' and str(message.author) != bot_name:
            channel = message.channel
            await channel.send('F')

class BotStatus(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['status'])
    async def Status(self, ctx, stat, *, act):
        """Status [online/dnd/idle] [string status]"""
        if stat != '':
            if stat == 'online':
                await self.bot.change_presence(status = discord.Status.online, activity = discord.Game(act))
            elif stat == 'dnd':
                await self.bot.change_presence(status = discord.Status.dnd, activity = discord.Game(act))
            elif stat == 'idle':
                await self.bot.change_presence(status = discord.Status.idle, activity = discord.Game(act))
def setup(bot):
    bot.add_cog(TextMessages(bot))
    bot.add_cog(BotStatus(bot))