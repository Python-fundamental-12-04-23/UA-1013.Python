class Human:
    species = 'Homo sapiens'

    def __init__(self, name):
        self.name = name

    @classmethod
    def species_func(cls):
        return f"Human race belongs to {cls.species} species"

    @staticmethod
    def random_msg():
        return "The man shouldn't be a wolf to other man! We're humans!"

    def welcome(self):
        return f"Hello, dear {self.name}!"
