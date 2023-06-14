import random


# Practical Tasks

# I. Ball super ball

class Ball:
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type


# II. Color ghost

class Ghost:
    def __init__(self):
        self.color = random.choice(["white", "yellow", "purple", "red"])


ghost = Ghost()
print(ghost.color)

# III. Basic subclasses-Adam and Eve


class Human:
    def __init__(self, name):
        self.name = name


class Man(Human):
    def __init__(self, name):
        super().__init__(name)


class Woman(Human):
    def __init__(self, name):
        super().__init__(name)


def create_adam_and_eve():
    adam = Man("Adam")
    eve = Woman("Eve")
    return [adam, eve]

# IV. Classy classes


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.info = f"{name}s age is {age}"

    def get_info(self):
        return self.info


# V. Building Spheres

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
        volume = 4/3 * Sphere.pi * pow(self.radius, 3)
        return round(volume, 5)

    def get_surface_area(self):
        surface = 4*Sphere.pi * pow(self.radius, 2)
        return round(surface, 5)

    def get_density(self):
        density = self.mass / (4/3 * Sphere.pi * pow(self.radius, 3))
        return round(density, 5)


ball = Sphere(15, 70)
print(ball.get_radius())
print(ball.get_mass())
print(ball.get_volume())
print(ball.get_surface_area())
print(ball.get_density())


# VI. Dynamic Classes
def change_class_name(old_class, new_class_name):
    if not new_class_name[0].isupper() or not new_class_name.isalnum():
        raise ValueError()

    globals()[new_class_name] = type(new_class_name,
                                     old_class.__bases__, dict(old_class.__dict__))
    return globals()[new_class_name]
