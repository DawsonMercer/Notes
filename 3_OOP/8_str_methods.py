
class Dog:
    tag = 0

    def __init__(self, name):
        self.name = name
        Dog.tag += 1
        self.dog_id = Dog.tag

    #This is a str method. a string must be returned.
    def __str__(self):
        return f"im a dog and my name is {self.name}. my ID is {self.dog_id}"

dog1 = Dog('spot')
dog2 = Dog('Buster')

print(dog1.dog_id)
print(dog2.dog_id)
print(dog1.name)

print(dog1)
print(dog2)

