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
    #if message.content.startswith('$id'):
    #    name = message.author
    #    await message.channel.send('твой id: {0}'.format(name))
    
    if message.content.startswith('$перс'):
        await message.author.send(f'Твой персонаж, {message.author} !\n–----------------–\n' + characterGen.characterCreation() +    '\n–----------------–\n')

    #async for message in client.channel(957366792400011264).history(limit=10):
    #    if message.content.startswith('$перс'):
    #        message_id = message.id
    #        await message.author.send(f'Твой персонаж, {message.author} !\n–----------------–\n' + characterGen.characterCreation() + '\n–----------------–\n')
    #else:
    #     await message.author.send('Команда отправлена не в тот канал! Перейди в #🧯бункер-бот')
    #     message_bot_id = message.id
    #     sleep(5)
    #     await message.delete(message_id)
    #     await message.delete(message_bot_id)

    if message.content.startswith('$ген 3'):
        await message.author.send(f'Твои персонажи, {message.author}!\n№1\n–----------------–\n' + characterGen.characterCreation() + '\n–----------------–\n')
        await message.author.send('\n№2\n–----------------–\n' + characterGen.characterCreation() + '\n–----------------–\n')
        await message.author.send('\n№3\n–----------------–\n' + characterGen.characterCreation() + '\n–----------------–\n')

    if message.content.startswith('$ген 10'):
        await message.author.send(f'Твои персонажи, {message.author}!\n№1\n–----------------–\n' + characterGen.characterCreation() + '\n–----------------–\n')
        for i in range(2, 11):
            sleep(0.5)
            await message.author.send(f'\n№{i}\n–----------------–\n' + characterGen.characterCreation() + '\n–----------------–\n')
            

    if message.content.startswith('$hello'):
        await message.channel.send('дарова')

client.run('OTU3MjUzMTU1OTEyMDU2ODgy.Yj8FeQ.EVQYUILUGnWYTqX0vOkGs3uJyP0')
