#Task 1
list_int = [i for i in range(1,20)]
list_float = [float(i) for i in list_int]
print(list_int)
print(list_float)
print('---------------------------------------------')

#Task 2
num = int(input('Enter value:'))
f_0 = 0
f_1 = 1

if num < 0:
    print('A positive number is required.')
else:
    print('Fibonacci numbers up to ' + str(num))
    print(f_0)
    print(f_1)
    for i in range(num+1):
        F_n = f_0 + f_1
        print(F_n)
        f_0 = f_1
        f_1 = F_n


print('---------------------------------------------')

#Task 3
num = int(input('Enter a number to calculate the factorial:'))
fac = 1
if num < 0:
    print('A positive number is required.')
elif num == 0:
    print(f'The factorial of number {num} is {fac}.')
else:
    for i in range(1,num+1):
        fac = fac * i
    print(f'The factorial of number {num} is {fac}.')
