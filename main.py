import discord
from discord.ext import commands
from colorama import Fore
import asyncio
from webserver import keep_alive
import os

prefix = "$$"

keep_alive()

bot = commands.Bot(command_prefix=prefix,
                   help_command=None,
                   case_insensitive=False,
                   self_bot=True)


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.offline)
    print("Bot is ready!")


@bot.command()
async def helpowo(ctx):
    await asyncio.sleep(1)
    await ctx.message.delete()
    await ctx.send(
        '**$$AutoOwO= owo h, owo b, owo sell all, owo flip 600. $$stopautoOwO= Stops the bot. bybasses ban**'
    )


@bot.command()
async def stopautoOwO(ctx):
    await ctx.message.delete()
    await ctx.send(
        '***AutoOwo is now disabled! To enable it again say `$$AutoOwo*')
    global dmcs
    dmcs = False


@bot.command(pass_context=True)
async def autoOwO(ctx):
    await ctx.message.delete()
    await ctx.send(
        '***AutoOwo is now enabled! Thank you so much for using this script. if you have any suggestions, dm emo-dragen#2544 on discord!*'
    )
    global dmcs
    dmcs = True
    while dmcs:
        async with ctx.typing():
            await asyncio.sleep(3)
            await ctx.send('owo h')
            await asyncio.sleep(2)
            await ctx.send('owo b')
            await asyncio.sleep(4)
            await ctx.send('owo flip 3000')
            await asyncio.sleep(16)
            await ctx.send('owo h')
            await asyncio.sleep(2)
            await ctx.send('owo b')
            await asyncio.sleep(4)
            await ctx.send('owo slots 3000')
            await asyncio.sleep(16)
            await asyncio.sleep(3)
            await ctx.send('owo h')
            await asyncio.sleep(2)
            await ctx.send('owo b')
            await asyncio.sleep(4)
            await ctx.send('owo flip 3000')
            await asyncio.sleep(16)
            await ctx.send('owo h')
            await asyncio.sleep(2)
            await ctx.send('owo b')
            await asyncio.sleep(4)
            await ctx.send('owo slots 3000')
            await asyncio.sleep(16)
            await asyncio.sleep(3)
            await ctx.send('owo h')
            await asyncio.sleep(2)
            await ctx.send('owo b')
            await asyncio.sleep(4)
            await ctx.send('owo flip 3000')
            await asyncio.sleep(16)
            await ctx.send('owo h')
            await asyncio.sleep(2)
            await ctx.send('owo b')
            await asyncio.sleep(4)
            await ctx.send('owo slots 3000')
            await asyncio.sleep(16)
            await asyncio.sleep(3)
            await ctx.send('owo h')
            await asyncio.sleep(2)
            await ctx.send('owo b')
            await asyncio.sleep(4)
            await ctx.send('owo flip 3000')
            await asyncio.sleep(16)
            await ctx.send('owo h')
            await asyncio.sleep(2)
            await ctx.send('owo b')
            await asyncio.sleep(4)
            await ctx.send('owo slots 3000')
            await asyncio.sleep(16)
            await asyncio.sleep(3)
            await ctx.send('owo h')
            await asyncio.sleep(2)
            await ctx.send('owo b')
            await asyncio.sleep(4)
            await ctx.send('owo flip 3000')
            await asyncio.sleep(16)
            await ctx.send('owo h')
            await asyncio.sleep(2)
            await ctx.send('owo b')
            await asyncio.sleep(4)
            await ctx.send('owo slots 3000')
            await asyncio.sleep(16)
            await asyncio.sleep(3)
            await ctx.send('owo h')
            await asyncio.sleep(2)
            await ctx.send('owo b')
            await asyncio.sleep(4)
            await ctx.send('owo flip 3000')
            await asyncio.sleep(16)
            await ctx.send('owo h')
            await asyncio.sleep(2)
            await ctx.send('owo b')
            await asyncio.sleep(4)
            await ctx.send('owo slots 3000')
            await asyncio.sleep(16)
            await asyncio.sleep(3)
            await ctx.send('owo h')
            await asyncio.sleep(2)
            await ctx.send('owo b')
            await asyncio.sleep(4)
            await ctx.send('owo flip 3000')
            await asyncio.sleep(16)
            await ctx.send('owo h')
            await asyncio.sleep(2)
            await ctx.send('owo b')
            await asyncio.sleep(4)
            await ctx.send('owo slots 3000')
            await asyncio.sleep(16)
            await asyncio.sleep(3)
            await ctx.send('owo h')
            await asyncio.sleep(2)
            await ctx.send('owo b')
            await asyncio.sleep(4)
            await ctx.send('owo flip 3000')
            await asyncio.sleep(16)
            print('break for 30 mins')
            await asyncio.sleep(1800)
            await ctx.send('owo h')
            await asyncio.sleep(2)
            await ctx.send('owo b')
            await asyncio.sleep(4)
            await ctx.send('owo slots 3000')
            await asyncio.sleep(16)
            await asyncio.sleep(3)
            await ctx.send('owo h')
            await asyncio.sleep(2)
            await ctx.send('owo b')
            await asyncio.sleep(4)
            await ctx.send('owo flip 3000')
            await asyncio.sleep(16)
            await ctx.send('owo h')
            await asyncio.sleep(2)
            await ctx.send('owo b')
            await asyncio.sleep(4)
            await ctx.send('owo slots 3000')
            await asyncio.sleep(16)
            await asyncio.sleep(3)
            await ctx.send('owo h')
            await asyncio.sleep(2)
            await ctx.send('owo b')
            await asyncio.sleep(4)
            await ctx.send('owo flip 3000')
            await asyncio.sleep(16)
            await ctx.send('owo h')
            await asyncio.sleep(2)
            await ctx.send('owo b')
            await asyncio.sleep(4)
            await ctx.send('owo slots 3000')
            await asyncio.sleep(16)
            await asyncio.sleep(3)
            await ctx.send('owo h')
            await asyncio.sleep(2)
            await ctx.send('owo b')
            await asyncio.sleep(4)
            await ctx.send('owo flip 3000')
            await asyncio.sleep(16)
            await ctx.send('owo h')
            await asyncio.sleep(2)
            await ctx.send('owo b')
            await asyncio.sleep(4)
            await ctx.send('owo slots 3000')
            await asyncio.sleep(16)
            await asyncio.sleep(3)
            await ctx.send('owo h')
            await asyncio.sleep(2)
            await ctx.send('owo b')
            await asyncio.sleep(4)
            await ctx.send('owo flip 3000')
            await asyncio.sleep(16)
            await ctx.send('owo h')
            await asyncio.sleep(2)
            await ctx.send('owo b')
            await asyncio.sleep(4)
            await ctx.send('owo slots 3000')
            await asyncio.sleep(16)
            await asyncio.sleep(3)
            await ctx.send('owo h')
            await asyncio.sleep(2)
            await ctx.send('owo b')
            await asyncio.sleep(4)
            await ctx.send('owo flip 3000')
            await asyncio.sleep(16)
            await ctx.send('owo h')
            await asyncio.sleep(2)
            await ctx.send('owo b')
            await asyncio.sleep(4)
            await ctx.send('owo slots 3000')
            await asyncio.sleep(16)
            await asyncio.sleep(3)
            await ctx.send('owo h')
            await asyncio.sleep(2)
            await ctx.send('owo b')
            await asyncio.sleep(4)
            await ctx.send('owo flip 3000')
            await asyncio.sleep(16)
            await ctx.send('owo h')
            await asyncio.sleep(2)
            await ctx.send('owo b')
            await asyncio.sleep(4)
            await ctx.send('owo slots 3000')
            await asyncio.sleep(16)
            await asyncio.sleep(3)
            await ctx.send('owo h')
            await asyncio.sleep(2)
            await ctx.send('owo b')
            await asyncio.sleep(4)
            await ctx.send('owo flip 3000')
            await asyncio.sleep(16)
            await ctx.send('owo h')
            await asyncio.sleep(2)
            await ctx.send('owo b')
            await asyncio.sleep(4)
            await ctx.send('owo slots 3000')
            await asyncio.sleep(16)
            await asyncio.sleep(3)
            await ctx.send('owo h')
            await asyncio.sleep(2)
            await ctx.send('owo b')
            await asyncio.sleep(4)
            await ctx.send('owo flip 3000')
            await asyncio.sleep(16)
            await ctx.send('owo h')
            await asyncio.sleep(2)
            await ctx.send('owo b')
            await asyncio.sleep(4)
            await ctx.send('owo slots 3000')
            await asyncio.sleep(16)
            await asyncio.sleep(3)
            await ctx.send('owo h')
            await asyncio.sleep(2)
            await ctx.send('owo b')
            await asyncio.sleep(4)
            await ctx.send('owo flip 3000')
            await asyncio.sleep(16)
            await ctx.send('owo h')
            await asyncio.sleep(2)
            await ctx.send('owo b')
            await asyncio.sleep(4)
            await ctx.send('owo slots 3000')
            await asyncio.sleep(16)
            await asyncio.sleep(3)
            await ctx.send('owo h')
            await asyncio.sleep(2)
            await ctx.send('owo b')
            await asyncio.sleep(4)
            await ctx.send('owo flip 3000')
            await asyncio.sleep(16)
            await ctx.send('owo h')
            await asyncio.sleep(2)
            await ctx.send('owo b')
            await asyncio.sleep(4)
            await ctx.send('owo slots 3000')
            await asyncio.sleep(16)
            await asyncio.sleep(3)
            await ctx.send('owo h')
            await asyncio.sleep(2)
            await ctx.send('owo b')
            print('break for 30 mins')
            await asyncio.sleep(1800)
            await asyncio.sleep(4)
            await ctx.send('owo flip 3000')
            await asyncio.sleep(16)
            await ctx.send('owo h')
            await asyncio.sleep(2)
            await ctx.send('owo b')
            await asyncio.sleep(4)
            await ctx.send('owo slots 3000')
            await asyncio.sleep(16)
            await asyncio.sleep(3)
            await ctx.send('owo h')
            await asyncio.sleep(2)
            await ctx.send('owo b')
            await asyncio.sleep(4)
            await ctx.send('owo flip 3000')
            await asyncio.sleep(16)
            await ctx.send('owo h')
            await asyncio.sleep(2)
            await ctx.send('owo b')
            await asyncio.sleep(4)
            await ctx.send('owo slots 3000')
            await asyncio.sleep(16)
            await asyncio.sleep(3)
            await ctx.send('owo h')
            await asyncio.sleep(2)
            await ctx.send('owo b')
            await asyncio.sleep(4)
            await ctx.send('owo flip 3000')
            await asyncio.sleep(16)
            await ctx.send('owo h')
            await asyncio.sleep(2)
            await ctx.send('owo b')
            await asyncio.sleep(4)
            await ctx.send('owo slots 3000')
            await asyncio.sleep(16)
            await asyncio.sleep(3)
            await ctx.send('owo h')
            await asyncio.sleep(2)
            await ctx.send('owo b')
            await asyncio.sleep(4)
            await ctx.send('owo flip 3000')
            await asyncio.sleep(16)
            await ctx.send('owo h')
            await asyncio.sleep(2)
            await ctx.send('owo b')
            await asyncio.sleep(4)
            await ctx.send('owo slots 3000')
            await asyncio.sleep(16)
            print('break for 1 hour 30 min')
            await asyncio.sleep(5400)


bot.run(os.getenv('token'), bot=False)
