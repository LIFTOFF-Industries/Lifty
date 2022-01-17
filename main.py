import discord

# Discord client
client = discord.Client()

# Message on startup
@client.event
async def on_ready():
    print('Eingeloggt als {0.user}'.format(client))

#bot.load_extension(entry)

client.run('Token')