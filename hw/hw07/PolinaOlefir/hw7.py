#Task1
#a function that returns the largest number of two numbers
def compare_num(x_1, x_2):
    """this function return the largest number"""

    if x_1 > x_2:
        print(f"The largest number among {x_1} and {x_2} is {x_1} ")
    elif x_2 == x_1:
        print(f'The numbers {x_1} and {x_2} are equal.')
    else:
        print(f"The largest number is among {x_1} and {x_2} is {x_2} ")
print(compare_num(5,8))

print('---------------------------------------------')


#Task2
#program that calculates the area of a rectangle, triangle and circle
import math
rectangle = lambda w, l: w*l
triangle = lambda h, b: 1/2*h*b
circle = lambda R: math.pi*(R**2)

test = input("Enter the name of the figure (rectangle, triangle, circle) whose area you want to know:")
if test == "rectangle":
    w = float(input("Enter the width:"))
    l = float(input("Enter the length:"))
    print(f"Area of a rectangle with sides {w}, {l} is equal {round(rectangle(w,l),2)}")
elif test == "triangle":
    h = float(input("Enter the height:"))
    b = float(input("Enter the base:"))
    print(f"Area of a rectangle with base {b} and height {h} is equal {round(triangle(h, b),2)}")

else:
    R = float(input("Enter the radius:"))
    print(f"Area of a rectangle with radius {R} is equal {round(circle(R),2)}")

print('---------------------------------------------')

#Task3
#a function that calculates the number of characters included in given string

def str_to_dict(some_str):
    num_of_characters = {}
    for let in some_str:
        if let not in num_of_characters:
            num_of_characters[let] = 0
        num_of_characters[let] += 1
    return num_of_characters

print(str_to_dict('hello'))
