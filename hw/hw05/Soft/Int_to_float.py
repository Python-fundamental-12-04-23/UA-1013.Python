

def int_to_float(l):
    for i in range(len(l)):
        if isinstance(i, int):
            l[i] = float(i)
    return l

