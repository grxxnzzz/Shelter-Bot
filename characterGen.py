from encodings import utf_8
import random
import discord


sexes = ('М', 'Ж')

cataclysms=()
profs = ()
phobias = ()  
hobbies = () 
cards = () 

cataclysmsFile = open('cataclysms.txt', 'r', encoding="utf-8")
for i in cataclysmsFile:
    cataclysms = i.split(",")
cataclysmsFile.close()

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

bodyTypes = ("Не может самостоятельно передвигаться из-за ожирения", "Не хватает сил, чтобы перемещаться самостоятельно", "Хилое", "Худое", "Стройное", "Мускулистое", "Полное", "Жирное", "Геракл", "Афина")
bodyLimbs = ("всё при себе", "нет руки", "нет ноги", "нет рук", "нет ног", "Вуйчич", "нет глаза", "нет уха")

health = ("Здоров", "HIV", "Герпес", "Геморрой", "Наркоман", "Наркоман крайней степени тяжести", "Глухонемой", "Глухой", "Немой", "Маниакальное расстройство", "Паранойя", "Шизофрения", "Астма", "Астма в крайней степени тяжести", "Рак легких", "Фимоз", "Радикулит", "Остеопороз", "Идеально здоров", "Простуда", "Хронический бронхит", "Хронический насморк", "Пневмония", "В целом здоров", "Кариес", "Флюс", "Артрит", "Гипертония", "Гипотония", "Расстройство пищевого поведения")

traits = ("Мерзкий", "Скромный", "Беззрасудный", "Гений", "Маэстро", "Хладнокровный", "Никакущий", "Мечтатель", "Подлый", "Добрый", "Любезный", "Хороший", "Среднестатист", "Человечишка", "Быдло", "Жалкий", "Крутой", "Скромный", "Глупый", "Обаяшка", "Диоген")

def characterCreation():
    createdCharacter = ''
    sex = random.choice(sexes)
    age = int(random.triangular(16, 100, 40))

    bCL = random.choice(bodyLimbs)
    if bCL == bodyLimbs[0]:
        bodyCondition = (random.choice(bodyTypes))
    else:
        bodyCondition = (random.choice(bodyTypes) + f', {bCL}')

    proffesion = str(random.choice(profs)) 
    profLevel = random.randint(1, 5)
    healthCondition = str(random.choice(health))
    hobbie = str(random.choice(hobbies))
    phobia = str(random.choice(phobias))
    trait = str(random.choice(traits))
    card1 = str(random.choice(cards))
    card2 = str(random.choice(cards))

    while (card1==card2): # no duplicate card
        card2=random.choice(cards)

    createdCharacterPool = (f'Пол: {sex}', f'Возраст: {str(age)}', f'Тело: {bodyCondition.lower()}', f'Проффессия: {proffesion.lower()}, умение: {str(profLevel)} из 5', f'Здоровье: {healthCondition.lower()}', f'Хобби: {hobbie.lower()}', f'Фобия: {phobia.lower()}', f'Характер: {trait.lower()}', f'Карта №1: {card1.lower()}', f'Карта №2: {card2.lower()}')

    for i in createdCharacterPool:
        createdCharacter = createdCharacter + i + '\n'

    return createdCharacter
    

print(characterCreation())