# def area_of_rectangle(a,b):
#     """The function that returns the area of a rectangle"""
#     return a*b
#
# def area_of_triangle(a,b):
#     """The function that returns the area of a triangle"""
#     return a*b/2
#
# def area_of_circle(r):
#     """The function that returns the area of a circle """
#
# #    PI=3.14
#     return math.pi*pow(r,2)



import calculates_the_areas
user_choise=int(input("Choose the a shape to calculate the area: 1 is rectangle, 2 is triangle, 3 is circle: "))
if user_choise==1:
    a=float(input("enter lenth of a rectangle side 1: "))
    b=float(input("enter lenth of a rectangle side 2: "))
    print("area of rectangle is ", calculates_the_areas.area_of_rectangle(a,b))
elif user_choise==2:
    a = float(input("enter lenth of a triangle side 1: "))
    b = float(input("enter lenth of a triangle side 2: "))
    print("area of triangle is ", calculates_the_areas.area_of_triangle(a, b))
elif user_choise==3:
    r = float(input("enter lenth of a circle radius: "))
    print("area of circle is ",calculates_the_areas.area_of_circle(r))

else:
    print("Unfrecognized shape for calculation, please enter number for 1 to 3")
print()

