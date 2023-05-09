# Task 1
l = [10, 20, 15, 30]
l_float = []
for i in l:
    i = float(i)
    l_float.append(i)
print(l_float)

# Task 2
k = int(input("Enter number of terms "))
a = 0
b = 1
s = 0

for x in range(k):
    print(s, end=" ")
    s = a + b
    b = a
    a = s

# Task 3
n = input("Enter a number: ")
factorial = 1
if int(n) >= 1:
    for i in range(1, int(n)+1):
        factorial = factorial * i
print("Factorail of ", n, " is : ", factorial)