from question_2_points import Point
import math


class Line:

    def __init__(self, start_point: Point, end_point: Point):
        assert isinstance(start_point, Point), 'Start point must be of type point'
        assert isinstance(end_point, Point), 'End point must be of type point'
        self.__start_point = start_point
        self.__end_point = end_point

    @property
    def start_point(self):
        return self.__start_point

    @property
    def end_point(self):
        return self.__end_point

    @end_point.setter
    def end_point(self, new_end_point):
        assert isinstance(new_end_point, Point), 'New End Point must be of type point'
        self.__end_point = new_end_point

    # derived property - meaning it is not being stored in the object but is derived from teh object's attributes.
    @property
    def length(self):
        distance = math.sqrt(((self.start_point.x - self.end_point.x) ** 2) +
                                   ((self.start_point.y - self.end_point.y) ** 2))
        return distance


def main():

    start = Point(1.0, 2.0)
    end = Point(3.0, 5.0)

    line1 = Line(start, end)
    print(line1.length())


if __name__ == "__main__":
    main()
