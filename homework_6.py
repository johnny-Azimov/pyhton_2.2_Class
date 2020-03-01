class farm:
    total_weight = 0
    heaviest_animal = None

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        farm.total_weight = 0
        farm.heaviest_animal = None    

    def feed(self):
        print(" {}".format(self.name))

    def scream(self):
        self.sound = 'scream' 

    def product(self):
        pass


class Bird(farm):
    def egg(self):
        print("  яйца от {}".format(self.name))

    def product(self):
        self.egg()

class Goose(Bird):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.sound = 'га-га-га'

class Chicken(Bird):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.sound = 'кудахчет'

class Duck(Bird):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.sound = 'кря-кря-кря'




class Milkfarm(farm):
    def milk(self):
        print("  молоко от {}".format(self.name))

    def product(self):
        self.milk()

class Cow(Milkfarm):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.sound = 'мууу'

class Goat(Milkfarm):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.sound = 'ме-ме-ме'



class Sheep(farm):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.sound = 'бе-бе-бе'

    def shear(self):
        print("  шерсть от {}".format(self.name))

    def product(self):
        self.shear()


goose_Gray = Goose('Гусь "Серый"', 3.3)
goose_White = Goose('Гусь "Белый"', 2.5)
cow_Manka = Cow('Корова "Манька"', 510)
sheep_Lamb = Sheep('Овечка "Барашек"', 67.5)
sheep_Curly = Sheep('Овечка "Кудрявая"', 82.4)
goat_Horns = Goat('Коза "Рога"', 47.7)
goat_Hooves = Goat('Коза "Копыта"', 52)
chicken_Ko = Chicken('Курица "Ko-Ko"', 3)
chicken_Kukareku = Chicken('Курица "Кукареку"', 3.9)
duck_Mallard = Duck('Утка "Кряква"', 1.2)

the_farm = [goose_Gray, goose_White, cow_Manka, sheep_Lamb, sheep_Curly, goat_Horns, goat_Hooves, chicken_Ko, chicken_Kukareku, duck_Mallard]

print('\nЖивотные на ферме, которых нужно кормить:')
for animal in the_farm:
    animal.feed()


print('\nПродукты от животных на ферме:')
for animal in the_farm:
    animal.product()

print('\nЗвуки издаваемые животными на ферме ')
for animal in the_farm:
    print('  {} - {}'.format(animal.name, animal.sound))

for animal in the_farm:
    farm.total_weight = farm.total_weight + animal.weight
print('\nОбщий вес всех животных: {} кг'. format(farm.total_weight))

for animal in the_farm:
    if farm.heaviest_animal is None:
        farm.heaviest_animal = animal
    elif animal.weight > farm.heaviest_animal.weight:
        farm.heaviest_animal = animal
print('Самое тяжёлое животное: {}, имеет вес: {} кг '.format(farm.heaviest_animal.name, farm.heaviest_animal.weight))