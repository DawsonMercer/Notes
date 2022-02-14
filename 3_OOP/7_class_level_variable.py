
# class X:
#     x_class_var = 0
#
#
#
# x1 = X()
# x2 = X()
#
# print(x1.x_class_var)
# X.x_class_var = 1
# print(x1.x_class_var)
#
# print(x2.x_class_var)
#

class Dog:
    tag = 0

    def __init__(self, name):
        self.name = name
        Dog.tag += 1
        self.dog_id = Dog.tag


dog1 = Dog('spot')
dog2 = Dog('Buster')

print(dog1.dog_id)
print(dog2.dog_id)
print(dog1.name)


