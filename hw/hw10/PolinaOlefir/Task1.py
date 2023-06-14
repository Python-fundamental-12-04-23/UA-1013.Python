# Task1.Create a polygon class and a rectangle class that inherits from the polygon class
# and finds the square of rectangle.
class Polygon:
    def __init__(self, num_of_sides):
        self.num_of_sides = num_of_sides

    def square(self):
        pass


class Rectangle(Polygon):
    def __init__(self, a, b):
        super().__init__(4)
        self.a = a
        self.b =b

    def square(self):
        return self.a * self.b





