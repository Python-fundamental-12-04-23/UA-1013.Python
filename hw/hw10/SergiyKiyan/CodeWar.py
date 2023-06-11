# Create a class Ball. Ball objects should accept one argument for "ball type" when instantiated.
#
# If no arguments are given, ball objects should instantiate with a "ball type" of "regular."

class Ball(object):
    def __init__(self, ball_type='regular'):
        self.ball_type = ball_type

#Color Ghost
import random

class Ghost(object):
  def __init__(self):
    self.color = random.choice(["white", "yellow", "purple", "red"])



# Basic subclasses - Adam and Eve

class Human:
    def __init__(self):
        pass


class Man(Human):
    def __init__(self):
        super().__init__()


class Woman(Human):
    def __init__(self):
        super().__init__()




def God():
    adam = Man()
    eve = Woman()
    return [adam, eve]

humans = God()