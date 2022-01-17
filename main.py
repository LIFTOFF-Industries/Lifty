import discord
import os
from discord.ext import commands

# Defines
intents = discord.Intents(members=True)
bot = commands.Bot(command_prefix='!', intents=intents)

# Message on startup
@bot.event
async def on_ready():
    print('Bot running...')
    print('Name: {0.user.name}'.format(bot))
    print('ID: {0.user.id}'.format(bot))
    print('--------------------')
    await bot.change_presence(activity=discord.Game("Making Money"))

# Load Extensions
bot.load_extension('entry')

bot.run('Token')