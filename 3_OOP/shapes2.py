import random
from dataclasses import dataclass
class Circle:
    def __init__(self, circle_radius, circle_color):
        self.__radius = circle_radius #private
        self.color = circle_color #public

    def get_radius(self):
        return self.__radius

    def set_radius(self, new_radius):
        assert isinstance(new_radius, (int, float)), 'new radius must be int or float'
        assert new_radius > 0, 'new radius must be greater than 0'
        self.__radius = new_radius


my_circle = Circle(10, 'red')

print(my_circle.color)
#print(my_circle.__radius) error
#print(my_circle.radius) error

my_circle.set_radius(12.2)
print(my_circle.get_radius())

#the advantage of @property is that you no lonmger need to call upon the get_value method. you can instead say die.value()

#this is data class
@dataclass
class Die:
    __value: int = 1

    #property and @value.setter have to be the same name as the value attribute otherwise it will never know they are meant to be used together
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        assert value >= 1 and value <= 6, "Die value must be between 1 and 6"
        self.__value = value

    def roll(self):
        self.__value = random.randrange(1, 7)

die = Die()
die.value = 1

#for read only attributes, only do a getter (property) and not setter (@value.setter)


#this is a standard class with no setter
class Dice:
    def __init__(self):
        self.__list = []

    @property
    def list(self):
        return self.tuple(self.__list)

    def addDie(self, die):
        self.__list.append(die)

    def rollAll(self):
        for die in self.__list:
            die.roll()



