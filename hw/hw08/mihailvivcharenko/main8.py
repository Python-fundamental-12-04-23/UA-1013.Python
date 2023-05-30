
import re
from areas import area_of_circle, area_of_rectangle, area_of_triangle


# Task 1
# print(list(filter(lambda s: '__' not in s, dir())))


# Task2.  Write a Python program to check the validity of a password (input from users)
def check_password():
    print('Your password must contain:')
    print('At least 1 letter between [a-z] and 1 letter between [A-Z].')
    print('At least 1 number between [0-9].')
    print('At least 1 character from [$#@]')
    print('Minimum length 6 characters.')
    print('Maximum length 16 characters.')

    password_regexp = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$#@])[A-Za-z\d$#@]{6,16}$"
    password_check_pattern = re.compile(password_regexp)

    while True:
        password = input('Enter password:  ')
        if password_check_pattern.fullmatch(password):
            return "Password is valid"
        else:
            print('Password is not valid. Try again!!')


print(check_password())


# Task3.
# Write a program that calculates the area of a rectangle S=a*b, the area of a
# triangle S=0.5*h*a, the area of a circle S=pi*r**2. This module must be used in
# another module in which we ask the user the area of which figure he wants to
# calculate.


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


# print(calculate_area())
