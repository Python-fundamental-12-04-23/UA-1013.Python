import re


def check_password(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$#]).{6,16}'
    return bool(re.search(pattern, password))
