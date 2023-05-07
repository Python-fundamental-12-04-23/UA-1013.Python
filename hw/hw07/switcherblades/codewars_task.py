# I
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)


# II
def distance(x1, y1, x2, y2):
    import math
    return round(math.sqrt(((x2 - x1) ** 2) + (y2 - y1) ** 2), 2)


# III
def filter_words(st):
    return " ".join(st.split()).capitalize()


# IV
def number_to_string(num):
    return str(num)


# V
def reverse(st):
    return " ".join([x for x in st.split()[::-1]])


# VI
def reverse_list(l):
    return l[::-1]


# VII
def solution(number):
    sum = 0
    for i in range(number):
        if (i % 3 == 0) or (i % 5 == 0):
            sum += i
    return sum


# VIII
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return distance_to_pump <= (mpg * fuel_left)


# IX
def are_you_playing_banjo(name):
    return name + " plays banjo" if name[0] == 'r' or name[0] == 'R' else name + " does not play banjo"


# X
def bool_to_word(boolean):
    return "Yes" if boolean == True else "No"


# XI
def count_sheeps(sheep):
    count = 0
    for i in range(len(sheep)):
        if sheep[i] == True:
            count += 1
    return count


# XII
def correct_tail(body, tail):
    if body[-1] == tail:
        return True
    else:
        return False
