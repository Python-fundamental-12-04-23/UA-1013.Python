import random
from math import pi

# Regular Ball, Super Ball

class Ball:
    def __init__(self, ball_type='regular'):
        self.ball_type = ball_type

# Color ghost

class Ghost:
    def __init__(self):
        self.color = random.choice(["white", "yellow", "purple", "red"])

class Human:
    def __init__(self):
        self.legs = self.hands = 2
        self.is_sapient = True

class Man(Human):
    def __init__(self, name):
        super().__init__()
        self.name, self.sex = name, 'male'

class Woman(Human):
    def __init__(self, name):
        super().__init__()
        self.name, self.sex = name, 'female'

class God:
    def create(self, male_name, female_name):
        return Man(male_name), Woman(female_name)

# classy classes

class Person:
    def __init__(self, name: str, age: int):
        self.name, self.age = name, age
        self.info = f"{name}'s age is {age}"

    def get_info(self):
        return self.info

# building spheres

class Sphere:
    def __init__(self, radius: float, mass: float):
        self.radius, self.mass = radius, mass

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        return round((4.0 / 3.0) * pi * pow(self.radius, 3), 5)

    def get_surface_area(self):
        return round(4 * pi * pow(self.radius, 2), 5)

    def get_density(self):
        return round(self.mass / self.get_volume(), 5)

# dynamic classes

def class_name_changer(cls, new_name: str):
    if new_name[0].isupper() and new_name.isalnum():
        cls.__name__ = new_name
    else:
        raise Exception('Invalid class name')
