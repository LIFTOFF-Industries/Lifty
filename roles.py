# Extension which handles the roles for new Users

import discord
from discord.ext import commands

# Define class
class roles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Message on startup
    @commands.Cog.listener()
    async def on_ready(self):
        print('roles running...')
        print('--------------------')

    # Events
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, event):
        print('Member {0.member} reacted on message {0.message_id} with {0.emoji.name}.'.format(event))
        if event.emoji.name == '\N{WHITE HEAVY CHECK MARK}' and event.message_id == 841772436319109160:
            print('{0.member} getting friends role'.format(event))
            role = discord.utils.get(event.member.guild.roles, id = 841755767978852423)
            await event.member.add_roles(role)
        else:
            print('No action')


# define extension
def setup(bot):
    bot.add_cog(roles(bot))