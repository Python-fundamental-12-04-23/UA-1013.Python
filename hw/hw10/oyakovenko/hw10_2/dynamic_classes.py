import re


def class_name_changer(cls, newclassname):
    pattern = r"^[A-Z][a-zA-Z0-9_]{1,20}$"
    if re.match(pattern, newclassname):
        cls.__name__ = newclassname
        return cls.__name__
    else:
        raise Exception

