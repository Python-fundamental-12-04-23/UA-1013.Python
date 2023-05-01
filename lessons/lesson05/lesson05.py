import random

#
# l = []
# count = 0
# while len(l) <= 10:
#     temp = random.randint(1, 100)
#     count +=1
#     print(f"{count}\t{temp}", end="\t")
#     if not temp % 2:
#         l.append(temp)
#         print("append")
#     else:
#         print("not append")
# print(l)
# for element in sorted(l):
#     print(element, element**2, element**3)
# for i in range(len(l)):
#     print(l[i], l[i]**2, l[i]**3)
# temp = None
# for i in range(3):
#     print(f"i:{i}")
#     for j in range(3):
#         print(f"\tj:{i}")
#         for k in range(2):
#             temp = i+j+k
#             print(f"\t\tk:{k}")
# print(i, j, k, temp)
# print(list(range(-7, -2)))
# print(range(10))

# for i in range(8):
#     if i%3 == 2:
#         continue
#     print(i)
# else:
#     print("end")
# print("*"*10)
# for i in range(4):
#     print(i)
# else:
#     print("end")
# print("*"*10)
# for i in range(8):
#     if i == 2:
#         break
#     print(i)
# else:
#     print("end")
#
# l = [1,2,3,4,-5]
# is_p = True
# for i in l:
#     if i < 0:
#         is_p = False
# if is_p:
#     print("all elements is positive")
#
# l = [1,2,3,4,5]
# for i in l:
#     if i < 0:
#         break
# else:
#     print("all elements is positive")

# for c in "test":
#     print(c)
#
# d = {"1": 10,
#      "2": 20,
#      "3": 30}
# for key in d:
#     print(key, d[key])
# print(d.items())
# key, value = ('1', 10)
# key = ('1', 10)
# print(key, value)
# for key, value in d.items():
#     print(key, value)
# for item in d.items():
#     print(item)
# from enum import Enum
# class Color(Enum):
#     RED = 1
#     GREEN = 2
# s = "range(5)"
# print(list(enumerate("range(5)")))
# for i, value in enumerate("range(5)"):
#     print(i, value, s[i])
# for i in Color:
#     print(i.value)
#
# Color.RED
# Color.GREEN