# first task
nums = [1, 2, 3, 4, 5, 6]

def create_float(arr):
    res = []
    
    for num in arr:
       res.append(float(num))
    return res

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
    arr = []
    a, res = 1, 1

    while a < x + 1:
        arr.append(a)
        a += 1

    for n in arr:
        res = res * n

    return res

print(factorial(7))
        
       

