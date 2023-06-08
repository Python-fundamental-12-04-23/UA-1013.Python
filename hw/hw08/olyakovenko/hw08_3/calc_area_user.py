from calc_formulas import *


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
