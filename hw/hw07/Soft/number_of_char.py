

def number_of_char(string):
    dict = {}

    for char in string:
        dict[char] = string.count(char)
    return dict


