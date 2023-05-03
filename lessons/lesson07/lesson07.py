# """
#  dbvsvjhfdsbivfhdvu
# """
# A = 156
# A_B = bin(156)
# print(A_B)
# print(int(A_B[2:], 2))
#
# def f_sum(args):
#     """
#     my fsum
#     :param a:
#     :return:
#     """
#     return args+ args
#
#
# def f_print(a):
#     print(a)
#
#
# print("f_sum", f_sum(15))
# print("f_print", f_print(15))
#
# help(sum)
# help(f_sum)
# print(f_sum.__doc__)
#
# def my_f(n):
#     for i in range(1, 10):
#         for j in range(1, 10):
#             for k in range(1, 10):
#                 if i*j*k > 10:
#                     return (i, j, k, i*j*k, i*j*k)
#                 print(i, j, k, i*j*k)
# f = my_f(3)
# print(f)
#
# def my_f(a, b):
#     return a ** b
#
#
# print(my_f(2, 3))
# print(my_f(3, 2))
# print(my_f(b=3, a=2))
#
# # print(my_f(c=3, a=2))
# # print(my_f(2, 3, 4))
# # print(my_f(2))
# def print_info(name, age=18):
#     print("Name: ", name)
#     print("Age: ", age)
#     print()
# print_info("Liubomyr")
# print_info("Liubomyr", 37)
# print_info(age=99, name="Liubomyr")
# print_info("Liubomyr")
# def print_info(name, sex, age=18, city='Lviv'):
#     print("Name: ", name)
#     print("Age: ", age)
#     print("Sex: ", sex)
#     print("City: ", city)
#     print()
#
#
# print(print_info("trest", "elephan", 45))
# # print_info("elephan", 45, name="trest")
# print_info(sex="elephan",
#            age=45,
#            name="trest")
# def my_f(l=[]):
#     l.append((1))
#     print(id(l), l)
#

# my_f() # [1]
# my_f()# [1]
# my_f() # [1]
# my_f([1, 2, 3, 4]) # [1,2,3,4, 1, 1, 1,1]
# my_f() # [1]
# my_f([1, 2, 3, 4][::-1])
#
# def my_f(a, *args, d=1, **kwargs):
#     print(f"{a=} {args=} {d=} {kwargs=}")
#     print(f"{type(args)} {args=} {type(kwargs)}{kwargs=}")
#
#
# my_f(1, 2, 3, 4, 5, 6, 7, 8, d=9, c=15, k=17)
#
#
# def print_info(name, sex, age=18, city='Lviv'):
#     print("Name: ", name)
#     print("Age: ", age)
#     print("Sex: ", sex)
#     print("City: ", city)
#
#     print()
#
#
# l = ("test", "male", 45, "Odesa")
# print_info(l[0], l[1], l[2], l[3])
# print_info(*l)
# d = {
#     "name": "test", "sex": "male", "age": 45, "city": "Odesa"
# }
# print_info(**d)
# print_info(name=d["name"], sex=d["sex"], age=d["age"], city=d["city"], )


# A = 10
#
#
# def my_f():
#     print(dir())
#     print(A)
#
#
# my_f()
# print(A)
# print(dir())
# my_f()
# print(dir())
# print(A)

# A = 10
#
#
# def my_f():
#     # print(dir())
#
#     A = 90
#     print(A)
#
#
# print(A)
# my_f()
# print(A)

# A = 10
#
#
# def my_f():
#     global A
#     A = 90
#     print(A)
#
#
#
# print(A)
# my_f()
# print(A)

# def f():
#     count = 0
#
#     def my_f():
#         nonlocal count
#         count += 1
#         print(count)
#
#     print(count)
#     return my_f
#
# f1 = f()
# f2 = f()
# f1()
# f2()
# f1()
# f3 = f()
#
# def fac1(n):
#     s = 1
#     for i in range(1, n + 1):
#         s *= i
#     return s
#
#
# def fac2(n):
#     n = abs(n)
#     if not n:
#         return 1
#     else:
#         return n * fac2(n - 1)
#
#
# print(fac1(5), fac2(5))
# print(fac1(7), fac2(7))
# print(fac1(7), fac2(7))
# print(fac2(-7))

# a = lambda a, b, c: a + b + c
# print("test")
#
# print(a(1, 2, 34))
# b = a(1, 222, 34)
# print(b)
#
#
# def a(a, b, c):
#     f = ''
#     result = a + b + c
#     return result;
#
#
# def dd(e):
#     return e ** e
#
#
# l = [1, 4, 2, 45, 67, 2]
# ll = map(lambda e: e ** e, l)
# ll2 = map(dd, l)
# print(list(ll))
# print(list(ll2))

def f(x):
    import math
    return {"sin": math.sin(x),
            "cos": math.cos(x)}
t = f(0.8)
print(t)
print(t.get("cos"))