# 1
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)

# 2
import math


def distance(x1, y1, x2, y2):
    dist = round(math.sqrt((x2-x1)**2 + (y2-y1)**2), 2)
    return dist


# 3
def filter_words(st):
    lst = st.split()
    new_st = (' '.join(st.split())).capitalize()
    return new_st


# 4
def number_to_string(num):
    return str(num)

# 5
def reverse(st):
    lst = st.split()
    len_l = len(lst)
    new_lst = lst[::-1]
    n_st = ' '.join(new_lst)
    return n_st

# 6
def reverse_list(l):
    return l[::-1]

# 7

def solution(number):
    if number <= 0:
        return 0
    else:
        sum = 0
        i = 1
        while i < number:
            if (i % 3 == 0) or (i % 5 == 0):
                sum += i
            i += 1
        return sum


# 8
def zero_fuel(distance_to_pump, mpg, fuel_left):
    dist_true = mpg * fuel_left
    if dist_true >= distance_to_pump:
        return True
    else:
        return False

# 9

def are_you_playing_banjo(name):
    if name.lower()[0] == 'r':
        name = name + " plays banjo"
    else:
        name = name + " does not play banjo"
    return name


# 10

def bool_to_word(boolean):
    if boolean == True:
        return 'Yes'
    else:
        return 'No'


# 11

def count_sheeps(sheep):
    count = 0
    for i in sheep:
        if i == True:
            count += 1
    return count

# 12

def correct_tail(body, tail):
    if body[-1] == tail[0]:
        return True
    else:
        return False