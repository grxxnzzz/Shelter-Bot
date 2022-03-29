from multiprocessing.connection import Client
from time import sleep
import discord
import characterGen
import cataclysmGen

client = discord.Client()

@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
     
    if message.content.startswith('$перс'):
        await message.author.send(f'Твой персонаж, {message.author} !\n–----------------–\n' + characterGen.characterCreation() +    '\n–----------------–\n')
        name = message.author
        print(f'user {name} generated a character!')

    if message.content.startswith('$ген 3'):
        await message.author.send(f'Твои персонажи, {message.author}!\n№1\n–----------------–\n' + characterGen.characterCreation() + '\n–----------------–\n')
        await message.author.send('\n№2\n–----------------–\n' + characterGen.characterCreation() + '\n–----------------–\n')
        await message.author.send('\n№3\n–----------------–\n' + characterGen.characterCreation() + '\n–----------------–\n')
        name = message.author
        print(f'user {name} generated 3 characters!')

    if message.content.startswith('$ген 10'):
        await message.author.send(f'Твои персонажи, {message.author}!\n№1\n–----------------–\n' + characterGen.characterCreation() + '\n–----------------–\n')
        for i in range(2, 11):
            sleep(0.5)
            await message.author.send(f'\n№{i}\n–----------------–\n' + characterGen.characterCreation() + '\n–----------------–\n')
        name = message.author
        print(f'user {name} generated 10 characters!')

    if message.content.startswith('$катабункер'):
        await message.channel.send(cataclysmGen.cataclysmPlusBunker())
        await message.channel.send(cataclysmGen.bunkerCreation())

    #if message.content.startswith('$hello'):
    #    await message.channel.send('дарова')
    
    #if message.content.startswith('$id'):
    #    name = message.author
    #    await message.channel.send('твой id: {0}'.format(name))

client.run('OTU3MjUzMTU1OTEyMDU2ODgy.Yj8FeQ.EVQYUILUGnWYTqX0vOkGs3uJyP0')
