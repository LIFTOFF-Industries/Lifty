# Extension which handles the join of new Users

import discord
from discord.ext import commands

# Define class
class entry(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Message on startup
    @commands.Cog.listener()
    async def on_ready(self):
        print('entry running...')
        print('--------------------')

    # Events
    @commands.Cog.listener()
    async def on_member_join(self, member):
        print('Member joined: {0}'.format(member))
        line1 = '**Herzlichen Willkommen auf dem Discord Server von LiftOff Industries {0.name}.**'.format(member)
        line2 = 'Um vollen Zugang zu unserem öffentlichen Bereich zu erhalten, musst du zuerst unsere Server Regeln akzeptieren.'
        line3 = 'Besuche dazu folgenden Channel <#841755767988289615>, lies dir die Regeln gemütlich durch und bestätige sie.'
        line4 = 'Lifty'
        await member.send(line1 + '\n\n' + line2 + '\n' + line3 + '\n\n' + line4)

# define extension
def setup(bot):
    bot.add_cog(entry(bot))