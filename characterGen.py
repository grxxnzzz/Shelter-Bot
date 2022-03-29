from encodings import utf_8
import random

sexes = (':male_sign:', ':female_sign:')
childFree = (':negative_squared_cross_mark: Чайлдфри', ':white_check_mark: Фертилен', ':sweat_drops: Бык-осеменитель')

profs = ()
phobias = ()
hobbies = ()
cards = ()
inventory = ()

profsFile = open('proffession.txt', 'r', encoding="utf-8")
for i in profsFile:
    profs = i.split(",")
profsFile.close()

phobiasFile = open('phobias.txt', 'r', encoding="utf-8")
for i in phobiasFile:
    phobias = i.split("$")
phobiasFile.close()

hobbiesFile = open('hobbies.txt', 'r', encoding="utf-8")
for i in hobbiesFile:
    hobbies = i.split(",")
hobbiesFile.close()

cardsFile = open('cards.txt', 'r', encoding="utf-8")
for i in cardsFile:
    cards = i.split("$")
cardsFile.close()

inventoryFile = open('inventory.txt', 'r', encoding="utf-8")
for i in inventoryFile:
    inventory = i.split("$")
inventoryFile.close()

bodyTypes = ("Не может самостоятельно передвигаться из-за ожирения", "Не хватает сил, чтобы перемещаться самостоятельно",
             "Хилое", "Худое", "Стройное", "Мускулистое", "Полное", "Жирное", "Геракл", "Афина")
bodyLimbs = ("всё при себе", "нет руки", "нет ноги", "нет рук",
             "нет ног", "Вуйчич", "нет глаза", "нет уха")

health = ("Здоров", "HIV", "Герпес", "Геморрой", "Наркоман", "Наркоман крайней степени тяжести", "Глухонемой", "Глухой", "Немой", "Маниакальное расстройство", "Паранойя", "Шизофрения", "Астма", "Астма в крайней степени тяжести", "Рак легких",
          "Фимоз", "Радикулит", "Остеопороз", "Идеально здоров", "Простуда", "Хронический бронхит", "Хронический насморк", "Пневмония", "В целом здоров", "Кариес", "Флюс", "Артрит", "Гипертония", "Гипотония", "Расстройство пищевого поведения")

traits = ("Мерзкий", "Скромный", "Беззрасудный", "Гений", "Маэстро", "Хладнокровный", "Никакущий", "Мечтатель", "Подлый", "Добрый",
          "Любезный", "Хороший", "Среднестатист", "Человечишка", "Быдло", "Жалкий", "Крутой", "Глупый", "Обаяшка", "Диоген")


def characterCreation():
    createdCharacter = ''

    sex = random.choice(sexes)
    childFreeSex = random.choices(childFree, weights=(10, 75, 5))
    childFreeSex = str(childFreeSex[0])

    age = int(random.triangular(16, 100, 40))

    bCL = random.choices(bodyLimbs, weights=(50, 7, 7, 7, 7, 8, 7, 7), k=1)
    bCL = str(bCL[0])
    if bCL == bodyLimbs[0]:
        bodyCondition = (random.choices(bodyTypes, weights=(1,1,25,25,10,5,25,15,3,3)))
        bodyCondition = str(bodyCondition[0])
    else:
        bodyCondition = (random.choices(bodyTypes, weights=(1,1,25,25,10,5,25,15,3,3)))
        bodyCondition = str(bodyCondition[0] + f', :wheelchair: {bCL}')

    proffesion = str(random.choice(profs))
    profLevel = random.randrange(0, 5)

    healthCondition = random.choices(health, weights=(25,1,10,1,5,2,15,15,15,1,6,12,3,8,1,50,2,2,10,5,25,25,1,75,35,35,1,50,50,90), k=1)
    healthCondition = str(healthCondition[0])

    hobbie = str(random.choice(hobbies))

    phobia = random.choices(phobias, weights=(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 25))
    phobia = str(phobia[0])

    trait = random.choices(traits, weights=(5,5,1,1,3,3,10,5,5,25,25,25,90,11,4,4,1,10,50,1))
    trait = str(trait[0])

    backpack = str(random.choice(inventory))

    card1 = str(random.choice(cards))
    card2 = str(random.choice(cards))

    while (card1 == card2):  # no duplicate card
        card2 = random.choice(cards)

    # a tuple with character parameters
    createdCharacterPool = [
        f'\n:busts_in_silhouette: Пол: {sex} {childFreeSex.lower()}',
        f':calendar_spiral: Возраст: {str(age)}',
        f':bust_in_silhouette: Тело: {bodyCondition.lower()}',
        f':tools: Профессия: {proffesion.lower()}, умение: {str(profLevel)} из 5',
        f':anatomical_heart: Здоровье: {healthCondition.lower()}',
        f':thought_balloon: Хобби: {hobbie.lower()}',
        f':eye: Фобия: {phobia.lower()}',
        f':speaking_head: Характер: {trait.lower()}\n',
        f':package: С собой: {backpack.lower()}',
        f':flower_playing_cards: №1: {card1.lower()}',
        f':flower_playing_cards: №2: {card2.lower()}']

    # beautifying changes • emoji
    ### aging emojis
    ### if  (age >= 50) and (sex == ':male_sign:'):
    ###     createdCharacterPool[0] = f'\n:older_man: Пол: {sex}, {childFreeSex.lower()}'
    ### elif (age >= 50) and (sex == ':female_sign:'):
    ###     createdCharacterPool[0] = f'\n:older_woman: Пол: {sex}, {childFreeSex.lower()}'
    ### elif  (age < 50) and (sex == ':male_sign:'):
    ###     createdCharacterPool[0] = f'\n:man_raising_hand: Пол: {sex}, {childFreeSex.lower()}'
    ### elif (age < 50) and (sex == ':female_sign:'):
    ###     createdCharacterPool[0] = f'\n:woman_raising_hand: Пол: {sex}, {childFreeSex.lower()}'

    # finishing character creation 
    for i in createdCharacterPool:
        createdCharacter = createdCharacter + i + '\n'

    return createdCharacter

# сделать отдельную команду для смены профессии