# task I
class Ball:
    def __init__(self, balltype='regular'):
        self.ball_type = balltype


ball1 = Ball()
ball2 = Ball("super")

# task II
import random


class Ghost():
    def __init__(self):
        self.color = random.choice(['white', 'yellow', 'purple', 'red'])


ghost = Ghost()
print(ghost.color)


# task III
def God():
    return [Man(), Woman()]


class Human(object):
    pass


class Man(Human):
    pass


class Woman(Human):
    pass


# task IV
class Person:
    def __init__(self, name, age):
        self.info = f"{name}s age is {age}"


# task V
import math


class Sphere(object):
    def __init__(self, r, m):
        self.r = r
        self.m = m

    def get_radius(self):
        return self.r

    def get_mass(self):
        return self.m

    def get_volume(self):
        V = (4 / 3) * math.pi * self.r ** 3
        return round(V, 5)

    def get_surface_area(self):
        sa = 4 * math.pi * self.r ** 2
        return round(sa, 5)

    def get_density(self):
        d = self.m / ((4 / 3) * math.pi * self.r ** 3)
        return round(d, 5)


ball = Sphere(2, 50)
print(ball.get_radius())
print(ball.get_mass())
print(ball.get_volume())
print(ball.get_surface_area())
print(ball.get_density())


# task VI

def class_name_changer(cls, new_name):
    assert new_name[0].isupper() and new_name.isalnum()
    cls.__name__ = new_name
