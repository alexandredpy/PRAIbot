# By ADU and AKOE - 03/02/22
# Licence : CC-BY-NC-SA

#### IMPORTS ####
import discord
from discord.ext.commands.bot import Bot
from discord.ext import commands
import datetime
from blagues_api import BlaguesAPI
#################

#### TOKENS ####
# Get the Discord bot TOKEN
with open('BotToken.txt', 'r') as f:
    TOKEN = f.readline()
    f.close()

# Get the blague API TOKEN
with open('BlagueToken.txt', 'r') as f:
    TOKENBLAGUE = f.readline()
    f.close()
#################

#### Init ####
PREFIX = '!'
INTENTS = discord.Intents.default()
bot = commands.Bot(command_prefix=PREFIX, intents=INTENTS, case_insensitive=True) # case_insensitive to fix caps issue
blagues = BlaguesAPI(TOKENBLAGUE) # Blague API init
client = discord.Client()
jacky = True # Boolean to control Jacky usage
#################

# Is printed when !prai help is called
helpmsg = "Aide pour les gens perdus :\n\
```\
!prai               # Calls PRAI\n\
!prai force         # Mentions PRAI in case of emergency\n\
!prai broadcast     # In case of ULTIMATE emergency \n\
!prai voice         # Send a voice file\n\
!prai xplosion      # Reads PRAI with TTS\n\
!prai joke          # Tells a random funny joke\n\
!prai status        # Returns the current activity of PRAI\n\
!prai version       # Prints the version of the bot\n\
!prai stats         # Returns the bot usage counter\n\
!prai help          # Prints this help message\n\
```"

# Is printed when !prai version is called
versionmsg = "Bot: PRAIbot - Version 1.6\nAuthor: ADU\nPython version: 3.9.2\nOS: Debian 11 Bullseye (amd64)\nHypervisor: ESXi 6.7U3"

#### Functions ####
# Function to increment the usage counter by one
def appendToFile(cntr):
    open('count.txt', 'w').close()
    with open('count.txt', 'a') as f:
        cntr += 1
        f.write(str(cntr))
        f.close()

# Function to check btw 2 times (for prai status)
def time_in_range(start, end, current):
    return start <= current <= end
#################

@bot.event
async def on_ready():
    print(f'Logged in as: {bot.user.name}')
    print(f'With ID: {bot.user.id}')

@bot.command(pass_context = True)
async def prai(ctx, param: str=None):
    global jacky # Make the jacky variable global

    # Read the daily counter
    with open('count.txt', 'r+') as f:
        cntr = f.readline()
        f.close()

    # For admin purposes only
    if (ctx.message.author.id == 299572932307582976 and jacky == False):
        return
    
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
            await ctx.send(f"Le bot a d??j?? cri?? **PRAI** {str(cntr)} fois dans sa vie")
            return
        elif (param == 'xplosion'):
            # If the parameter is 'xplosion', the read the msg with TTSs
            appendToFile(int(cntr)) # Increment the usage counter
            await ctx.send("p??rai", tts=True)
            return
        elif (param == 'joke'):
            # If the parameter is 'joke', return a random joke
            appendToFile(int(cntr)) # Increment the usage counter
            blague = await blagues.random()
            await ctx.send(blague.joke) # Send the joke
            await ctx.send(f"||{blague.answer}||") # Send the answer
            return
        elif (param == 'voice'):
            # If the parameter is 'voice', send a voice file
            appendToFile(int(cntr)) # Increment the usage counter
            with open('prai.flac', 'rb') as f:
                audio = discord.File(f)
            await ctx.send(file = audio)
            return
        elif (param == 'jacky'):
            # For admin usage only 
            if (ctx.message.author.id == 151379424967786496 or ctx.message.author.id == 316317238103769089): # if Alex or Alois
                jacky = not jacky # Invert the jacky bool
                await ctx.send(":white_check_mark:")
                return
            await ctx.send("Vous n'??tes pas autoris?? ?? utiliser cette commande.") # If not admin
            return
        elif (param == 'status'):
            # If the parameter is 'status', then return the status
            appendToFile(int(cntr)) # Increment the usage counter
            now = datetime.datetime.now().time() # Get current time
            if (time_in_range(datetime.time(21, 30, 0), datetime.time(23, 59, 59), now)):
                await ctx.send('**PRAI** fait dodo :zzz:')
                return
            elif (time_in_range(datetime.time(0, 0, 0), datetime.time(7, 0, 0), now)):
                await ctx.send('**PRAI** fait dodo :zzz:')
                return
            elif (time_in_range(datetime.time(7, 0, 0), datetime.time(10, 0, 0), now)):
                await ctx.send('**PRAI** fait ses petites emplettes :basket:')
                return
            elif (time_in_range(datetime.time(10, 0, 0), datetime.time(11, 45, 0), now)):
                await ctx.send('**PRAI** regarde la TV :tv: #Motus')
                return
            elif (time_in_range(datetime.time(11, 45, 0), datetime.time(14, 15, 0), now)):
                await ctx.send('**PRAI** mange :hamburger:')
                return
            elif (time_in_range(datetime.time(14, 15, 0), datetime.time(16, 30, 0), now)):
                await ctx.send('**PRAI** fait la sieste :zzz:')
                return
            elif (time_in_range(datetime.time(16, 30, 0), datetime.time(17, 00, 0), now)):
                await ctx.send('**PRAI** fait un test PCR :microbe:')
                return
            elif (time_in_range(datetime.time(17, 00, 0), datetime.time(18, 30, 0), now)):
                await ctx.send('**PRAI** fait des mots crois??s :pencil:')
                return
            elif (time_in_range(datetime.time(18, 30, 0), datetime.time(21, 30, 0), now)):
                await ctx.send('**PRAI** prends le souper :ramen:')
                return
            return
        else:
            # If parameter is not recognized
            with open('prai-perdu.jpg', 'rb') as f:
                picture = discord.File(f)
                await ctx.send(f'**PRAI** perdu, merci de r??essayer. *#PRAYforPRAI*', file = picture)
                return
            
bot.run(TOKEN)
