# TASK 1 github

r = range(1, 10)
list_even = [d for d in r if d % 2 == 0]
list_odd = [x for x in r if x % 3 == 0]
list_other = [y for y in r if y % 2 != 0 and y % 3 != 0]

print(list_even)
print(list_odd)
print(list_other)


# OR function
def sort_numbers(start, stop):
    r = range(start, stop)
    list_even = [d for d in r if d % 2 == 0]
    list_odd = [x for x in r if x % 3 == 0]
    list_other = [y for y in r if y % 2 != 0 and y % 3 != 0]
    return (list_even, list_odd, list_other)


print(sort_numbers(1, 10))


# TASK 2 github

login = input("Enter your login: ")

while login != "First":
    print("Error: Incorrect login!")
    login = input("Enter your login again: ")

print("Hello, " + login + "!")
