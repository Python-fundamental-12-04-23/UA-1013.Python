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
# Create a class Human, everyone has a name, create a method in the
# class that displays a welcome message to each person. Create a class method
# in the class that returns information that it is a species of "Homosapiens". And
# in the class create a static method that returns an arbitrary message.

class Human:
    def __init__(self,name):
        def welcome_mesage(self):
            print(f"Welcome,{self.name}!")
            @classmethod
            def species(cls):
                return "Homosapiens"

            @staticmethod
            def rbitrary_message():
                return "an arbitrary message"
