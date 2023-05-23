# Task 1

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(l)
for i in range(len(l)):
    l[i] = str(l[i])
print(l)

# Task 2

n = int(input("Fibonacci:"))
a, b = 0, 1
print(a, b, end=" ")
for i in range(n):
    f = a + b
    print(f, end=" ")
    a = b
    b = f
print()

# Task 3

factorial = int(input("Factorial: "))
fact = 1
if factorial == 0:
    print(1)
else:
    for i in range(1, factorial+1):
        fact = fact * i
        print(fact, end=" ")

