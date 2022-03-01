class Fraction:
    def __init__(self, numerator, denominator):
        self.__num = numerator
        self.__denom = denominator

    @property
    def numer(self):
        return self.__num

    @property
    def denom(self):
        return self.__denom

    @property
    def decimal(self):
        return self.__num/self.__denom

    def __str__(self):
        return f'{self.__num}/{self.__denom}'

    def __add__(self, other):
        return self.decimal + other.decimal


    def __sub__(self, other):
        return self.decimal - other.decimal

    def __mul__(self, other):
        return self.decimal * other.decimal

    def __truediv__(self, other):
        return self.decimal / other.decimal

    def __eq__(self, other):
        return self.decimal == other.decimal

    def __lt__(self, other):
        return self.decimal < other.decimal


    def __gt__(self, other):
        return self.decimal > other.decimal

    def __le__(self, other):
        return self.decimal <= other.decimal

    def __ge__(self, other):
        return self.decimal >= other.decimal


two_thirds = Fraction(numerator=2, denominator=3)
half = Fraction(numerator=1, denominator=2)
print(two_thirds)
print(half)

# to test __add__
print("__add__")
print(two_thirds + half)
print("__sub__")

print(two_thirds - half)
print("__mul__")

print(two_thirds * half)
print("__truedic__")

print(two_thirds / half)
print("__lt__")

print(two_thirds < half)
print("__gt__")

print(two_thirds > half)
print("__le__")

print(two_thirds <= half)
print("__ge__")

print(two_thirds >= half)