from calc_area import *

test = input("Enter the name of the figure (rectangle, triangle, circle) whose area you want to know:")
if test == "rectangle":
    a = float(input("Enter the width:"))
    b = float(input("Enter the length:"))
    print(f"Area of a rectangle with sides {a}, {b} is equal {round(area_of_a_rectangle(a,b),2)}")
elif test == "triangle":
    h = float(input("Enter the height:"))
    a = float(input("Enter the base:"))
    print(f"Area of a rectangle with base {h} and height {a} is equal {round(area_of_a_triangle(h,a),2)}")
else:
    r = float(input("Enter the radius:"))
    print(f"Area of a rectangle with radius {r} is equal {round(area_of_a_circle(r),2)}")
