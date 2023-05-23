def check_password(password):
    count = 0
    flag = False
    if 6 <= len(password) <= 16:
        count += 1
    for i in range(len(password)):
        if (65 <= ord(password[i]) <= 90) or (97 <= ord(password[i]) <= 122):
            flag = True
    if flag == True:
        count += 1
        flag = False
    for i in range(len(password)):
        if 48 <= ord(password[i]) <= 57:
            flag = True
    if flag == True:
        count += 1
        flag = False
    for i in "$#@":
        if i in password:
            flag = True
    if flag == True:
        count += 1
        flag = False
    return count == 4


print(check_password("b4asfaF@$"))
