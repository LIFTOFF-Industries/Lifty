# Extension which handles the roles for new Users

import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

# Defines
load_dotenv('variables.env')

# Variables
rule_channel_id = os.getenv('RULE_CHANNEL_ID')
rule_message_id = int(os.getenv('RULE_MESSAGE_ID'))
role_friends_id = int(os.getenv('ROLE_FRIENDS_ID'))

# Define class
class roles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Message on startup
    @commands.Cog.listener()
    async def on_ready(self):
        print('roles running...')
        print('--------------------')
        channel = await self.bot.fetch_channel(rule_channel_id)
        message = await channel.fetch_message(rule_message_id)
        await message.add_reaction('\N{WHITE HEAVY CHECK MARK}')

    # Events
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, event):
        print('Member {0.member} reacted on message {0.message_id} with {0.emoji.name}.'.format(event))
        if event.emoji.name == '\N{WHITE HEAVY CHECK MARK}' and event.message_id == rule_message_id and event.member != self.bot.user:
            print('{0.member} getting friends role'.format(event))
            role = event.member.guild.get_role(role_friends_id)
            await event.member.add_roles(role)
            channel = await self.bot.fetch_channel(event.channel_id)
            message = await channel.fetch_message(event.message_id)
            await message.remove_reaction(event.emoji, event.member)


# define extension
def setup(bot):
    bot.add_cog(roles(bot))