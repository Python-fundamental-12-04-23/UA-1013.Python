

def are_counter(shape, **kwargs):
    """


    float --> float

    returns are of triangle, rectangle or circle

    """
    from math import pi

    if shape == "triangle":
        base = kwargs['base']
        height = kwargs['height']
        area = 0.5 * base * height
        return area

    elif shape == "rectangle":
        length = kwargs['length']
        width = kwargs['width']
        area = length * width
        return area

    elif shape == "circle":
        radius = kwargs['radius']
        area = round(pi * radius ** 2, 1)
        return area

    else:
        return None


print(are_counter("circle", radius=7))
