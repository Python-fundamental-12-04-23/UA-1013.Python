import re


def check_password():
    psw = input('Please, enter the password: ')
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$#])[A-Za-z\d@$!%*#?&]{8,16}$'
    if re.match(pattern, psw) is None:
        return False
    else:
        return True


