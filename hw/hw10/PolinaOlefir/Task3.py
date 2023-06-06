# Task3. Create an employee class. Each employee has characteristics such as name and salary.
# The class should have a counter that calculates the total number of employees, as well as a method
# that prints the total number of employees and a method that displays information about each employee in particular,
# namely the name and salary.

class Employee:
    count = 0
    def __init__(self, name,salary):
        self.name = name
        self.salary = salary
        Employee.count += 1

    @classmethod
    def total_number(self):
        print(f"Number of employees: {self.count}")

    def info(self):
        return f"{self.name} has {self.salary}"





print(Employee.__bases__)

print(Employee.__dict__)

print(Employee.__name__)

print(Employee.__module__)

print(Employee.__doc__)