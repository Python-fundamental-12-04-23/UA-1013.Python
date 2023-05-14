#task 2
password=input("Enter password to check:")
print(password.find("$"))
password_symbols=list(password)
print(password_symbols)
if len(password)>16:
    print("Max length of password is 16")
if len(password)<6:
    print(print("Min length of password is 6"))
elif not any(i.find("$") for i in password):
    print("Password must contain $")
if not any(i.isdigit() for i in password):
    print("Password must contain at least one number")
if not any(i.isupper() for i in password):
    print("Password must contain at least one capital letter")

