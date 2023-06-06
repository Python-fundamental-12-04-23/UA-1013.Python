# 1. Write a functions that returns the largest number
# of two numbers. Use docstring

def largest_number_of_two(num1, num2):
    """Function largest_number_of_two returns the largest number
    of two numbers"""
    if num1 > num2:
        return num1
    else:
        return num2


print(largest_number_of_two.__doc__)
print(largest_number_of_two(10, 1))
print(largest_number_of_two(3, 8))


# 2. Write a program that caclulates the area of a rectangle, triangle
# and circle (write three functions to  calculete the area. And call them in the main program,
# depending on the users choice)


def s_rectangle(a, b):
    return a*b


def s_triangle(a, h):
    return 0.5 * a * h


def s_circle(r):
    p = 3.14
    return p*(r**2)


def find_area():
    figure_type = input('please, enter the type of figure: ')

    if figure_type == 'rectangle':
        width = int(input('please, enter width of rectangle: '))
        height = int(input('please, enter height of rectangle: '))
        area = s_rectangle(width, height)
        return area
    elif figure_type == 'triangle':
        base = int(input('please, enter base of triangle: '))
        height = int(input('please, enter height of triangle: '))
        area = s_triangle(base, height)
        return area
    elif figure_type == 'circle':
        radius = int(input('please, enter radius of circle: '))
        area = s_circle(radius)
        return area
    else:
        print('Unknown figure')


# print(find_area())


# 3. Write a function that calculates the number of characters included
# in given string

def calc_characters_in_string(some_str):
    check_dict = {}
    for i in some_str:
        count = some_str.count(i)
        if i not in check_dict:
            check_dict[i] = count
    return check_dict


print(calc_characters_in_string('hello'))
