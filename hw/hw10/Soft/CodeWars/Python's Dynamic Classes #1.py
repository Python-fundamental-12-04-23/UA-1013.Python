

# Python's Dynamic Classes #1

def class_name_changer(cls, new_name: str):
    if new_name[0].isupper and new_name.isalnum():
        cls.__name__ = new_name
    else:
        raise Exception('Invalid class name')