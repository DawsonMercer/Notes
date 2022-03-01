
class Student:
    def __init__(self, id, name, address, program):
        self.__id = id
        self.__name = name
        self.__address = address
        self.__program = program
        self.__current_courses = []  # contains a list of course IDs
        self.__completed_courses= {}  # contains mapp from course ID to marks obtained

    @property
    def name(self):
        return self.__name

    @property
    def id(self):
        return self.__id

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, new_address):
        self.__address = new_address

    @property
    def average_score(self):
        if len(self.__completed_courses) == 0:
            return -1
        else:
            total = 0
            for course in self.__completed_courses:
                score = self.__completed_courses[course]
                total += score
            average_score = round(total / len(self.__completed_courses), 2)
            return average_score

    def add_course(self, new_course_id):
        self.__current_courses.append(new_course_id)

    def drop_course(self, delete_by_id):
        if delete_by_id in self.__current_courses:
            self.__current_courses.remove(delete_by_id)
            print(f"{delete_by_id} has been removed from the list")
            print(self.__current_courses)
        else:
            raise ValueError('Cannot delete. Course ID does not exist')

    def course_completed(self, course_id, marks_obtained):
        if course_id in self.__current_courses:
            self.__completed_courses[course_id] = marks_obtained
            print(f"Completed courses Dict: {self.__completed_courses}")
        else:
            print(f"There is no course with id {course_id}")


def main():
    student_1 = Student(2011, "Dawson", "42069 Blaze St", "ASD", [2001, 2201, 5432, 1001],
                        {
                            2202: 80,
                            5432: 70,
                            1001: 60

                        })
    student_1.add_course(4004)
    print(f"{student_1.name}'s Average Score: {student_1.average_score()}")
    # student_1.drop_course(5005)
    student_1.drop_course(2001)
    student_1.course_completed(2001, 98)


if __name__ == "__main__":
    main()
