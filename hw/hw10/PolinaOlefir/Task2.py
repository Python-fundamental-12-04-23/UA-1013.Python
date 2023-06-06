# Task2. Create a class Human, everyone has a name, create a method in the class that displays a welcome message to each person.
# Create a class method in the class that returns information that it is a species of "Homosapiens".
# And in the class create a static method that returns an arbitrary message.

class Human:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Welcome {self.name}"

    @classmethod
    def info_about_species(cls):
        return "Homosapiens"

    @staticmethod
    def arbitrary_message():
        return "Glory to Ukraine!"
