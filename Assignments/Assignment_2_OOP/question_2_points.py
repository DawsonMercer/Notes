class Point:
    def __init__(self, x: float, y: float):
        self.__x = x
        self.__y = y


    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __str__(self):
        return f'({self.__x}, {self.__y})'


def main():
    p = Point(2.0, 3.0)
    print(p)


if __name__ == "__main__":
    main()

