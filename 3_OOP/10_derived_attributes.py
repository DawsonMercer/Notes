from datetime import date
# when to use data classes?
# when to use property? is this an attribute of a dataclass
# is @value.setter only used in dataclasses?

# when to use init??
# can you use __str__ with dataclasses and common classes or only common classes?
# when to use isInstance with assert?
#


class Dog:
    tag = 0

    def __init__(self, name: str, birthday: date):
        self.name = name
        self.__birthday = birthday
        Dog.tag += 1
        self.dog_id = Dog.tag

    # This is a str method. a string must be returned.
    def __str__(self):
        return f"im a dog and my name is {self.name}. my ID is {self.dog_id}. I am {self.age} years old"

    # example of derived property - age is not being stored in the obejct we are derived the birthday and current time
    @property
    def age(self):
        currentDate = date.today()  # get dcurrent date
        time_passed = currentDate - self.__birthday
        return time_passed.days // 365.25


dog1 = Dog('spot', date(year=2018, month=2, day=20))
dog2 = Dog('Buster', date(year=2020, month=8, day=5))

print(dog1.dog_id)
print(dog2.dog_id)
print(dog1.name)

print(dog1)
print(dog2)
