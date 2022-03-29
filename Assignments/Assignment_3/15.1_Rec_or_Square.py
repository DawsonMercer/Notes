# 15-2 Porject rectangle or square calculator

class Rectangle:
    def __init__(self, height: int, width: int):
        self.__height = height
        self.__width = width

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        return (self.__height * 2) + (self.__width * 2)

    def make_shape(self):
        column_counter = 0
        row_counter = 1
        shape = ""
        while row_counter <= self.__height:
            if row_counter == 1 or row_counter == self.__height:
                shape+=("*  " * self.__width)
                shape +="\n"
            row_counter += 1
            if 1 < row_counter < self.__height:
                shape+=("*  " + ("   " * (self.__width - 2)) + "*")
                shape+="\n"

        return shape


    def __str__(self):
        return f'Height {self.__height}' \
               f'\nWidth: {self.__width}' \
               f'\nArea: {self.area()}' \
               f'\nPerimeter: {self.perimeter()}' \
               f'\n{self.make_shape()}'


class Square(Rectangle):
    def __init__(self, height):
        Rectangle.__init__(self, height, height)



def main():
    print("Rectangle Calculator\n")
    while True:

        shape = input("Rectangle or Square? (r/s): ")
        height = int(input("Height: "))

        if shape == "s":
            print(Square(height))
        elif shape == "r":
            width = int(input("Width: "))
            print(Rectangle(height, width))

        choice = input(f"Continue? (y/n):")
        if choice.lower() == "y":
            continue
        elif choice.lower() == "n":
            print("\nBye!")
            break
        else:
            print("Invalid entry. Continueing")



    # rec1 = Rectangle(height, width)
    # print(rec1)


if __name__ == "__main__":
    main()
