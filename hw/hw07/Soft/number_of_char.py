

def number_of_char(string):
    """

    :param  string
    :return: dict

    takes string and return dict with counted char in string

    """

    my_dict = {}

    for char in string:
        my_dict[char] = string.count(char)
    return my_dict


