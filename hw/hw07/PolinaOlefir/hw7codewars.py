#Task1
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)

print('---------------------------------------------')

#Task2
def distance(x1, y1, x2, y2):

    X = x2-x1
    Y = y2-y1
    return round(((X**2 + Y**2)**0.5),2)

print('---------------------------------------------')

#Task3
def filter_words(st):

    return st.capitalize()

print('---------------------------------------------')

#Task4
def number_to_string(num):

    return str(num)

print('---------------------------------------------')

#Task5
def reverse(st):

    s = st.split(" ")
    st = " ".join(reversed(s))
    return st


print('---------------------------------------------')

#Task6
def reverse_list(l):

    return list(reversed(l))

print('---------------------------------------------')

#Task7
def solution(number):
    sum = 0
    if number < 0:
        return 0
    for i in range(1, number):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum


print('---------------------------------------------')

#Task8
def zero_fuel(distance_to_pump, mpg, fuel_left):

    d_real = mpg * fuel_left
    if d_real >= distance_to_pump:
        return True
    else:
        return False


print('---------------------------------------------')

#Task9
def are_you_playing_banjo(name):

    if name[0] == "R" or name[0] == "r":
        return name + " plays banjo"
    else:
        return name + " does not play banjo"


print('---------------------------------------------')

#Task10
def bool_to_word(boolean):

    return "Yes" if boolean == True else "No"

print('---------------------------------------------')


#Task11
def count_sheeps(sheep):
   return sheep.count(True)

print('---------------------------------------------')


#Task12
def correct_tail(body, tail):
    if body[-1] == tail:
        return True
    else:
        return False