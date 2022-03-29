
import random


class RandomIntList(list):
    def __init__(self, count):
        super().__init__()
        self.__count = count
        # self.__random_list = []
        self.create_list()
        #print(self)

    # @property
    # def count(self):
    #     return self.__count

    def create_list(self):
        while len(self) < self.__count:
            rand_int = random.randint(1, 100)
            self.append(rand_int)

    def average(self):
        total = 0
        for number in self:
            total += number
        return round(total/len(self), 3)

    def total(self):
        total = 0
        for number in self:
            total += number
        return total

    def __str__(self):
        integers = ""
        for number in self:
            if (self.index(number)+1) == len(self):
                integers += f"{number}"
            else:
                integers += f"{number}, "
        return f"\nRandom Integers\n" \
               f"===============\n" \
               f"Integers: {integers}\n" \
               f"Count: {self.__count}\n" \
               f"Total: {self.total()}\n" \
               f"Average: {self.average()}\n"



def main():
    print("Random Integer List")
    while True:
        int_list = RandomIntList(5)
        print(int_list)

        choice = input("Continue? (y/n): ")
        if choice.lower() == "n":
            #print("\nBye!")
            break




if __name__ =="__main__":
    main()