import random

cataclysms = ()

cataclysmsFile = open('cataclysms.txt', 'r', encoding="utf-8")
for i in cataclysmsFile:
    cataclysms = i.split("$")
cataclysmsFile.close()

bunkerInventoryFile = open('bunkerInventory.txt', 'r', encoding="utf-8")
bunkerInventoryTuple = bunkerInventoryFile.readlines()
bunkerInventoryFile.close()
for i in range(len(bunkerInventoryTuple)):
    bunkerInventoryTuple[i] = bunkerInventoryTuple[i].rstrip('\n')


def bunkerCreation():
    
    bunkerConditionTuple = ("хорошем", "плохом", "сносном", "кое-как пригодном", "отличном", "ужасном")
    bunkerDefenseTuple = ('достаточно защищено', "недостаточно защищено", "недостаточно защищено и, при желании, **враждебные существа и другие выжившие могут попасть внутрь**", "отлично защищено, *местоположение скрыто*", "отлично защищено, но **местоположение известно другим выжившим**", "защищено","надёжно","ненадёжно", "находится в прекрасном состоянии, *надежно спрятано* и хорошо защищено внутри от недоброжелателей *защитно-герметическими дверями*.")
    bunkerLifeSysTuple = ('в исправности', "не исправны")
    bunkerAutonomyTuple = ('работают в автономном режиме', "не работают в автономном режиме")
    bunkerRefuseTuple = ('в любой момент могут отказать', "и не откажут вработе", "и имеют небольшой шанс на поломку")
    bunkerRepairTuple = ('Все схемы и документация о починке механизмов присутствуют', "Схемы и документация о починке отсутствуют")
    
    bunkerRoomsTuple = ('Химическая лаборатория', 'Склад с защитной экипировкой', 'Класс-кабинет', 'Столовая', 'Пункт управления', 'Комната отдыха', 'Мастерская', 'Санитарный узел', 'Кухня-столовая', 'Кухня', 'Теплица', 'Архив с секретными данными', 'Оружейная', 'Медкабинет', 'Барьер для животных', 'Гидропонная ферма', 'Грядка')
    
    bunkerRoom = str(random.choice(bunkerRoomsTuple))
    bunkerRoom2 = str(random.choice(bunkerRoomsTuple))
    
    while(bunkerRoom == bunkerRoom2):
        bunkerRoom2 = str(random.choice(bunkerRoomsTuple))
    
    bunkerArea = int(random.triangular(26, 136, 55))
    bunkerPlaces = int(bunkerArea//13.65)
    
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
    bunkerInventory2 = str(random.choice(bunkerInventoryTuple))
    
    while (bunkerInventory == bunkerInventory2):
        bunkerInventory2 = str(random.choice(bunkerInventoryTuple))

    # не исправны → в любой момент могут отказать
    if bunkerLifeSys == bunkerLifeSysTuple[1]:
        bunkerRefuse = str(bunkerRefuseTuple[0])
        if bunkerRepair == bunkerRepairTuple[0]:
            bunkerRepair = str(bunkerRepair[0]+', но это бесполезно')

    createdBunkerPool = [
    f':house_abandoned: Площадь убежища: {bunkerArea}м², :bust_in_silhouette: мест в бункере: {bunkerPlaces}\n', 
    f'Убежище находится в {bunkerCondition} состоянии, {bunkerDefense}. ', 
    f'Системы жизнеобеспечения {bunkerLifeSys} и {bunkerAutonomy}, {bunkerRefuse}. {bunkerRepair}.\n\n',
    f':wrench: Бункер оборудован: {bunkerRoom}\n',
    f':wrench: Бункер оборудован: {bunkerRoom2}\n\n',
    f':package: В бункере есть: {bunkerInventory}.\n'
    f':package: В бункере есть: {bunkerInventory2}.'
    ]

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