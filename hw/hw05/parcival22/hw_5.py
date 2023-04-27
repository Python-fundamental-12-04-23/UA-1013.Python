# first task
nums = [1, 2, 3, 4, 5, 6]

def create_float(arr):
    arr[:] = [float(num) for num in arr]
    return arr

print(create_float(nums))

# ---------------------------

# second task

def fibonacci(n):
    count, a, b = 0, 0, 1
    while count < n:
        print(a)
        c = a + b
        a = b
        b = c
        count += 1

fibonacci(10)

# -------------------------

# third task

def factorial(x):
     res = 1

     for n in range(1, x+1):
        res = res * n

     return res

print(factorial(7))
        
       

