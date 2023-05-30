
from helpers import circle_area, rect_area, triangle_area

while True:

    command = input("\nOkey, I can calculate the area of circle, triangle and rectangle!\nWhich figure`s area do you want me to find?\n")

    if command == 'triangle' or command == 'rectangle':
        a = int(input(f"Nice, now give me the {'base' if command == 'triangle' else 'length'} of the {command}: "))
        b = int(input(f"And {'height' if command == 'triangle' else 'width'}, please: "))
        area = triangle_area(a, b) if command == 'triangle' else rect_area(a, b)
        print(f"The area of your {command} is {area}")    
    elif command == 'circle':
        radius = int(input("Please give me the radius of your circle: "))
        area = round(circle_area(radius), 2)
        print(f"The area of your {command} is {area}")
    else:
        print("Sorry, I cannot calculate the area of this figure!")