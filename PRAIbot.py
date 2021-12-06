# BY ADU and AKOE - 06/12/21
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
helpmsg = "Aide pour les gens perdus :\n\
```\
!prai               # Calls PRAI\n\
!prai force         # Mentions PRAI in case of emergency\n\
!prai broadcast     # In case of ULTIMATE emergency \n\
!prai voice         # Send a voice file\n\
!prai version       # Prints the version of the bot\n\
!prai stats         # Returns the bot usage counter\n\
!prai help          # Prints this help message\n\
```"

# Is printed when !prai version is called
versionmsg = "Bot: PRAIbot - Version 1.2\nAuthor: ADU\nPython version: 3.9.2\nOS: Debian 11 Bullseye (amd64)\nHypervisor: ESXi 6.7U3"

# Function to increment the usage counter by one
def appendToFile(cntr):
    open('count.txt', 'w').close()
    with open('count.txt', 'a') as f:
        cntr += 1
        f.write(str(cntr))
        f.close()

client = discord.Client()

@bot.event
async def on_ready():
    print(f'Logged in as: {bot.user.name}')
    print(f'With ID: {bot.user.id}')

@bot.command()
async def prai(ctx, param: str=None):
    # Read the daily counter
    with open('count.txt', 'r+') as f:
        cntr = f.readline()
        f.close()
    # This is checking if the parameter is given or not
    if (param is None):
        appendToFile(int(cntr)) # Increment the usage counter
        await ctx.send('**PRAI**')
        return
    else:
        param = param.lower()
        if (param == 'help'):
            # If the parameter is 'help', then send the help guide
            await ctx.send(helpmsg)
            return
        elif (param == 'broadcast'):
            # If the parameter is 'help', then send the help guide
            appendToFile(int(cntr)) # Increment the usage counter
            await ctx.send('**PRAI** <@&915525095835967519>')
            return
        elif (param == 'force'):
            # If the parameter is 'force', then mention PRAI
            appendToFile(int(cntr)) # Increment the usage counter
            await ctx.send('**PRAI** <@131170813444358144>')
            return
        elif (param == 'version'):
            # If the parameter is 'version', send information about the bot
            await ctx.send(versionmsg)
            return
        elif (param == 'stats'):
            # If the parameter is 'stats', then return the counter
            await ctx.send(f"Le bot a été utilisé : {str(cntr)} fois aujourd'hui.")
            return
        elif (param == 'voice'):
            # If the parameter is 'voice', send a voice file
            appendToFile(int(cntr)) # Increment the usage counter
            with open('prai.flac', 'rb') as f:
                audio = discord.File(f)
            await ctx.send(file = audio)
            return
        else:
            # If parameter is not recognized
            await ctx.send('**PRAI** perdu, merci de réessayer. *#PRAYforPRAI*')
            return
            
bot.run(TOKEN)
