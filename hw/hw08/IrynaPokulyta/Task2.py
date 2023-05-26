#Task 2
# write a python program to check validity of a password (input from user ):

# -at least one letter betwen [a-z] and 1 letter betwen [A-Z]
# -at least one number betwen [0-9]
# -at least 1 character from [$#@]
# -minimum length 6 characters
# -maximum length  16 characters

def password_valid(password):
    
    lowercase_check = False
    uppercase_check = False
    number_check = False
    char_check = False
    
    for char in password:
        if char.islower():
            lowercase_check = True
        elif char.isupper():
            uppercase_check = True
        elif char.isdigit():
            number_check = True
        elif char in "$#@":
            char_check = True
    
    if len(password) >= 6 and len(password) <= 16 and lowercase_check and uppercase_check and number_check and char_check:
        print("Your password is valid")
    else:
        print("Your password is not valid")

password_valid(input("Enter a password: "))



