

__all__ = ["rectangle_area", "triangle_are", "circle_are"]


import math


def rectangle_area(a, b):
    return a * b


def triangle_are(h, a):
    return 0.5 * h * a


def circle_are(r):
    return round(math.pi * pow(r, 2), 1)
