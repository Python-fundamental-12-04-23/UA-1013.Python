#task 2
password=input("Enter password to check:")
password_symbols=list(password)
print(password_symbols)
if len(password)>16:
    print("Max length of password is 16")
elif len(password)<6:
    print(print("Min length of password is 6"))
#elif