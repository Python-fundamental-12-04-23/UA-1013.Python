class Employee:
    """Creates a class for employees that takes parameters such as name and salary."""

    __counter = 0

    @classmethod
    def get_counter(cls):
        print(cls.__counter)

    def __init__(self, name, salary):
        Employee.__counter += 1
        self.name = name
        self.salary = salary

    def get_employee(self):
        print(f"Employee name: {self.name}\nEmployee salary: {self.salary}")

    def display_info(self):
        print(Employee.__bases__)
        print(Employee.__dict__)
        print(Employee.__name__)
        print(Employee.__module__)
        print(Employee.__doc__)
