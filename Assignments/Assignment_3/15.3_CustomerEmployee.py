
class Person:
    def __init__(self, first_name, last_name, email):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email

    @property
    def full_name(self):
        return f"{self.__first_name} {self.__last_name}"

    @property
    def first_name(self):
        return self.__first_name

    @property
    def last_name(self):
        return self.__last_name

    @property
    def email(self):
        return self.__email


class Customer(Person):
    def __init__(self, first_name, last_name, email, customer_number):
        Person.__init__(self, first_name, last_name, email)
        self.__customer_number = customer_number

    @property
    def customer_number(self):
        return self.__customer_number

    def __str__(self):
        return f"\nCUSTOMER\n" \
               f"First name: {self.first_name}\n" \
               f"Last name: {self.last_name}\n" \
               f"Email: {self.email}\n" \
               f"Number: {self.customer_number}\n"


class Employee(Person):
    def __init__(self, first_name, last_name, email, ssn):
        Person.__init__(self, first_name, last_name, email)
        self.__ssn = ssn

    @property
    def ssn(self):
        return self.__ssn

    def __str__(self):
        return f"\nEMPLOYEE\n" \
               f"First name: {self.first_name}\n" \
               f"Last name: {self.last_name}\n" \
               f"Email: {self.email}\n" \
               f"SSN: {self.ssn}\n"


def data_entry():
    while True:
        option = input("\nCustomer or Employee? (c/e): ")
        person = None
        number = None
        print("\nDATA ENTRY")
        first_name = input("First name: ")
        last_name = input("last name: ")
        email = input("Email: ")
        if option.lower() == "c":
            number = input("Number: ")
            person = Customer(first_name, last_name, email, number)
        elif option.lower() == "e":
            number = input("SSN: ")
            person = Employee(first_name, last_name, email, number)
        if isinstance(person, Customer):
            print(person)
        if isinstance(person, Employee):
            print(person)

        choice = input("Continue? (y/n): ")
        if choice.lower() == "n":
            print("\nBye!")
            break


def main():
    print("Customer/Employee Data Entry")
    data_entry()


if __name__ == "__main__":
    main()
