# Extension which handles the appliance commands

import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

# Defines
load_dotenv('variables.env')

# Variables
channel_bot_id = int(os.getenv('CHANNEL_BOT_ID'))
channel_ticket_id = int(os.getenv('CHANNEL_TICKET_ID'))
role_diplo_id = int(os.getenv('ROLE_DIPLO_ID'))
role_everyone_id = int(os.getenv('ROLE_EVERYONE_ID'))
role_md_id = int(os.getenv('ROLE_MD_ID'))
role_me_id = int(os.getenv('ROLE_ME_ID'))

# Define class
class appliance(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Message on startup
    @commands.Cog.listener()
    async def on_ready(self):
        print('appliance running...')
        print('--------------------')
    
    # Handle application command
    @commands.command()
    async def appliance(self, ctx):
        print('Member {0.author} wants to applicate.'.format(ctx))
        if ctx.channel.id != channel_bot_id:
            print('Wrong channel detected, command will be deleted.')
            await ctx.message.delete()
        elif ctx.channel.id == channel_bot_id:
            print('Appliance channel will be created.')
            await ctx.message.delete()
            support = await ctx.author.guild.create_text_channel(name = "Bewerbung-" + ctx.author.name, category = ctx.message.channel.category)
            role_everyone = ctx.author.guild.get_role(role_everyone_id)
            role_md = ctx.author.guild.get_role(role_md_id)
            role_me = ctx.author.guild.get_role(role_me_id)
            await support.set_permissions(role_everyone, read_messages = False, send_messages = False)
            await support.set_permissions(role_md, read_messages = True, send_messages = True)
            await support.set_permissions(role_me, read_messages = True, send_messages = True)
            await support.set_permissions(ctx.author, read_messages = True, send_messages = True, manage_channels = True)
            print('Channel {0} for appliance of {1} was created'.format(support, ctx.author))
            channel_ticket = ctx.author.guild.get_channel(channel_ticket_id)
            msg = 'Hallo LiftOff Management!\n\n{0.mention} hat eine Beitrittsanfrage in {1.mention} erstellt!'.format(ctx.author, support)
            await channel_ticket.send(msg)

# Define extension
def setup(bot):
    bot.add_cog(appliance(bot))