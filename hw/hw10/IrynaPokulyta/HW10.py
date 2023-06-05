# Task 1. Create a polygon class and a rectangle class that inherits from
# the polygon class and finds the square of a rectangle

class Polygon:
    def __init__(self, num_sides):
        self.num_sides = num_sides
        self.sides = [0] * num_sides
    
    def input_sides(self):
        self.sides = [float(input(f"Enter length of side {i+1}: ")) for i in range(self.num_sides)]
    
    def display_sides(self):
        for i, side in enumerate(self.sides):
            print(f"Side {i+1}: {side}")
    
    def perimeter(self):
        return sum(self.sides)

class Rectangle(Polygon):
    def __init__(self):
        super().__init__(4)  # Rectangle has 4 sides
    
    def area(self):
        if len(self.sides) == 4 and self.sides[0] == self.sides[2] and self.sides[1] == self.sides[3]:
            return self.sides[0] * self.sides[1]
        else:
            return "Invalid rectangle!"

rectangle = Rectangle()
rectangle.input_sides()
rectangle.display_sides()
print("Perimeter:", rectangle.perimeter())
print("Area:", rectangle.area())

# Task2. Create a class Human, everyone has a name, create a method in the
# class that displays a welcome message to each person. Create a class method
# in the class that returns information that it is a species of "Homosapiens". And
# in the class create a static method that returns an arbitrary message.

class Human:
    def __init__(self, name):
        self.name = name
    
    def welcome_message(self):
        print(f"Welcome, {self.name}!")
    
    @classmethod
    def get_species(cls):
        return "Homosapiens"
    
    @staticmethod
    def arbitrary_message():
        return "This is an arbitrary message."

person1 = Human("Iryna")
person1.welcome_message()  
print(Human.get_species())         
print(Human.arbitrary_message())

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
    """
    This is the Employee class.
    It represents employees with their name and salary.
    """
    total_employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employees += 1

    def display_employee_info(self):
        """
        Display the name and salary of the employee.
        """
        print("Name:", self.name)
        print("Salary:", self.salary)

    @classmethod
    def display_total_employees(cls):
        """
        Display the total number of employees.
        """
        print("Total Employees:", cls.total_employees)

emp1 = Employee("Sam Voronenko", 5000)
emp2 = Employee("Nastya Green", 6000)

emp1.display_employee_info()
emp2.display_employee_info()

Employee.display_total_employees()

# Displaying additional class information
print("Base classes:", Employee.__base__)
print("Class namespace:", Employee.__dict__)
print("Class name:", Employee.__name__)
print("Module name:", Employee.__module__)
print("Documentation:", Employee.__doc__)