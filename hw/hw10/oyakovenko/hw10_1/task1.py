class Polygon:
    def __init__(self, num_sides):
        self.num_sides = num_sides

    def get_num_sides(self):
        return self.num_sides

    def set_num_sides(self, new_val):
        self.num_sides = new_val


class Rectangle(Polygon):
    def __init__(self, a, b):
        Polygon.__init__(self, 4)
        self.a = a
        self.b = b

    def get_square(self):
        return self.a * self.b


my_rectangle = Rectangle(4, 6)
print(my_rectangle.get_square())