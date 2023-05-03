

login = input("Hi! Write your login here to get access: ")
attempts = 0

while True:
    login2 = input("Confirm your login: ")
    if login2 == login:
        print("Great!")
        break
    else:
        attempts += 1
        if attempts == 3:
            print("Try again later.")
            break
        else:
            print(f"You have {3 - attempts} attempts left")


