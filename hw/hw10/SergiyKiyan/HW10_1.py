#Task 1
class Polygon():
    pass
class Rectangle(Polygon):
    def __init__(self,a_side,b_side ):
        self.a_side=a_side
        self.b_side=b_side


    def square(self):
        return self.a_side*self.b_side

square_rect=Rectangle(10,5)
print(square_rect.square())

#Task 2
# Create a class Human, everyone has a name, create a method in the
# class that displays a welcome message to each person. Create a class method
# in the class that returns information that it is a species of "Homosapiens". And
# in the class create a static method that returns an arbitrary message.

class Human:
    def __init__(self,name):
        def welcome_mesage(self):
            print(f"Welcome,{self.name}!")
            @classmethod
            def species(cls):
                return "Homosapiens"

            @staticmethod
            def rbitrary_message():
                return "an arbitrary message"


# Task3.
# Create an employee class. Each employee has characteristics such as name
# and salary. The class should have a counter that calculates the total number of
# employees, as well as a method that prints the total number of employees and a
# method that displays information about each employee in particular, namely the
# name and salary.
# In addition to creating a class, display information about the base classes from which
# the employee class is inherited (__base__), the class namespace (__dict__), the
# class name (__name__), the module name in which the class is defined
# (__module__), the documentation bar ( __doc__)

class Employee:
    employees_count=0

    def __init__(self, name, salary):
        self.name=name
        self.salary=salary
        Employee.employees_count+=1

    @classmethod
    def total_number_of_employees(self):
        print(f"total number of employees: {self.employees_count}")

    def information_about_each_employee(self):
        print(f"Emploee name: {self.name} \n Emploee salary: {self.salary}")

    def the_base_classes(self):
        print(Employee.__base__)
        print(Employee.__dict__)
        print(Employee.__name__)
        print(Employee.__module__)
        print(Employee.__doc__)




