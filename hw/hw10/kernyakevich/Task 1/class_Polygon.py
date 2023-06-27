class Polygon:
    """This class provides a framework for any geometrical object.
    Child classes can inherit from this parent class by adding specific methods."""

    def __init__(self, **kwargs):
        self.sides = kwargs


class Rectangle(Polygon):
    def get_square(self):
        return self.sides['width'] * self.sides['height']
