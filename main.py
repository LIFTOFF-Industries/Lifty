import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

# Defines
intents = discord.Intents.default()
intents.members = True
intents.reactions = True
intents.voice_states = True
bot = commands.Bot(command_prefix='!', intents=intents)
load_dotenv('variablestest.env')

# Variables
token = os.getenv('DISCORD_TOKEN')

# Message on startup
@bot.event
async def on_ready():
    print('Bot running...')
    print('Name: {0.user}'.format(bot))
    print('ID: {0.user.id}'.format(bot))
    print('--------------------')
    await bot.change_presence(activity=discord.Game("LiftOff Industries"))

# Load Extensions
bot.load_extension('tempvoice')
bot.load_extension('support')
bot.load_extension('appliance')
bot.load_extension('diplo')
bot.load_extension('help')

bot.run(token)