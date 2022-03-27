import characterGen
import cataclysmGen

# print multiple times for debug
for i in range(0, 5):
    print(characterGen.characterCreation())

# manual chances enter
#sum = ''
#
#for i in characterGen.traits:
#    abc = input(f"введи шансы на [{i}]: ")
#    sum = sum + ',' + abc
#    if abc=='':
#        print(sum)
#        break
#else:
#    print(sum)