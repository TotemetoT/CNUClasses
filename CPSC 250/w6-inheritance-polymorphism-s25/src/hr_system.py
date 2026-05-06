"""
File for implementation of an hr system. See slides for requirements
"""

#Note: If you want to enforce the abstractness of Person, make it abstract using the ABC class
# you can also use the @abstractmethod decorator for abstract methods
#from abc import ABC, abstractmethod
#class Person(ABC)
from given.person import Person

class Student(Person):

    def __init__(self,first_name,last_name,id,year,second_last_name=None):
        Person.__init__(self,first_name,last_name,id,second_last_name)
        self._year = year

    def __str__(self):
        return Person.__str__(self) + ',' + str(self._year)


class Employee(Person):
    hours_per_week = 40
    def __init__(self,first_name,last_name,id,pay_rate,job_title,second_last_name=None):
        Person.__init__(self,first_name,last_name,id,second_last_name)
        self._pay_rate = pay_rate
        self._job_title = job_title

    def __str__(self):
        return Person.__str__(self) + "," + self._job_title

    def get_weekly_pay(self):
        return Employee.hours_per_week * self._pay_rate

class StudentEmployee(Student,Employee):
    hours_per_week = 10
    student_pay = 12
    def __init__(self,first_name,last_name,id,year,job_title,second_last_name=None):
        Student.__init__(self,first_name,last_name,id,year,second_last_name)
        Employee.__init__(self,first_name,last_name,id,StudentEmployee.student_pay,job_title,second_last_name)

    def __str__(self):
        return Person.__str__(self) + "," + self._id

    def get_weekly_pay(self):
        return StudentEmployee.hours_per_week * self.student_pay


#function to write (print to screen) the checks for the employee
def write_check(employee):
    if isinstance(employee, Employee):
        print(str(employee) + " - $" + str(employee.get_weekly_pay()))
    else:
        print("ERROR: cannot write a check to a non-employee")



if __name__ == '__main__':
    people = []
    john_stevens = Student("John", "Stevens", "00001", 2024)
    print(str(john_stevens) + " is class " + str(type(john_stevens)))
    people.append(john_stevens)


    # cindy_stevens = Employee("Cindy", "Stevens", "000211", 38, "System Administrator")
    # print(str(cindy_stevens) + " is class ", type(cindy_stevens))
    # print(str(cindy_stevens) + " makes " + str(cindy_stevens.get_weekly_pay()), " per week")
    # people.append(cindy_stevens)
    #
    # john_stone = StudentEmployee("John", "Stone", "002224", 2022, "Tutor")
    # print(str(john_stone) + " is class " + str(type(john_stone)))
    # print(str(john_stone) + " makes " + str(john_stone.get_weekly_pay()), " per week")
    # people.append(john_stone)
    #
    # zazzy_zanzibar = Employee("Zazzy", "Zanzibar", "200224", 52, "Life Coach")
    # print(str(zazzy_zanzibar) + " is class " + str(type(zazzy_zanzibar)))
    # print(str(zazzy_zanzibar) + " makes " + str(zazzy_zanzibar.get_weekly_pay()), " per week")
    # people.append(zazzy_zanzibar)
    #
    # april_alpha = Employee("April", "Alpha", "200224", 22, "Lawn Care Specialist")
    # print(str(april_alpha) + " is class " + str(type(april_alpha)))
    # print(str(april_alpha) + " makes " + str(april_alpha.get_weekly_pay()), " per week")
    # people.append(april_alpha)
    #
    # manuel_pérez_quiñones = Employee("Manuel", "Pérez", "2000", 75, "Professor", "Quiñones")
    # print(str(manuel_pérez_quiñones) + " is class " + str(type(manuel_pérez_quiñones)))
    # print(str(manuel_pérez_quiñones) + " makes " + str(manuel_pérez_quiñones.get_weekly_pay()), " per week")
    # people.append(manuel_pérez_quiñones)
    #
    # print("Ordered list of employees at CNU:")
    # people.sort()
    # print(people)
    # for person in people:
    #     print(person)
    #
    # # Exercise -- append an a to the employee name. Does your sort method still work?
    # #  What string method is being called in < > == ?  Make it Person()
    #
    # # Exercise -- what string method is student employee calling?
    # #  The order you inherit matters
    #
    # # Exercise -- Abstract classes. You can enforce abstractness using the ABC class
    # # you can also use the @abstractmethod decorator for abstract methods
    # # Try changing the class constructor of Person to:
    # #    from abc import ABC, abstractmethod
    # #    lass Person(ABC)
    #
    # # Exercise -- Polymorphism: type() vs isInstance()
    # print ("\ntype vs. isinstance")
    # print("type of john_stone = ", str(type(john_stone)))
    # print("type(john_stone) == StudentEmployee", type(john_stone) == StudentEmployee)
    # print("type(john_stone) == type(Student)", type(john_stone) == type(Student))
    # print("type(john_stone).isInstance(Student)", isinstance(john_stone, Student))
    #
    # #Write some checks (Polymorphism demo)
    # print("\nWriting Checks")
    # print("John Stone is a Student Employee")
    # write_check(john_stone)
    # print("April Alpha is an Employee")
    # write_check(april_alpha)
    # print("John Stevens is not an Employee, just a Student")
    # write_check(john_stevens)
