class Employee:
    num_employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.num_employees += 1

    def display_info(self):
        print(f"Employee name: {self.name}\nSalary{self.salary}")

    @classmethod
    def numbers_of_employees(self):
        print(f"Number of employees: {self.num_employees}")


print(Employee.__bases__)

print(Employee.__dict__)

print(Employee.__name__)

print(Employee.__module__)

print(Employee.__doc__)