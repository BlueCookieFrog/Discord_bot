import discord
import random
import os
from discord.ext import commands
from discord.utils import get

class Misc(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def add(self, ctx, *args:float):
        sum = 0
        for x in args:
            sum += x
        await ctx.send(sum)

    @commands.command()
    async def multiply(self, ctx, *args:float):
        result = 1
        for x in args:
            result *= x
        await ctx.send(result)

    @commands.command()
    async def divide(self,ctx, *args:float):
        result = args[0]
        for x in args[1:]:
            if x == 0:
                await ctx.send('Dzielenie przez zero')
                return
            else:
                result = result / x
        await ctx.send(result)

    @commands.command()
    async def RandomNum(self, ctx, bottom, top):
        number = random.randrange(int(bottom), int(top))
        await ctx.send(number)

    @commands.command()
    async def choose(self, ctx, *args:str):
        choice = random.choice(args)
        await ctx.send(choice)

    @commands.command()
    async def teams(self, ctx, no_teams:int, *args:str):

        if len(args) < no_teams:
            await ctx.send('Za mało osób')
            return

        members = []
        for i in range(len(args)):
            members.append(args[i])

        if (len(members) % no_teams) != 0:
            await ctx.send('Nierówne zespoły')

        per_team = int(len(members) / no_teams)
        over = len(members) % no_teams
        additonal = False

        for x in range(no_teams):
            await ctx.send(f'Team {x+1}:')
            if over > 0:
                additonal = True
                over -= 1
            else:
                additonal = False
            for i in range(per_team + additonal):
                z = random.randint(0, len(members)-1)
                await ctx.send(members.pop(z))

def setup(bot):
    bot.add_cog(Misc(bot))