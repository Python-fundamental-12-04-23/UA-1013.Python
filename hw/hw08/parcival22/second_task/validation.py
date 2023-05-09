import re

while True:

        password = input('Invent your password so I can check it: ')

        if len(password) < 6:
            print('Your password is too short. Password should contain at least 6 characters.')
        elif len(password) > 16:
            print('Your password is too long. Password should contain no more then 16 characters.')
        elif not re.search('[a-z]', password):
            print('Your password should contain at least one letter in range of a to z')
        elif not re.search('[A-Z]', password):
            print('Your password should contain at least one letter in range of A to Z')
        elif not re.search('[0-9]', password):
            print('Your password should contain at least one number in range of 0 to 9')
        elif not re.search('[$#@]', password):
            print('Your password should contain at least one character in range of @, #, and $')
        else:
            print('Congratulations, your password is valid!')
            