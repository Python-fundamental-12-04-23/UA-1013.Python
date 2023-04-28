

def fibonacci(n):
    fib_nums = []
    a, b = 0, 1

    while a <= n:
        fib_nums.append(a)
        a, b = b, a + b
        print(fib_nums)



