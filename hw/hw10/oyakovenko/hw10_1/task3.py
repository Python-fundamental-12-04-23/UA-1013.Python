class Employee:
    """This is class Employee with counter of instance which were created"""
    i = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.i += 1

    @classmethod
    def print_total_number_of_employee(cls):
        print(cls.i)

    def get_info_about_employee(self):
        info = 'Employee name is ' + self.name + '. Employee salary is ' + str(self.salary)
        return info


employee1 = Employee('Alex', 5000)
employee2 = Employee('Jack', 6000)

print(employee1.get_info_about_employee())
print(employee2.get_info_about_employee())
Employee.print_total_number_of_employee()
print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)
