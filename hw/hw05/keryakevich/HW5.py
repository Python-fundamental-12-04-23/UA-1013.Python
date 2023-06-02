#TASK1

integer_list = [1, 2, 3, 4, 5]
float_list = []

for num in integer_list:
    float_num = float(num)
    float_list.append(float_num)

print(float_list)


#TASK2

n = 20  # Приклад 
fibonacci = []

if n == 0:
    fibonacci.append(0)
elif n == 1:
    fibonacci = [0, 1]
else:
    fibonacci = [0, 1]
    a, b = 0, 1
    while a + b <= n:
        fibonacci.append(a + b)
        a, b = b, a + b

print(fibonacci)


#TASK3

n = 5  # Приклад
factorial_value = 1

if n < 0:
    print("Факторіал визначений лише для невід'ємних чисел")
elif n == 0:
    factorial_value = 1
else:
    for i in range(1, n + 1):
        factorial_value *= i

print(factorial_value)

