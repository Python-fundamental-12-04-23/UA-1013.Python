import math


class Sphere:
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        v = round((4/3*math.pi*self.radius**3), 5)
        return v

    def get_surface_area(self):
        sa = round((4*math.pi*self.radius**2), 5)
        return sa

    def get_density(self):
        p = round((self.mass / (4/3*math.pi*self.radius**3)), 5)
        return p
