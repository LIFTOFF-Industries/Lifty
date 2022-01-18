import discord
import os
from discord.ext import commands

# Defines
intents = discord.Intents.default()
intents.members = True
intents.reactions = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Message on startup
@bot.event
async def on_ready():
    print('Bot running...')
    print('Name: {0.user}'.format(bot))
    print('ID: {0.user.id}'.format(bot))
    print('--------------------')
    await bot.change_presence(activity=discord.Game("LiftOff Industries"))

# Load Extensions
bot.load_extension('entry')
bot.load_extension('roles')

bot.run('ODMzNDI5OTA0NzYyMDc3MjA2.YHyOFQ.7gJHZ_fJUHIt4rVaLnqypwsGv_g')