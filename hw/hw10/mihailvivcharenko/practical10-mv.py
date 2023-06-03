# Task1. Create a polygon class and a rectangle class
# that inherits from the polygon class and finds the square
# of rectangle.

class Polygon:
    def __init__(self, sides):
        self.sides = sides


class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__(4)
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width


rectangle = Rectangle(5, 10)
area = rectangle.get_area()
print("Area of the rectangle:", area)


# Тask2. Create a class Human, everyone has a name, create a method in the
# class that displays a welcome message to each person. Create a class method
# in the class that returns information that it is a species of "Homosapiens". And
# in the class create a static method that returns an arbitrary message

class Human:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        species = self.species()
        return f"Welcome {self.name}! You are {species}."

    @classmethod
    def species(cls):
        return "Homosapiens"

    @staticmethod
    def arbitrary_message():
        return "static method"


human1 = Human('Mihail')
print(human1)


# Task3. Create an employee class. Each employee has characteristics such as name
# and salary. The class should have a counter that calculates the total number of
# employees, as well as a method that prints the total number of employees and a
# method that displays information about each employee in particular, namely the
# name and salary.
# In addition to creating a class, display information about the base classes from which
# the employee class is inherited (__base__), the class namespace (__dict__), the
# class name (__name__), the module name in which the class is defined
# (__module__), the documentation bar ( __doc__)

class Employee:

    total = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total += 1

    def info_employee(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

    @classmethod
    def total_employee(cls):
        print(f"Total employees: {cls.total}")


emp1 = Employee("Oleg Gromov", 4000)
emp2 = Employee("Bastian Gonset", 15000)
emp3 = Employee("John Stevenson", 23100)
emp4 = Employee("Mihail Rect", 12130)


emp1.info_employee()
Employee.total_employee()
print("Class namespace (__dict__):", Employee.__dict__)
print("Class name (__name__):", Employee.__name__)
print("Module name (__module__):", Employee.__module__)
print("Documentation (__doc__):", Employee.__doc__)
