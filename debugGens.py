#import characterGen
#import cataclysmGen

#cards=tuple
#
#cardsFile = open('cards.txt', 'r', encoding="utf-8")
#cards = cardsFile.readlines()
#cardsFile.close()
#for i in range(len(cards)):
#    cards[i] = cards[i].rstrip('\n')

#print multiple times for debug
#for i in range(1, 6):
#    print(f'{i}\n' + characterGen.characterCreation())

# print multiple times catabunker for debug
#for i in range (1,6):
#    print(f'#{i}\n' + cataclysmGen.cataclysmPlusBunker())

#print(cataclysmGen.cataclysmPlusBunker(), cataclysmGen.bunkerCreation())

#for i in range(1, cataclysmGen.cataclysms):
#    print(cataclysmGen.cataclysms[i])

# manual chances enter
# sum = ''
# 
# for i in characterGen.traits:
#     abc = input(f"введи шансы на [{i}]: ")
#     sum = sum + ',' + abc
#     if abc=='':
#         print(sum)
#         break
# else:
#     print(sum)

# auto chances enter
# for i in range(len(characterGen.phobias)):
#     sum = str(sum) + '1, '
# else:
#     print(sum)
# print(len(characterGen.phobias))

#тест генерации бункера
#for i in range(1, 10):
#    print(f'бункер №{i}')
#    print(cataclysmGen.bunkerCreation())
#    print()

#if message.content.startswith('$ген 3'):
#    await message.author.send(f'Твои персонажи, {message.author}!\n№1\n–----------------–\n' + characterGen.characterCreation() + '\n–----------------–\n')
#    await message.author.send('\n№2\n–----------------–\n' + characterGen.characterCreation() + '\n–----------------–\n')
#    await message.author.send('\n№3\n–----------------–\n' + characterGen.characterCreation() + '\n–----------------–\n')
#    name = message.author
#    print(f'user {name} generated 3 characters!')

#if message.content.startswith('$ген 10'):
#    await message.author.send(f'Твои персонажи, {message.author}!\n№1\n–----------------–\n' + characterGen.characterCreation() + '\n–----------------–\n')
#    for i in range(2, 11):
#        sleep(0.5)
#        await message.author.send(f'\n№{i}\n–----------------–\n' + characterGen.characterCreation() + '\n–----------------–\n')
#    name = message.author
#    print(f'user {name} generated 10 characters!')
        
#if message.content.startswith('$hello'):
#    await message.channel.send('дарова')
    
#if message.content.startswith('$id'):
#    name = message.author
#    await message.channel.send('твой id: {0}'.format(name))


#@tree.command(guild = discord.Object(id = 477422164400930816), name='перс', description = 'Создаёт уникального персонажа для игры в Бункер')
#async def slash(interaction: discord.Interaction):
#    author = author.interaction
#    await interaction.response.send_message(f'Твой персонаж, {author}! {characterGen.characterCreation()}')
