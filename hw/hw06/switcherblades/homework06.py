#task1
evennumbs = [x for x in range(1, 10) if x % 2 == 0]
print(evennumbs)
oddnumbs = [x for x in range(1, 10) if x % 3 == 0]
print(oddnumbs)
notdiv2and3 = [x for x in range(1,10) if (x % 2 != 0) and (x % 3 != 0)]
print(notdiv2and3)
#task2
while True:
    login = input()
    if login == "First":
        print("Welcome")
        break
    else:
        print("Please input correct login")