# task 1
class Polygon():
    pass
class Rectangle(Polygon):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rect = Rectangle(5, 3)
print(rect.area())

# task2

class Human:
    def __init__(self, name):
        self.name = name

    def greetings(self):
        return f"Hello, {self.name}"

    def type_of_human(self):
        return "Homosapiens"

    @staticmethod
    def random_text():
        import random
        return random.choice(['test1', 'test2', 'test3', 'test4'])

pl1 = Human('Sasha')
print(pl1.greetings())
print(pl1.type_of_human())
print(pl1.random_text())

# task 3

class Employee():
    '''test string for doc'''
    employees = []
    count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employees.append(self)
        Employee.count += 1

    @classmethod
    def count_employee(cls):
        return cls.count

    def employee_info(cls):
        info = ""
        for employee in cls.employees:
            info += f"The name of employee: {employee.name}, his salary: {employee.salary}\n"
        return info


emp1 = Employee("Sasha", 1000)
emp2 = Employee("Oleksandr", 15000)
emp3 = Employee("Sanya", 25000)

print(emp1.employee_info())

print(Employee.count_employee())

print(Employee.__bases__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)
