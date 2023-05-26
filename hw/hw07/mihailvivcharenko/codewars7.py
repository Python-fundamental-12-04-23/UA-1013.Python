import math

# codewars

# I. Jenny's secret message


def greet(name):

    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)


print(greet('Johnny'))


# II. Find The Distance Between Two Points
def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dist = math.sqrt(dx*dx + dy*dy)
    return round(dist, 2)


# III. No yelling!
def filter_words(st):
    words = st.split()
    words = [words[0].capitalize()] + [word.lower() for word in words[1:]]
    return ' '.join(words)


# IV. Convert a Number to a String
def number_to_string(num):
    num_list = list(str(num))
    num_str = ''.join(num_list)
    return num_str


print(number_to_string(7852))
print(type(number_to_string(7852)))


# V. Reversing Words in a String
def reverse(st):
    l = st.split()
    l.reverse()
    new_st = ' '.join(l)
    return new_st


print(reverse('hello world!!'))


# VI. Reverse List Order
def reverse_list(l):
    'return a list with the reverse order of l'
    l.reverse()
    return l


# VII. Multiples of 3 or 5
def solution(number):
    l = []
    if number <= 0:
        return 0
    for n in range(number):
        if n % 3 == 0:
            l.append(n)
        elif n % 5 == 0:
            l.append(n)
    l_s = sum(l)
    return l_s


print(solution(50))


# VIII. Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    if fuel_left * mpg >= distance_to_pump:
        return True
    else:
        return False


# IX. Are You Playing Banjo?
def are_you_playing_banjo(name):
    l = list(name)
    if l[0].lower() == 'r':
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"


# X. Convert boolean values to strings 'Yes' or 'No’
def bool_to_word(boolean):
    if boolean == True:
        return "Yes"
    else:
        return "No"


# XI. Counting sheep
def count_sheeps(sheep):
    sh_count = sheep.count(True)
    return sh_count


# XII. Is this my tail?
def correct_tail(body, tail):
    sub = body[len(body)-len(tail):]
    if sub == tail:
        return True
    else:
        return False
