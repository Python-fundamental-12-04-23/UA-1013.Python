# Jenny's secret message


def greet(name):
    if name == "Johnny":
        return f"Hello, my love!"
    else:
        return f"Hello, {name}!"


# Simple: Find The Distance Between Two Points


def distance(x1, y1, x2, y2):
    import math
    res = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return round(res, 2)

# No yelling!


def filter_words(st):
    st = st.lower()
    res = st.split()
    res[0] = res[0].capitalize()
    return " ".join(res)


# Convert a Number to a String!


def number_to_string(num): return str(num)

# Reversing Words in a String


def reverse(st):
    res = st.split()
    res.reverse()
    return " ".join(res)

# Reverse List Order


def reverse_list(l):
    return l[::-1]

# Multiples of 3 or 5


def solution(number):
    new_l = []
    for char in range(number):
        if char < 0:
            return 0
        elif char > 0:
            if char % 3 == 0 or char % 5 == 0:
                new_l.append(char)
    return sum(new_l)

# Will you make it?


def zero_fuel(distance_to_pump, mpg, fuel_left):
    if distance_to_pump / mpg > fuel_left:
        return False
    else:
        return True

# Are You Playing Banjo?


def are_you_playing_banjo(name):
    if name.startswith("R") or name.startswith("r"):
        return name + " plays banjo"
    else:
        return name + " does not play banjo"

# Convert boolean values to strings 'Yes' or 'No'


def bool_to_word(boolean): return "Yes" if boolean else "No"

# Counting sheep...


def count_sheeps(sheep):
    present = 0
    for i in sheep:
        if i == True:
            present += 1
    return present

# Is this my tail?


def correct_tail(body, tail):
    if body.endswith(tail):
        return True
    else:
        return False

