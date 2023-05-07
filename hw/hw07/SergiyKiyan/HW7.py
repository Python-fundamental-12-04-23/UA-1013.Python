#write a function that returns the largest number of two numbers
#use Docstring documenattion strinf in a function

def largest_number(x1,x2):
    """The function that returns the largest number of two numbers"""
    if x1>x2:
        largest=x1
    elif x1==x2:
        print(x1,"=",x2)
        largest="the numbers are equal"

    else:
        largest=x2

    return largest

print(largest_number(555,333))


# Task2. Write a program that calculates the area of a rectangle,
# triangle and circle
# (write three functions to calculate the area, and call them in the
# main program depending on the user's choice)

def area_of_rectangle(a,b):
    return a*b

def area_of_triangle(a,b):
    return a*b/2

def area_of_circle(r):
    PI=3.14
    return PI*r**2

user_choise=int(input("Choose the a chape to calculate the area: 1 is rectangle, 2 is triangle, 3 is circle: "))
if user_choise==1:
    a=float(input("enter lenth of a rectangle side 1: "))
    b=float(input("enter lenth of a rectangle side 2: "))
    print("area of rectangle is ",area_of_rectangle(a,b))
elif user_choise==2:
    a = float(input("enter lenth of a triangle side 1: "))
    b = float(input("enter lenth of a triangle side 2: "))
    print("area of triangle is ", area_of_triangle(a, b))
elif user_choise==3:
    r = float(input("enter lenth of a circle radius: "))
    print("area of circle is ", area_of_circle(r))

else:
    print("Unfrecognized shape for calculation, please enter number for 1 to 3")

