

# Basic subclasses - Adam and Eve

def God():
    adam = Man()
    eve = Woman()
    return [adam, eve]


class Human:
    def __init__(self):
        pass


class Man(Human):
    def __init__(self):
        super().__init__()


class Woman(Human):
    def __init__(self):
        super().__init__()


humans = God()
