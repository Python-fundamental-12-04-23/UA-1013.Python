# first task
class Polygon:
    """this class provides frame for any geometrical object.
    you can create child classes that inherites from this 
    parent class by adding specific methods in child class
    since parent class accept any parameter you pass and store it 
    in dict"""
    def __init__(self, **kwargs):
        self.sides = {key: value for key, value in kwargs.items()}
        

class Rectangle(Polygon):
    def get_square(self):
        return self.sides['width'] * self.sides['height']
    
# second task
class Human:
    __species = 'Homo sapiens'

    def __init__(self, name):
        self.name = name

    @classmethod
    def species_func(cls):
        return f"Human race belongs to {cls.__species} species"
    
    @staticmethod
    def random_msg():
        return f"The man souldn`t be a wolf to other man! We`re humans!"
    
    def welcome(self):
        return f"Hello dear {self.name}!"
    
# third task

class Employee:
    """Creates a class for employees
       takes such a parameters as name and salary"""

    __counter = 0

    @classmethod
    def get_counter(cls):
        print(cls.__counter)

    def __init__(self, name, salary):
        Employee.__counter += 1
        self.name = name
        self.salary = salary

    def get_employee(self):
        print(f"Employee name: {self.name}.\nEmployee salary: {self.salary}")
    
    def display_info(self):
        print(Employee.__base__)
        print(Employee.__dict__)
        print(Employee.__name__)
        print(Employee.__module__)
        print(Employee.__doc__)





   
    


