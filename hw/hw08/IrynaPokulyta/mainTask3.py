import Task3 

while True:
    area_type = int(input("Which area do you want to calculate, rectangle(1), triangle(2), circle(3)?. Enter any number 1, 2, 3 or 0 to quit. "))
    if area_type == 1:
        width = input("Enter width of a rectangle ")
        height = input("Enter height of a rectangle ")
        print("Area of rectangle is equal " + str(Task3.area_rectangle(int(width), int(height))))
    elif area_type == 2:
        base = input("Enter base of a triangle ")
        height = input("Enter height of a triangle ")
        print("Area of triangle is equal " + str(Task3.area_triangle(int(base), int(height))))
    elif area_type == 3:
        radius = input("Enter radius of a circle ")
        print("Area of circle is equal " + str(Task3.area_circle(int(radius))))
    else:
        break