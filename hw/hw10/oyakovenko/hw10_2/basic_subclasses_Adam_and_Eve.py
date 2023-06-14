class Human:
    def __init__(self):
        self.person = 'Human'
        print('Human is created')

    def get_person(self):
        name = self.person
        return name


class Man(Human):
    def __init__(self):
        super().__init__()
        self.person = 'Man'
        print("Man Created")


class Woman(Human):
    def __init__(self):
        super().__init__()
        self.person = 'Woman'
        print("Woman Created")


def God():
    m = Man()
    w = Woman()
    list = [m, w]
    return list

paradise = God()
print((isinstance(paradise[0], Man), True, "First object are a man"))

