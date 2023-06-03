#I

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)


#II

def calculate_distance(x1, y1, x2, y2):
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return round(distance, 2)


#III

def filter_words(string):
    words = string.split()
    filtered_words = []
    for i, word in enumerate(words):
        if i == 0:
            filtered_words.append(word.capitalize())
        else:
            filtered_words.append(word.lower())
    filtered_string = ' '.join(filtered_words)
    return filtered_string


#IV

def int_to_string(num):
    return str(num)


#V

def reverse(st):
    words = st.split()
    return " ".join(words[::-1])


#VI

def reverse_list(lst):
    lst.reverse()
    return lst


#VII

def solution(number):
    if number < 0:
        return 0

    total_sum = 0
    for num in range(number):
        if num % 3 == 0 or num % 5 == 0:
            total_sum += num

    return total_sum

pass



#VIII

def zero_fuel(distance_to_pump, mpg, fuel_left):
    return distance_to_pump <= mpg * fuel_left


#IX

def are_you_playing_banjo(name):
    if name[0].lower() == 'r':
        return name + " plays banjo"
    else:
        return name + " does not play banjo"


#X

def bool_to_word(boolean):
    if boolean:
        return "Yes"
    else:
        return "No"


#XI

def count_sheep(sheep):
    count = 0
    for value in sheep:
        if value:
            count += 1
    return count


#XII

def correct_tail(body, tail):
    if body[-1] == tail:
        return True
    else:
        return False



