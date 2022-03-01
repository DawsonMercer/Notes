import datetime

class Company:
    def __init__(self, name, address, phone):
        self.name = name
        self.employees = []

    def hire(self, employee):
        assert isinstance(employee, Employee) #!!! as
        self.employees.append(employee)



class Employee:
    employee_counter: int = 0

    def __init__(self, name, sin):
        assert isinstance(name, str), "name must be string"
        #if sin is not an int, raise type error
        if not isinstance(sin,int):
            raise TypeError("sin must be int")
        #if sin's lenght is != 9, raise value error
        #if not 1000000000 <= sin <=999999999:
        #raise Value Error()
        if len(str(sin))!= 9:
            raise ValueError("SIN must be 9-digit")
        self.name = name # public var
        self.__sin = sin # private var
        Employee.employee_counter += 1


        @property
        def SIN(self):
            return "PRIVATE"

        @SIN.setter
        def SIN(self, new_sin):
            if not isinstance(new_sin, int):
                raise TypeError("sin must be int")
            if len(str(new_sin)) != 9:
                raise ValueError("SIN must be 9-digit number")
            self.__old_sins.append(self.__sin)
            self.__sin = new_sin


class HourlyEmployee(Employee):
    def __init__(self, name, sin, hourly_wage):
        Employee.__init__(self, name, sin)
        self.__wage = hourly_wage
        self.__id = f"H{str(Employee.employee_counter).zfill(2)}" # H01, H02
        self.__work_log = []

    @property
    def id(self):
        return self.__id

    def add_work_log(self, start_time, end_time):
        assert isinstance(start_time, datetime.datetime), "start_time must be datetime.datetime object"
        assert isinstance(end_time, datetime.datetime), "end_time must be datetime.datetime object"
        assert end_time > start_time, 'end_time must be after start time'
        log = {"start_time": start_time, "end-time": end_time}
        self.__work_log.append(log)

    def get_hours_worked_since(self, timestamp):
        # go through the work_log list
        # check if start_time is greater than timestamp, if so, calculate hours worked and add to total
        # return total
        pass


class SalariedEmployee(Employee):
    def __init__(self, name, sin , annual_salary):
        Employee.__init__(self, name, sin)
        self.__salary = annual_salary
        self.__id = f"SE_{str(Employee.employee_counter).zfill(2)}" # SE_01

    @property
    def id(self):
        return self.__id



if __name__ == "__main__":

    dawson = HourlyEmployee("Dawson", 123456789, 80)
    print(dawson.id)

    employee_robin = SalariedEmployee("Robin", 222222222, 800000)
    print(employee_robin.id)
