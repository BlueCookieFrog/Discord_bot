import asyncio
import discord
import json
from discord.ext import commands
from discord.utils import get
import os

def get_prefix(ctx, message):
    with open('./config/prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

bot = commands.Bot(command_prefix = get_prefix)
bot_name='Tymbelownia#7917'

def read_token():
    with open(f'./token.txt', 'r') as f:
        lines = f.readlines()
        return lines[0].strip()

token = read_token()

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_guild_join(guild):
    with open('./config/prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = "."

    with open('./config/prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@bot.event
async def on_guild_remove(guild):
    with open('./config/prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('./config/prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@bot.command()
async def prefix(ctx, pref):
    with open('./config/prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = pref

    with open('./config/prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@bot.command(hidden=True)
async def load(ctx, extension):

    if str(ctx.author) == 'BlueCookieFrog#9874':
        bot.load_extension(f'cogs.{extension}')
        print(f'Loaded {extension}')
        await ctx.send(f'Loaded {extension}')
    else:
        await ctx.send(file = discord.File(f'./denied.gif'), delete_after=20)

@bot.command(hidden=True)
async def unload(ctx, extension):

    if str(ctx.author) == 'BlueCookieFrog#9874':
        bot.unload_extension(f'cogs.{extension}')
        print(f'Unloaded {extension}')
    else:
        await ctx.send(file = discord.File(f'./denied.gif'), delete_after=20)

@bot.command()
async def reload(ctx, extension):

    if str(ctx.author) == 'BlueCookieFrog#9874':
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
    else:
        await ctx.send(file = discord.File(f'./denied.gif'), delete_after=20)

#execution part

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
        print(f'Loaded {filename}')

bot.run(token)