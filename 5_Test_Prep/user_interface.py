import pickle
from employees import Employee, HourlyEmployee, SalariedEmployee
def display_menu():
    print('1. Save File')
    print('2. read file')
    print("3. add new hourly employee")
    print('4. Add salaries employee')
    print('0. Exit')


def main():
    employees = []
    while True:
        display_menu()
        choice = input('Enter Choice: ')
        if choice == "0":
            break
        elif choice == "1":
            filename = input('enter filename: ')
            save_file(employees, filename) # with open bin

        elif choice == "2":
            employees = read_file(employees, filename)
        elif choice == "3":
            name = input('Enter employee name: ')
            sin = input('enter employee sin')
            hourly_rate = input('enter hourly rate: ')
            hourly_employee = HourlyEmployee(name, sin, hourly_rate)
            employees.append(hourly_employee)
            # todo: check to rest of his code on github




if __name == "main":
    main()