#TASK1

a = []
b= []
c = []

for num in range(1, 11):
    if num % 2 == 0:
        a.append(num)
    elif num % 3 == 0:
        b.append(num)
    else:
        c.append(num)

print("Парні числа,що діляться на 2:", a)
print("Непарні числа, що діляться на 3:", b)
print("Числа, що не діляться на 2 і 3:", c)


#TASK2
login = input("Enter your login: ")

while login != "First":
    print("Error: Invalid login.")
    login = input("Enter your login again: ")

print("Welcome, user!")

