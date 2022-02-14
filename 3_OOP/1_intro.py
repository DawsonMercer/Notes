#create a class called A
class A:
    #init means initilizer - similar to a constructor
    #do not always need a init but you will mostly use it
    #self and this are very similar
    def __init__(self, a1, a2):
        print("init method is invoked")
        self.a1 = a1
        self.a2 = a2

    def afoo(self):
        print(self.a1, self.a2)

#creating a new object class a_object and passing values for the attributes
a_object = A(10, 20)

#calling the afoo() method from the a_object
a_object.afoo()



"""
class A
attributes: a1, a2
method: afoo
"""