# Task 1
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = list(filter(lambda x: (x % 2 == 0), list_1))
print("Even numbers that are divisible by 2 are:", result)

result = list(filter(lambda x: (x % 3 == 0), list_1))
print("Odd numbers that are divisible by 3 are:", result)

result = list(filter(lambda x: (x % 2 and x % 3 != 0), list_1))
print("Numbers that are not divisible by 2 and 3 are:", result)

# Task 2
while True:
    log = input("Enter your login: ")
    if log == "First":
        print("Congradulations!")
    else:
        print("Error!")



