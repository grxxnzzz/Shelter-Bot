import characterGen
import cataclysmGen

# print multiple times for debug
#for i in range(1, 6):
#    print(f'#{i}\n' + characterGen.characterCreation())

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