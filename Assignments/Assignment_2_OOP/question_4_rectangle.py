from question_2_points import Point
from question_3_line import Line


class Rectangle:
    def __init__(self, bottom_left_corner: Point, top_right_corner: Point):
        assert isinstance(bottom_left_corner, Point)
        assert isinstance(top_right_corner, Point)
        self.__bottom_left_corner = bottom_left_corner
        self.__top_right_corner = top_right_corner

    @property
    def bottom_left_corner(self):
        return self.__bottom_left_corner

    @property
    def top_right_corner(self):
        return self.__top_right_corner

    @property
    def bottom_right_corner(self):
        bottom_right_object = Point(self.__top_right_corner.x, self.bottom_left_corner.y)
        return bottom_right_object

    @property
    def top_left_corner(self):
        top_left_point_object = Point(self.__bottom_left_corner.x, self.__top_right_corner.y)
        return top_left_point_object

    @property
    def area(self):
        line_1 = Line(self.top_left_corner, self.__top_right_corner)
        line_2= Line(self.top_left_corner, self.__bottom_left_corner)

        rec_length = line_1.length
        rec_width = line_2.length
        area = rec_length * rec_width
        return area

    @property
    def perimeter(self):
        line_1 = Line(self.top_left_corner, self.__top_right_corner)
        line_2 = Line(self.top_left_corner, self.__bottom_left_corner)
        rec_length = line_1.length
        rec_width = line_2.length
        perimeter = (rec_length * 2) + (rec_width * 2)
        return perimeter


def main():
    bottom_left = Point(1.0, 4.0)
    top_right = Point(8.0, 20.0)

    rectangle1 = Rectangle(bottom_left, top_right)
    print(f"Rectangle area is {rectangle1.area()} m2")
    print(f"Rectangle perimeter is {rectangle1.perimeter()} m")


if __name__ == "__main__":
    main()
