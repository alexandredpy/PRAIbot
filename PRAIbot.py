# BY ADU - 28/11/21
# Licence : CC-BY-NC-SA

import discord
from discord.ext.commands.bot import Bot
from discord.ext import commands

with open('BotToken.txt', 'r') as f:
    TOKEN = f.readline()
    f.close()

PREFIX = '!'
INTENTS = discord.Intents.default()
bot = commands.Bot(command_prefix=PREFIX, intents=INTENTS, case_insensitive=True) #case_insensitive to fix caps issue

# Is printed when !prai help is called
helpmsg = "Aide pour la version française :\
```\
!prai   # Calls PRAI\
```"

# Is printed when !prai version is called
versionmsg = "Bot: PRAIbot - Version 1.0\nPython version: 3.9.2\nOS: Debian 11 Bullseye (amd64)\nHypervisor: ESXi 6.7U3"

client = discord.Client()

@bot.event
async def on_ready():
    print(f'Logged in as: {bot.user.name}')
    print(f'With ID: {bot.user.id}')

@bot.command()
async def prai(ctx, param: str=None):
    # This is checking if the parameter is given or not
    if (param is None):
        await ctx.send("PRAI")
        return
    else:
        param = param.lower()
        if (param == 'help'):
            await ctx.send(helpmsg)
            return
        if (param == 'force'):
            await ctx.send('PRAI @<131170813444358144>')
            return
        if (param == 'version'):
            # If the parameter is 'version', send information about the bot
            await ctx.send(versionmsg)
            return

bot.run(TOKEN)
