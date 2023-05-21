#task 2 clasic approach
import re

password=input("Enter password to check:")
status = True
if len(password)>16:
    print("Max length of password is 16")
    status=False
if len(password)<6:
    print("Min length of password is 6")
    status = False
if password.find("@")!=-1:
    pass
elif password.find("#")!=-1:
    pass
elif password.find("$")==-1:
    print("Password must contain at least one symbol from - $,#,@")
    status = False
if not any(i.isdigit() for i in password):
    print("Password must contain at least one number")
    status = False
if not any(i.isupper() for i in password):
    print("Password must contain at least one capital letter")
    status = False
print("Password is corrrect" if status else "Password incorrect")



#task 2 RegEx approach
import math

def password_check(password):
    list(password)
    return all([
    re.search(".+[a-z]", password),
    re.search(".+[A-Z]", password),
    re.search("\d", password),
    re.search(".+[$#@]", password),
    re.search(".{6,16}", password),
    ])

    #return result
password=input("Enter password to check:")
print("Password is corrrect" if password_check(password) else "Password incorrect")