# Extension which handles the join of new Users

import discord
from discord.ext import commands

# Define class
class entry(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Events
    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(member)
        await member.send('Hallo!')

# define extension
def setup(bot):
    bot.add_cog(entry(bot))