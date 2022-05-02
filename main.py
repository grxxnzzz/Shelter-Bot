import time
import discord
#import asyncio
import characterGen
import cataclysmGen
import instructions

bot = discord.Client()
#(guild = discord.Object(id = 477422164400930816))

@bot.event
async def on_ready():

    realDate = time.localtime(time.time())
    print(f'logged in as {bot.user} [{realDate.tm_hour}:{realDate.tm_min}:{realDate.tm_sec}]')
    
    global shelter_Сhannel
    shelter_Сhannel = bot.get_channel(957366792400011264)

@bot.event
async def on_message(message):
    
    global username
    
    ### bot not reacting on itself messages
    if message.author == bot.user:
        return

    ########################################################################

    ### explaining rules
    if message.content.startswith('$правила'):
        username = message.author
        if message.channel.id == shelter_Сhannel.id:
            await shelter_Сhannel.send(instructions.Rules(username))
        else:
            await message.channel.send(f'{username.mention}, Вы просите правила не в том канале. Пожалуйста, перейдите в #{shelter_Сhannel}')

    ########################################################################

    ### bot commands
    if message.content.startswith('$ком'):
        username = message.author
        if message.channel.id == shelter_Сhannel.id:
            await shelter_Сhannel.send(instructions.bot_Commands())
        else:
            await message.channel.send(f'{username.mention}, Вы не в том канале. Пожалуйста, перейдите в #{shelter_Сhannel}')

    ########################################################################


    ### character creation 
    if message.content.startswith('$перс'):
        username = message.author
        realDate = time.localtime(time.time())
        
        await username.send(f'Твой персонаж, {username.mention}! {characterGen.characterCreation(False)}')
        await shelter_Сhannel.send(f'{username.mention} создал персонажа!')

        print(f'{username} • has generated a character! [{realDate.tm_hour}:{realDate.tm_min}:{realDate.tm_sec}]\n')

    ########################################################################

    ### character creation • profession change
    if message.content.startswith('$проф'):
        username = message.author
        realDate = time.localtime(time.time())
        
        await username.send(f'Твоя новая профессия, {username.mention} --> {characterGen.characterCreation(True)}')
        await shelter_Сhannel.send(f'{username.mention} обновил профессию!')

        print(f'{username} • has updated the profession! [{realDate.tm_hour}:{realDate.tm_min}:{realDate.tm_sec}]\n')

    ########################################################################
    
    ### cataclysm+bunker creation
    if message.content.startswith('$катабункер'):

        await message.channel.send(cataclysmGen.cataclysmPlusBunker())
        await message.channel.send(cataclysmGen.bunkerCreation())

    ########################################################################
    
    ### cataclysm creation
    if message.content.startswith('$катаклизм'):

        await message.channel.send(cataclysmGen.cataclysmPlusBunker())

    ########################################################################

    ### bunker creation    
    if message.content.startswith('$бункер'):

        await message.channel.send(cataclysmGen.bunkerCreation())

    ########################################################################

    ### debug purposes
    #if message.content.startswith('$debug'):
    #    username = message.author
    #    for i in range (0,10):
    #        await username.send(f'№{i+1}{characterGen.characterCreation()}')
    #        await asyncio.sleep(1)
    
    ########################################################################

bot.run('OTU3MjUzMTU1OTEyMDU2ODgy.Yj8FeQ.EVQYUILUGnWYTqX0vOkGs3uJyP0')

