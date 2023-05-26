# Task1. Write a function that returns
# the largest number of two numbers
# (use DocStrings documentation strings in the function).

def largest_number(num1, num2):
    """returns the largest number
        of two numbers

    Args:
        num1 (int): integer number
        num2 (int): integer number

    Returns:
        int: the largest number
    """
    if num1 > num2:
        return f"{num1} is the largest number"
    elif num2 > num1:
        return f"{num2} is the largest number"
    else:
        return f" {num1} and {num2} are equal"


print(largest_number.__doc__)
print(largest_number(2345, 2345))


# Task2. Write a program that calculates the area of a rectangle,
# triangle and circle
# (write three functions to calculate the area, and call them in the
# main program depending on the user's choice).

def area_of_rectangle(a, b):
    rec_area = a*b
    return rec_area


def area_of_triangle(a, b):
    tri_area = 0.5 * a*b
    return tri_area


def area_of_circle(r):
    PI = 3.14
    cir_area = PI * r**2
    return cir_area


def calculate_area():
    print("Which area you wanna calculate? ")
    print("1. rectangle ")
    print("2. trianble ")
    print("3. circle ")

    choice = int(input('choose a number:  '))

    if choice == 1:
        a = float(input('enter width: '))
        b = float(input('enter height: '))
        r_area = area_of_rectangle(a, b)
        return f"the area of rectangle = {r_area}"
    elif choice == 2:
        a = float(input("enter base length: "))
        b = float(input("enter height: "))
        t_area = area_of_triangle(a, b)
        return f"the area of triangle = {t_area}"
    elif choice == 3:
        r = float(input('enter radius: '))
        c_area = area_of_circle(r)
        return f"the area of circle = {c_area}"

    else:
        return "error!!! invalid number"


print(calculate_area())


# Task3. Write a function that calculates the number of characters
# included in a given string
# • input: "hello"
# • output: {"h":1, "e":1,"l":2,"o":1}

def count_characters(string):
    new_dict = {}
    for x in string:
        if x in new_dict:
            new_dict[x] += 1
        else:
            new_dict[x] = 1
    return new_dict


print(count_characters('dewfjwfnnrwefmrkerfeerwerf'))
