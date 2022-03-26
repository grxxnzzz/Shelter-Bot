import discord
import characterGen

client = discord.Client()

@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$id'):
        name = message.author
        await message.channel.send('твой id: {0}'.format(name))

    if message.content.startswith('$ген'):
        await message.author.send(characterGen.characterCreation())
    
    if message.content.startswith('$hello'):
        await message.channel.send('дарова')

client.run('OTU3MjUzMTU1OTEyMDU2ODgy.Yj8FeQ.EVQYUILUGnWYTqX0vOkGs3uJyP0')