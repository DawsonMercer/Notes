import math


class Circle:
    def __init__(self, radius: float = 1.0, color: str = 'red'):
        assert isinstance(radius, float), 'Radius must be float.'
        assert radius > 0, 'Radius must be greater than 0.'
        self.__radius = radius
        self.__color = color

    @property
    def radius(self):
        return self.__radius

    @property
    def color(self):
        return self.__color

    @radius.setter
    def radius(self, radius):
        if not isinstance(radius, float):
            raise TypeError('Radius must be numeric')
        elif radius <= 0:
            raise ValueError("Radius must be greater than 0.")
        self.__radius = radius

    @color.setter
    def color(self, color):
        self.__color = color

    def get_area(self):
        area = self.radius * self.radius * math.pi
        return area

    def get_circumference(self):
        circumference = ((self.radius * 2) * math.pi)
        return circumference

    def __str__(self):
        return f'The radius of the circle is {self.radius} and color is {self.color}'


def main():
    c1 = Circle(3.0, "green")
    # c1.radius = -1
    print(c1)
    print(f"Area: {c1.get_area()}")
    print(f"Perimeter: {c1.get_circumference()}")


if __name__ == "__main__":
    main()
