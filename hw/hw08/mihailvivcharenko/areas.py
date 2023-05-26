from math import pow, pi


def area_of_rectangle(a, b):
    rec_area = a*b
    return rec_area


def area_of_triangle(a, b):
    tri_area = 0.5 * a*b
    return tri_area


def area_of_circle(r):
    cir_area = pi * pow(r, 2)
    return cir_area
