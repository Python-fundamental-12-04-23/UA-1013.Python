#Task1 Regular Ball Super Ball
class Ball(object):
    # your code goes here
    def __init__(self,ball_type = 'regular'):
        self.ball_type = ball_type


#Task2 Color Ghost

import random
class Ghost(object):
    # your code goes here
    def __init__(self):
        self.color = random.choice(['white', 'yellow', 'purple', 'red'])




#Task3 Basic subclasses - Adam and Eve
def God():
    #code
    return [Man(), Woman()]

#code
class Human:
    pass

class Man(Human):
    pass

class Woman(Human):
    pass

#Task4 Classy Classes
class Person:
    def __init__(self,name,age):
        self.info=f"{name}s age is {age}"



#Task5 Building Spheres
import math


class Sphere(object):
    # Good Luck!
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        return round(4 / 3 * math.pi * self.radius ** 3, 5)

    def get_surface_area(self):
        return round(4 * math.pi * self.radius ** 2, 5)

    def get_density(self):
        return round(self.mass / self.get_volume(), 5)

#Task6 Python's Dynamic Classes

def class_name_changer(cls, new_name):
    if new_name[0].isupper() and new_name.isalnum():
        cls.__name__ = new_name
    else:
        raise Exception('Invalid class name.')
