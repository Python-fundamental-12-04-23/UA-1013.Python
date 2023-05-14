#task 2
password=input("Enter password to check:")
password_symbols=list(password)
print(password_symbols)
if len(password)>16:
    print("Max length of password is 16")
if len(password)<6:
    print("Min length of password is 6")
if password.find("@")==-1:#or password.find("#")==-1 or password.find("@")==-1:
    print("Password must contain at least one symbol from - $,#,@")
if not any(i.isdigit() for i in password):
    print("Password must contain at least one number")
if not any(i.isupper() for i in password):
    print("Password must contain at least one capital letter")
print(password.find("$"))

