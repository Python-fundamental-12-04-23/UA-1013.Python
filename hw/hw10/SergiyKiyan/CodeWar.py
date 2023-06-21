# Create a class Ball. Ball objects should accept one argument for "ball type" when instantiated.
#
# If no arguments are given, ball objects should instantiate with a "ball type" of "regular."

class Ball(object):
    def __init__(self, ball_type='regular'):
        self.ball_type = ball_type

#Color Ghost
import random

class Ghost(object):
  def __init__(self):
    self.color = random.choice(["white", "yellow", "purple", "red"])



# Basic subclasses - Adam and Eve

class Human:
    def __init__(self):
        pass


class Man(Human):
    def __init__(self):
        super().__init__()


class Woman(Human):
    def __init__(self):
        super().__init__()




def God():
    adam = Man()
    eve = Woman()
    return [adam, eve]

humans = God()


#Classy Classes
class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
        self.info = f"{name}s age is {age}"

#Building Spheres

from math import pi
class Sphere:


    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        v = 4/ 3 * pi * pow(self.radius, 3)
        return round(v, 5)

    def get_surface_area(self):
        s = 4 * Sphere.pi * pow(self.radius, 2)
        return round(s, 5)

    def get_density(self):
        v = self.get_volume()
        d = self.mass / v
        return round(d, 5)


#Python's Dynamic Classes
def class_name_changer(cls, new_name: str):
    if new_name[0].isupper and new_name.isalnum():
        cls.__name__ = new_name
    else:
        raise Exception('Invalid class name')