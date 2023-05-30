user_password = input("Let's check your password!\nWrite it here: ")


def pass_check(password):
    import string

    status1 = False
    status2 = False
    status3 = False
    status4 = False

    for char in password:
        if char in string.ascii_letters:
            status1 = True

        if char.isdigit():
            status2 = True

        if char in "$#@":
            status3 = True

    if 6 <= len(password) <= 16:
        status4 = True

    if status1 and status2 and status3 and status4:
        return "Password is valid :)"
    else:
        return "Invalid password :("


print(pass_check(user_password))
