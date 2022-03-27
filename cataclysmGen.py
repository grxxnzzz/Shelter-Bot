import random

cataclysms = ()

cataclysmsFile = open('cataclysms.txt', 'r', encoding="utf-8")
for i in cataclysmsFile:
    cataclysms = i.split("$")
cataclysmsFile.close()

for i in range(0, len(cataclysms)):
    print(cataclysms[i], end='\n\n')

print(len(cataclysms))

bunkerInventoryFile = open('bunkerInventory.txt', 'r', encoding="utf-8")
for i in bunkerInventoryFile:
    bunkerInventoryTuple = i.split("$")
bunkerInventoryFile.close()


def bunkerCreation():
    
    bunkerConditionTuple = ("хорошем", "плохом", "нормальном", "плачевном", "отличном", "ужасном")
    bunkerDefenseTuple = ('достаточно защищено', "недостаточно защищено", "недостаточно защищено и, при желании, **враждебные существа и другиевыжившие** могут попасть внутрь**", "отлично защищено, *местоположениескрыто*", "отлично защищено, но **местоположение известно другимвыжившим**", "защищено","надёжно","ненадёжно", "находится в прекрасномсостоянии, *надежно спрятано* и хорошо защищено внутри отнедоброжелателей *защитно-герметическими дверями*.")
    bunkerLifeSysTuple = ('в исправности', "не исправны")
    bunkerAutonomyTuple = ('работают в автономном режиме', "не работают вавтономном режиме")
    bunkerRefuseTuple = ('но в любой момент могут отказать', "и не откажут вработе", "и имеют небольшой шанс на поломку")
    bunkerRepairTuple = ('Все схемы и документация о починке механизмовприсутствуют', "Схемы и документация о починке отсутствуют")
    
    bunkerArea = int(random.triangular(20, 1000, 240))
    
    bunkerCondition = random.choices(bunkerConditionTuple, weights=(5,10, 10, 3, 1, 1))
    bunkerCondition = str(bunkerCondition[0])

    #bunkerDefense = str(random.choices(bunkerDefenseTuple, weights=()))
    #bunkerDefense = str(bunkerDefense[0])

    bunkerDefense = str(random.choice(bunkerDefenseTuple))

    bunkerLifeSys = random.choices(bunkerLifeSysTuple, weights=(75, 25), k=1)
    bunkerLifeSys = str(bunkerLifeSys[0])

    bunkerAutonomy = random.choices(bunkerAutonomyTuple, weights=(75, 25), k=1)
    bunkerAutonomy = str(bunkerAutonomy[0])

    bunkerRefuse = random.choices(bunkerRefuseTuple, weights=(50, 10, 90), k=1)
    bunkerRefuse = str(bunkerRefuse[0])

    bunkerRepair = random.choices(bunkerRepairTuple, weights=(25, 75), k=1)
    bunkerRepair = str(bunkerRepair[0])

    bunkerInventory = str(random.choice(bunkerInventoryTuple))

    createdBunkerPool = [f'Площадь убежища: {bunkerArea}м²\n', 
    f'Убежище находится в {bunkerCondition} состоянии, {bunkerDefense}. ', 
    f'Системы жизнеобеспечения {bunkerLifeSys} и {bunkerAutonomy}, {bunkerRefuse}. {bunkerRepair}.\n' 
    f':package: В бункере есть: {bunkerInventory}.']

    createdBunker = ''

    for i in createdBunkerPool:
       createdBunker = createdBunker + i

    return createdBunker

# shelter + cataclysm creation start
def cataclysmPlusBunker():

    cataBunkerCreation = ''
    cataclysm = str(random.choice(cataclysms))
    remainedPopulation = str(random.randint(5, 90))
    destructedSurface = str(random.randint(1, 90))

    cataBunkerCreationPool = (f'**Катаклизм:**\n{cataclysm}\n', f':busts_in_silhouette: **Остаток населения:** {remainedPopulation}%', f':boom: **Разрушения на поверхности:** {destructedSurface}%\n')

    # finishing shelter + cataclysm creation
    for i in cataBunkerCreationPool:
        cataBunkerCreation = cataBunkerCreation + i + '\n'

    return cataBunkerCreation