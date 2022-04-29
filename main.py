import time
import discord
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
    username = message.author
    
    ### bot not reacting on itself messages
    if message.author == bot.user:
        return

    ### explaining rules
    if message.content.startswith('$правила'):
        if message.channel.id == shelter_Сhannel.id:
            await shelter_Сhannel.send(instructions.Rules(username))
        else:
            await message.channel.send(f'{username.mention}, Вы просите правила не в том канале. Пожалуйста, перейдите в #{shelter_Сhannel}')


    ### character creation 
    if message.content.startswith('$перс'):
        realDate = time.localtime(time.time())

        await username.send(f'Твой персонаж, {username.mention}! {characterGen.characterCreation()}')
        await shelter_Сhannel.send(f'{username.mention} создал персонажа!')

        print(f'{username} • has generated a character! [{realDate.tm_hour}:{realDate.tm_min}:{realDate.tm_sec}]\n')

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

bot.run('OTU3MjUzMTU1OTEyMDU2ODgy.Yj8FeQ.EVQYUILUGnWYTqX0vOkGs3uJyP0')

