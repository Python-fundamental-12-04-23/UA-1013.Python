class Human:
    def __init__(self, name):
        self.name = name

    def welcome_method(self):
        print('Hello ' + self.name)

    @classmethod
    def species_info(cls):
        return 'This is the species of Homosapiens'

    @staticmethod
    def arbitrary_message():
        return 'Hello World!'


me = Human('Alex')
me.welcome_method()
print(Human.species_info())
print(Human.arbitrary_message())