import math

# I
def greet(name):
    return "Hello, my love!" if name == "Johnny" else f"Hello, {name}!"

# II
def distance(x1, y1, x2, y2):
    sum = pow(x2 - x1, 2) + pow(y2 - y1, 2)
    return round(math.sqrt(sum), 2)

# III
def filter_words(st):
    s = st.lower().split()
    j = ' '.join(s).capitalize()
    return j

# IV
def number_to_string(num):
    return str(num)

# V
def reverse(st):
    l = st.split()
    r = l.reverse()
    return ' '.join(l)

# VI
def reverse_list(l):
    r = l[::-1]
    return r

# VII
def solution(number):
    if number < 0:
        return 0
    res = 0
    for x in range(1, number): 
        if x % 3 == 0 or x % 5 == 0: 
            res += x
    return res

# VIII
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return mpg * fuel_left >= distance_to_pump 

# IX
def are_you_playing_banjo(name):
    return f"{name} plays banjo" if name.lower().startswith('r') else f"{name} does not play banjo"

# X
def bool_to_word(boolean):
    return 'Yes' if boolean else 'No'

# XI
def count_sheeps(sheeps):
    count = 0
    for sheep in sheeps:
        if sheep:
            count += 1
    return count

# XII
def correct_tail(body, tail):
    return body[-1] == tail 

