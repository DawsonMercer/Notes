class Doctor:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    @property
    def name(self):
        return self.__name

    @property
    def salary(self):
        return self.__salary

    def __str__(self):
        return self.__name + "" + str(self.__salary)


class Surgeon(Doctor):
    def __init__(self, name, salary, specialty):
        Doctor.__init__(self, name, salary)
        self.__specialty = specialty

    @property
    def specialty(self):
        return self.__specialty

    def __str__(self):
        return f"{Doctor.__str__(self)} {self.__specialty}"

class Hospital:
    def __init__(self):
        self.__doctors = []

    @property
    def doctors(self):
        return self.__doctors

    def add_doctors(self, doctor):
        self.__doctors.append(doctor)

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        if self.__index >= len(self.__doctors):
            raise StopIteration()
        doctor = self.__doctors[self.__index]
        self.__index += 1
        return doctor




def main():
    doctor = Doctor("Jim", 200000)
    surg = Surgeon("Jill", 350000, "eye")
    # print(doctor)
    # print(surg)

    hospital = Hospital()
    hospital.add_doctors(doctor)
    hospital.add_doctors(surg)
    # print(hospital)

    # for doc in hospital.doctors:
    #     print(doc)
    for doc in hospital:
        print(doc)


    num_list =[1,2,3,4,5]
    for num in num_list:
        print(num)

if __name__ == "__main__":
    main()
