import asyncio
import discord
from discord.ext import commands
from discord.utils import get
import os

bot = commands.Bot(command_prefix='.')
bot_name = 'Tymbelownia#7917'

def read_token():
    with open(f'./token.txt', 'r') as f:
        lines = f.readlines()
        return lines[0].strip()

token = read_token()

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    print(f'Loaded {extension}')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    print(f'Unloaded {extension}')

@bot.command()
async def reload(ctx, extension):
    if extension == 'all':

        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                try:
                    bot.unload_extension(f'cogs.{filename[:-3]}')
                except commands.ExtensionNotLoaded:
                    pass
                bot.load_extension(f'cogs.{filename[:-3]}')
                print(f'Reloaded {filename}')
        print(f'Reloaded all')
    else:
        bot.unload_extension(f'cogs.{extension}')
        bot.load_extension(f'cogs.{extension}')
        print(f'Reloaded {extension}')

#execution part

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
        print(f'Loaded {filename}')

bot.run(token)