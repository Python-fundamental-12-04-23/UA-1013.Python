int_list = [int(x) for x in range(1, 10)]
float_list = [float(x) for x in int_list]
print(float_list)
#---------------------------------------
n = int(input())
a = 1
y = 0
for i in range(1, n+1):
    b = a
    a = b + y
    y = b
    print(b, end=' ')
#----------------------------------------
n = int(input())
res = 1
if n == 0:
    n = 1
else:
    for i in range(1, n+1):
       res *= i
print(res)
