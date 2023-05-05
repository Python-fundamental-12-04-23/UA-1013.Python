import math
# first task
def largest(*args):
    """
    This function finds and return the largest of two given numbers
    You shouln`t pass as argument more than two numbers!
    """
    if len(args) > 2:
        return "You can pass only two numbers!"
    return max(args)
# -------------------------

# second task
def main():
    PI = 3.14

    def circle_area(r):
        nonlocal PI
        return PI * pow(r, 2)
    
    def rect_area(l, b):
        return l * b
    def triangle_area(b, h):
        return b * h / 2
    
    command = input("Hello, user! I can calculate the area of circle, triangle and rectangle!\nWhich figure`s area do you want me to find? \n")

    if command == 'triangle' or command == 'rectangle':
        a = int(input(f"Nice, now give me the {'base' if command == 'triangle' else 'length'} of the {command}: "))
        b = int(input(f"And {'height' if command == 'triangle' else 'width'}, please: "))
        area = triangle_area(a, b) if command == 'triangle' else rect_area(a, b)
        print(f"The area of your {command} is {area}")
    elif command == 'circle':
        radius = int(input("Please give me the radius of your circle: "))
        area = circle_area(radius)
        print(f"The area of your {command} is {area}")
    else:
        print("Sorry, I cannot calculate this figure")

# ---------------

# third task

def letters(string):
    d = {l: string.count(l) for l in string}
    return d

# -------------------