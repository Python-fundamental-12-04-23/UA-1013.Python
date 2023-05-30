#Task 1
class Polygon():
    pass
class Rectangle(Polygon):
    def __init__(self,a_side,b_side ):
        self.a_side=a_side
        self.b_side=b_side


    def square(self):
        return self.a_side*self.b_side

square_rect=Rectangle(10,5)
print(square_rect.square())

#Task 2