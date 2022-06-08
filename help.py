# Extension which handles the help command

from pydoc import describe
import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

# Defines
load_dotenv('variables.env')

# Variables
channel_bot_id = int(os.getenv('CHANNEL_BOT_ID'))

# Define class
class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Message on startup
    @commands.Cog.listener()
    async def on_ready(self):
        print('help running...')
        print('--------------------')

    # Handle Support command
    @commands.command()
    async def liftyhelp(self, ctx):
        if ctx.channel.id != channel_bot_id:
            await ctx.message.delete()
        elif ctx.channel.id == channel_bot_id:
            await ctx.channel.purge()
            # Embed
            embed = discord.Embed(title = 'Lifty Befehlsübersicht', description = 'Hier findest du eine Übersicht meiner Befehle!', color = discord.Color.from_rgb(218, 169, 0))
            
            embed.set_thumbnail(url = 'https://i.imgur.com/oRGuHnZ.png')

            embed.add_field(name = 'Support', value = '!support / Ich erstelle einen Privaten Kanal um dich bei Fragen rund um unsere Orga oder den Discord zu unterstützen.', inline = False)
            embed.add_field(name = 'Diplomatie', value = '!diplo / Ich erstelle einen Privaten Kanal um dich bei Diplomatischen Anfragen zu unterstützen.', inline = False)
            embed.add_field(name = 'Bewerbung', value = '!appliance / Ich erstelle einen Privaten Kanal für deine Bewerbung.', inline = False)
            
            embed.set_footer(text = 'Meine Befehle können nur in diesem Kanal genutzt werden!')

            await ctx.send(embed = embed)

# Define extension
def setup(bot):
    bot.add_cog(help(bot))