class Animal:
    alive = True
    fed = False

    def __init__(self, name):
        self.name = name

    # Метод eat:
    def eat(self, food):
        if isinstance(food, Plant):
            if food.edible:
                print(f"{self.name} съел {food.name}")
                self.fed = True

            else:
                print(f"{self.name} не стал есть {food.name}")
                self.alive = False
    # если животному дать съедобное растение, то животное насытится,
    # если не съедобное - погибнет.


# Для класса Plant атрибут edible = False(съедобность),
class Plant:
    edible = False

    def __init__(self, name):
        self.name = name


# 4 класса наследника:
# Mammal, Predator для Animal.
# Flower, Fruit для Plant.

class Mammal(Animal):
    pass


class Predator(Animal):
    pass


class Flower(Plant):
    pass


class Fruit(Plant):
    # У каждого объекта Fruit должен быть атрибут edible = True (переопределить при наследовании)
    edible = True

    def __init__(self, name):
        self.name = name


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)

# Что произошло: Хищник попытался съесть цветок и погиб, млекопитающее съело фрукт и насытилось.
