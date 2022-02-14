from question_2_points import Point
from question_3_line import Line


class Rectangle:
    def __init__(self, bottom_left_corner: Point, top_right_corner: Point):
        self.__bottom_left_corner = bottom_left_corner
        self.__top_right_corner = top_right_corner

    @property
    def bottom_left_corner(self):
        return self.__bottom_left_corner

    @property
    def top_right_corner(self):
        return self.__top_right_corner

    def derive_bottom_right(self):
        bottom_right_object = Point(self.__bottom_left_corner.y, self.__top_right_corner.x)
        return bottom_right_object

    def derive_top_left(self):
        top_left_point_object = Point(self.__bottom_left_corner.x, self.__top_right_corner.y)
        return top_left_point_object

    def area(self):
        line_1 = Line(Point(self.__bottom_left_corner.x, self.__bottom_left_corner.y),
                      Point(self.derive_top_left().x, self.derive_top_left().y))
        line_2 = Line(Point(self.derive_bottom_right().x, self.derive_bottom_right().y),
                      Point(self.__top_right_corner.x, self.__top_right_corner.y))
        rec_length = line_1.length()
        rec_width = line_2.length()
        area = round(rec_length * rec_width, 2)
        return area

    def perimeter(self):
        line_1 = Line(Point(self.__bottom_left_corner.x, self.__bottom_left_corner.y),
                      Point(self.derive_top_left().x, self.derive_top_left().y))
        line_2 = Line(Point(self.derive_bottom_right().x, self.derive_bottom_right().y),
                      Point(self.__top_right_corner.x, self.__top_right_corner.y))
        rec_length = line_1.length()
        rec_width = line_2.length()
        perimeter = round((rec_length * 2) + (rec_width * 2), 2)
        return perimeter


def main():
    bottom_left = Point(1.0, 2.0)
    top_right = Point(3.0, 5.0)

    rectangle1 = Rectangle(bottom_left, top_right)
    print(f"Rectangle area is {rectangle1.area()} m2")
    print(f"Rectangle perimeter is {rectangle1.perimeter()} m")


if __name__ == "__main__":
    main()
