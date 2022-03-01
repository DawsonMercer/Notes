import calendar


class Date:
    def __init__(self, year: int, month: int, day):
        if isinstance(day, bool):
            raise TypeError("Must be int")
        if not isinstance(day, int):
            raise TypeError("Must be int")
        if not isinstance(month, int):
            raise TypeError("Must be int")
        if not isinstance(year, int):
            raise TypeError("Must be int")
        if isinstance(year, float):
            raise TypeError("Must be int")
        if isinstance(month, float):
            raise TypeError("Must be int")
        if isinstance(day, str):
            raise TypeError("Must be int")
        if day >= 32 or day <1:
            raise ValueError("Day must be between 1 and 31")
        if month >= 13 or month <1:
            raise ValueError("Month must be between 1 and 12")


        self.__day = day
        self.__month = month
        self.__year = year


        # if isinstance(day, int):
        # else:
        #     raise TypeError('Day must be int.')
        # if isinstance(month, int):
        # else:
        #     raise TypeError('month must be int.')
        # if isinstance(year, int):
        # else:
        #     raise TypeError('Year must be int.')


    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, new_day: int):
        self.__day = new_day

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, new_month: int):
        self.__month = new_month

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, new_year: int):
        self.__year = new_year

    @property
    def is_leap_year(self):
        leap_year = False
        if calendar.isleap(self.year):
            leap_year = True
        return leap_year

    @property
    def is_valid_date(self):
        is_valid = False
        is_leap_year = calendar.isleap(self.year)
        if self.month in (1, 3, 5, 7, 8, 10, 12) and 31 >= self.day >= 1:
            is_valid = True
        elif self.month in (4, 6, 9, 11) and 30 >= self.day >= 1:
            is_valid = True
        elif self.month == 2 and 29 >= self.day >= 1:
            is_valid = True
            if is_leap_year is False and self.day == 29:
                is_valid = False
        else:
            is_valid = False

        return is_valid

    def __str__(self):
        return f'{str(self.day).zfill(2)}/{str(self.month).zfill(2)}/{str(self.year).zfill(4)}'

    # should something be returned each if statement or is it best to set the object to a variable?
    def next_day(self):
        next_day = None
        if Date(self.day, self.month, self.year).is_valid_date():
            if Date(self.day+1, self.month, self.year).is_valid_date():
                next_day = Date(self.day+1, self.month, self.year)
            elif Date(1, self.month+1, self.year).is_valid_date():
                next_day = Date(1, self.month+1, self.year)
            elif self.day == 31 and self.month == 12:
                next_day = Date(1, 1, self.year+1)
        else:
            next_day = "Are you trying to break my code?"
        return next_day

    def previous_day(self):
        if Date(self.day, self.month, self.year).is_valid_date():
            if Date(self.day-1, self.month, self.year).is_valid_date():
                return Date(self.day-1, self.month, self.year)
            elif Date(31, self.month-1, self.year).is_valid_date():
                return Date(31, self.month-1, self.year)
            elif Date(30, self.month-1, self.year).is_valid_date():
                return Date(30, self.month-1, self.year)
            elif Date(29, self.month-1, self.year).is_valid_date():
                return Date(29, self.month-1, self.year)
            elif Date(28, self.month-1, self.year).is_valid_date():
                return Date(28, self.month-1, self.year)
            elif self.day == 1 and self.month == 1:
                return Date(31, 12, self.year-1)
        else:
            return 'Bro thats not even a date'


def main():

    print("Question 5 - Day, Month, Year")
    while True:
        try:
            day = int(input("Enter Day: "))
            month = int(input("Enter Month: "))
            year = int(input("Enter year: "))
            break
        except ValueError:
            print("Day, Month,and Year must be int")

    date1 = Date(day, month, year)
    print(date1)
    print(f"Is this date valid? (T/F) {date1.is_valid_date()}")
    print(f"Leap year? (T/F) {date1.is_leap_year()}")

    print("\nDD/MM/YYY")
    print("Next day")
    print(date1.next_day())
    print("\nPrevious day")
    print(date1.previous_day())


if __name__ == "__main__":
    main()
