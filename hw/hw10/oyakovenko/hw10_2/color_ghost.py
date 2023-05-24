from random import randint


class Ghost:

    color_list = ["white", "yellow", "purple", "red"]

    def __init__(self):
        self.rand_num = randint(0, 3)
        self.color = Ghost.color_list[self.rand_num]


ghost = Ghost()
print(ghost.color)  #=> "white" or "yellow" or "purple" or "red"
