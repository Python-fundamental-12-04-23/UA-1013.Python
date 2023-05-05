

def number_of_char(string):
    """

    :param  string :
    :return: dict

    takes string and return dict with counted char in string

    """
    dict = {}

    for char in string:
        dict[char] = string.count(char)
    return dict


