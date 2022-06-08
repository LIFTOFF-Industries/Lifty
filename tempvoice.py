# Extension which handles the roles for new Users

import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

# Defines
load_dotenv('variables.env')

# Variables
voice_channel_id = int(os.getenv('CHANNEL_VOICE_ID'))
stream_voice_channel_id = int(os.getenv('CHANNEL_VOICESTREAM_ID'))

# Define class
class tempvoice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Message on startup
    @commands.Cog.listener()
    async def on_ready(self):
        print('tempvoice running...')
        print('--------------------')

    # Events
    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if after.channel != None:
            
            # Temp voice
            if after.channel.id == voice_channel_id:
                print('{0} joined {1.channel}'.format(member, after))
                voice = await member.guild.create_voice_channel(name = member.name + "'s voice", category = after.channel.category, bitrate = after.channel.bitrate)
                await voice.set_permissions(member, connect = True, mute_members = True, move_members = True, manage_channels = True)
                await member.move_to(channel = voice)
                print('Tempvoice "{0}" created and {1} moved'.format(voice, member))

                def check(x, y, z):
                    return len(voice.members) == 0
                await self.bot.wait_for('voice_state_update', check = check)
                await voice.delete()
                print('Tempvoice "{0}" deleted'.format(voice))

            # Stream temp voice
            if after.channel.id == stream_voice_channel_id:
                print('{0} joined {1.channel}'.format(member, after))
                voice = await member.guild.create_voice_channel(name = member.name + "'s stream", category = after.channel.category, bitrate = after.channel.bitrate)
                await voice.set_permissions(member, connect = True, mute_members = True, move_members = True, manage_channels = True)
                await member.move_to(channel = voice)
                print('Stream tempvoice "{0}" created and {1} moved'.format(voice, member))

                def check(x, y, z):
                    return len(voice.members) == 0
                await self.bot.wait_for('voice_state_update', check = check)
                await voice.delete()
                print('Stream tempvoice "{0}" deleted'.format(voice))
        
# define extension
def setup(bot):
    bot.add_cog(tempvoice(bot))
