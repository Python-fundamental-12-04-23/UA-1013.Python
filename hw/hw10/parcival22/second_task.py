# Regular Ball, Super Ball

class Ball(object):
    def __init__(self, ball_type='regular'):
        self.ball_type = ball_type

# Color ghost

import random

class Ghost(object):
  def __init__(self):
    self.color = random.choice(["white", "yellow", "purple", "red"])

# Adam & Eve

class Human:
   def __init__(self):
      self.legs = 2
      self.hands = 2
      self.isSapient = True

class Man(Human):
   def __init__(self, name):
      self.name = name
      self.sex = 'male'

class Woman(Human):
   def __init__(self, name):
      self.name = name
      self.sex = 'female'

class God:
   def create(self, male_name, female_name):
      man = Man(male_name)
      woman = Woman(female_name)
      return [man, woman]
   
# classy classes

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.info = f"{name}s age is {age}"

    def get_info(self):
       return self.info
    

# building spheres

class Sphere:
    from math import pi

    def __init__(self, radius: int or float, mass: int or float):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius
   
    def get_mass(self):
        return self.mass
   
    def get_volume(self):
        v = 4.0 / 3.0 * Sphere.pi * pow(self.radius, 3)
        return round(v, 5)
   
    def get_surface_area(self):
        s = 4 * Sphere.pi * pow(self.radius, 2)
        return round(s, 5)
   
    def get_density(self):
        v = self.get_volume()
        d = self.mass / v
        return round(d, 5)
    

# dynamic classes
def class_name_changer(cls, new_name: str):
    if new_name[0].isupper and new_name.isalnum():
        cls.__name__ = new_name 
    else: 
        raise Exception('Invalid class name')