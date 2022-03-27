import random

cataclysms = ()
bunker = ()

cataclysmsFile = open('cataclysms.txt', 'r', encoding="utf-8")
for i in cataclysmsFile:
    cataclysms = i.split("$")
cataclysmsFile.close()

bunkerFile = open('bunker.txt', 'r', encoding="utf-8")
for i in bunkerFile:
    bunker = i.split("$")
bunkerFile.close()

def cataclysmPlusBunker():
    cataBunkerCreation = ''
    
    return cataBunkerCreation