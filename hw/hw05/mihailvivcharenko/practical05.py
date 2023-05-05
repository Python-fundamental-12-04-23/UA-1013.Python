# Print all even numbers less than 100 (write two variants of the code:
# one using the while loop, and the other using the for loop).

for i in range(100):
    if i % 2 == 0:
        print(i)

w = 100
while w < 100:
    print(w)
    w % 2 == 0


# Print all odd numbers less than 100. (write two versions of the code:
# one using the continue operator,
# and
# the other without this operator).


for i in range(1, 100):
    if i % 2 == 0:
        continue
    print(i)

for i in range(1, 100):
    if i % 2 != 0:
        print(i)


# Check if the list contains odd numbers.
# (Hint: use the break statement)

l = [2, 4, 6, 8, 64]
for num in l:
    if num % 2 != 0:
        print("list containts odd numbers")
        break
else:
    print("the list does not contain odd numbers")


# Task1. Create a list that contains elements of integer type, then
# use the loop to change the type of these elements to a floating
# type.
# (Hint: use the built-in float () function).

l = [1, 2, 5, 8, 3, 45]
print(l)
float_l = []
for i in l:
    float_num = float(i)
    float_l.append(float_num)
print(float_l)


# Task2. Print Fibonacci numbers up to the entered number n,
# using cycles.
# (Sequence of Fibonacci numbers 0, 1, 1, 2, 3, 5, 8, 13, etc.)

n = int(input("Enter a number: "))
a, b = 0, 1
while a <= n:
    print(a)
    a, b = b, a+b
