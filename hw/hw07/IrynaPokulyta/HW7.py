# Task1
# Write a function that returns the largest of two numbers
# (use DocStrings documentation strings in the function)

def largestnumber (num1, num2):
    """Повертає найбільше число з двох поданих.

    Приклад використання:
    >>> largestnumber(2, 3)
    3

    Параметри:
    num1 (int): Перше число.
    num2 (int): Друге число.

    Повертає:
    int: Найбільше число.
    """
    if num1>num2:
        return num1
    else:
        return num2

print(largestnumber.__doc__)
print(largestnumber(7, 9))

# Task2

# Write a program that calculates the area of a rectangle, triangle and circle
# (write three functions to calculate the area. And call them in the main program 
# depending on the user's choice)

def area_rectangle(width, height):
    return width*height

def area_triangle(base, height):
    return 0.5*base*height

def area_circle(radius):
    return 3.14*radius**2

while True:
    area_type = int(input("Which area do you want to calculate, rectangle(1), triangle(2), circle(3)?. Enter any number 1, 2, 3 or 0 to quit. "))
    if area_type == 1:
        width = input("Enter width of a rectangle ")
        height = input("Enter height of a rectangle ")
        print("Area of rectangle is equal " + str(area_rectangle(int(width), int(height))))
    elif area_type == 2:
        base = input("Enter base of a triangle ")
        height = input("Enter height of a triangle ")
        print("Area of triangle is equal " + str(area_triangle(int(base), int(height))))
    elif area_type == 3:
        radius = input("Enter radius of a circle ")
        print("Area of circle is equal " + str(area_circle(int(radius))))
    else:
        break

# Task2
#Write a function that calculates the number of characters icluded in given string
# -input: "hello"
# -output: {"h": 1, "e": 1, "l": 2, "o": 1}


def number_characters(str):

    characters_count = {}
    for element in str:
        if element in characters_count:
            characters_count[element] += 1
        else:
            characters_count[element] = 1
    return characters_count

print(number_characters("hello"))