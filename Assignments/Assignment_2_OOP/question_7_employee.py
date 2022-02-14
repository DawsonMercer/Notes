
class Employee:
    def __init__(self, first_name: str, last_name: str, employee_id: str, salary: float):
        self.__first_name = first_name
        self.__last_name = last_name
        if len(employee_id) == 5 and employee_id[0] == "E" and employee_id[1:5].isnumeric():
            print("Emp number good")
            self.__employee_id = employee_id
        else:
            print("Invalid Employee ID")
        self.__salary = salary

    @property
    def employee_id(self):
        return self.__employee_id

    def annual_salary(self):
        return round(self.__salary * 12, 2)

    def name(self):
        return f'{self.__first_name} {self.__last_name}'

    def raise_salary(self, raise_percent):
        raise_calc = 1 + (raise_percent / 100)
        new_salary = round(self.__salary * raise_calc, 2)
        self.__salary = new_salary
        print(f'New Salary: {self.__salary}')


def main():

    # test employee class
    employee1 = Employee("dawson", "mercer", "E0001", 420.00)
    employee1.raise_salary(50)


if __name__ == "__main__":
    main()
