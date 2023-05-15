#task 2
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
print("Passwword passing status: ",status)

