# l = [i**2 for i in range(5)]
# print(l)
# s = "abcdez"
# z = zip(l, s)
# print(list(z))
# z = zip(s, l)
# print(list(z))
# z = zip(l, s, s)
# print(list(z))
# for i in z:
#     l , s1, s2 = i
# print()
# d = dict(z)
# print(d)
# from itertools import zip_longest
#
# print(list(zip_longest(l, s, fillvalue=999)))
# s = "12, 33, 65"
# l = list(map(int, s.split(",")))
# print(l)
# l = list(filter(lambda e: e % 2, l))
# print(l)
#
#
# def a_add_b(a, b):
#     print("a:{} b:{}".format(a, b))
#     return a + b
# from functools import reduce
#
# print(reduce(a_add_b, [47, 11, 42, 13]))
# print(reduce(a_add_b, [47, 11, 42, 13], -12))
#
# class MyNumbers:
#     def __iter__(self):
#         self.a = 1
#         return self
#
#     def __next__(self):
#         x = self.a
#         self.a += 1
#         if x > 10:
#             raise StopIteration
#         return x
#
#
# for i in iter(MyNumbers()):
#     print(i)
#     # if i > 10:
#     #     break

# t = (i for i in range(5))
# print(type(t), t)
# print(next(t))
# print(next(t))
# print(next(t))
# print(next(t))
# print(next(t))
# print(next(t))

# def my_gen():
#     yield 5
#     yield 2
#     yield 1
# g = my_gen()
# print(g)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# def my_range(start, stop=None, step=1, log=False):
#     if stop is None:
#         number = 0
#         while number < start:
#             if log: print("bf", number)
#             yield number
#             if log: print("af", number)
#             number += step
#
#     else:
#         number = start
#         while number < stop:
#             yield number
#             number += step


# print(list(my_range(5)))
# print(list(my_range(3, 8)))
# print(list(my_range(3, 8, 2)))


# r = my_range(5, log=True)
# print(next(r))
# print(next(r))
# print(next(r))
#
# def f(f="empty"):
#     print(f)
#
#
# f()
# f()
#
#
# @f
# def g():
#     print("g")
#
#
# g
# g
#
# def my_decorator(func):
#     def i(*args):
#         print(func, args)
#         result = func(*args)
#         return result
#
#     print("inner", i)
#     return i
#
#
# class My_decorator():
#     def __init__(self, f):
#         print("create My_decorator")
#         self.func = f
#
#     def __call__(self, *args, **kwargs):
#
#         print(self.func, args)
#         result = self.func(*args)
#         return result
#
#
# def star(func):
#     def inner(*args, **kwargs):
#         print("*" * 30)
#         func(*args, **kwargs)
#         print("*" * 30)
#
#     return inner
#
#
# def percent(func):
#     def inner(*args, **kwargs):
#         print("%" * 30)
#         func(*args, **kwargs)
#         print("%" * 30)
#
#     return inner
#
#
# @star
# @percent
# @my_decorator
# def my_sum(l):
#     return sum(l)
#
#
# def my_sum(l):
#     return sum(l)
# my_sum = my_decorator(my_sum)
#
# print(my_sum)
# print(my_sum(range(10)))
# print(my_sum(range(25, 30)))
#
#
# @percent
# @star
# @my_decorator
# def my_sum2(l):
#     return sum(l)
#
#
# print(my_sum2)
# print(my_sum2(range(10)))
# print(my_sum2(range(25, 30)))
# @percent
# @star
# @My_decorator
# def my_sum3(l):
#     return sum(l)
#
#
# print(my_sum3)
# print(my_sum3(range(10)))
# print(my_sum3(range(25, 30)))


def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)

    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)

    return inner


@star
@percent
def printer(msg):
    print(msg)

printer("Hello")
