from dataclasses import dataclass
import math


@dataclass
class Circle:
    radius:float
    centre_position:tuple

    def get_area(self):
        area = round(self.radius *  self.radius * math.pi, 2)
        return area

    def get_circumference(self):
        circumference = self.radius * 2
        return circumference


@dataclass
class Rectangle:
    length:float
    width:float
    top_left_corner_position:tuple

    def get_area(self):
        area = round(self.length * self.width, 2)
        return area

    def get_perimeter(self):
        perimeter = self.width + self.width + self.length + self.length
        return perimeter



