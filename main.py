# version


import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')



@bot.event
async def on_ready():
    print('Bot loaded. Yay!')


@bot.command()
async def hi(ctx):
    await ctx.send("Hi, {} !".format(ctx.message.author.name))

bot.run('TOKEN')
