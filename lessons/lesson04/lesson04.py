# a, b, c = 12, 8, 17
# print(a > b and a < c)
# print(17 >= c > a > b > 0)
# print(not 10)
# print(not 0)
# print(not {})
# print(not {11})
# print(True and 10 and [12, 1])
# print(True and 10 and 0 and [12, 1])
# print(True and 10 and [] and 0 and [12, 1])
# print(False or 10 or [])
# print(False or {} or [])

#
# def get_false(name=0):
#     from random import randint
#     l = [False, None, 0, "", {}, tuple(), []]
#     result = l[randint(0, len(l) - 1)]
#     print("\t f->", result, name)
#     return result
#
#
# def get_true(name=0):
#     from random import randint
#     l = [True, 12, 0.5, [1, 2], {1}, (1, 2, 3), "test"]
#     result = l[randint(0, len(l) - 1)]
#     print("\t t->", result, name)
#     return result
#
#
# print("or:")
# print(get_false() or get_false() or get_false() or get_true() or get_false())
# print("and:")
# print(get_true() and get_false() and get_true())
# print("and:")
# print(get_true(1) and get_false(2) or get_true(3) and get_true(4))
# print("and:")
# print(get_false(1) or get_true(2) and get_false(3) and get_true(4) or get_true(5))
# print("and:")
# print((get_false(1) or get_true(2)) and get_false(3) and (get_true(4) or get_true(5)))

#
# l1 = [10,20]
# l2 = [10,10]
# l3 = l2
# print("l1:", id(l1))
# print("l2:", id(l2))
# print("l3:", id(l3))
# print(l1 == l2)
# print(l1 != l2)
# print(l1 is l2)
# print(l2 is l3)
#
# print(l1 is not l2)
# print(l2 is not l3)
# print(not (l2 is l3))

# for i in range(260):
#     a = i
#     b = (i+1)-1
#     if not id(a) == id(b):
#         print(a, b)

# "1" in 1 #error
# l = [True, 12, 0.5, [1, 2], {1}, (1, 2, 3), "test", 1, 2, 3]
#
# print(12 in l)
# print([1, 2] in l)
# print([1, 2, 3] in l)
# print([1, 2, 3] not in l)
# print("test" in l)
# print("test" in "bsdjhtestadsad")

# l = [True, 12, 0.5, [1, 2], {1}, (1, 2, 3), "test", 1, 2, 3]
# if 12 in l:
#     print("start if:")
#     print(l)
#     print("end if:")
# print("_"*8)
# if 13 in l:
#     print("start if:")
#     print(l)
#     print("end if:")
# print("_"*8)
# if 12 in l:
#     print("start if:")
#     print(l)
#     print("end if:")
# else:
#     print("start else:")
#     print(":(")
#     print("end else:")
# print("_"*8)
# age = int(input("age: "))
# if age <60:
#     if age <18:
#         if age < 13:
#             print("baby")
#         else:
#             print("teenager")
#     else:
#         print("young")
# else:
#     print("old")
# print("_"*8)
#
# if age >= 60:
#     print("old")
# elif age >18:
#     print("young")
# elif age > 13:
#     print("teenager")
# else:
#     print("baby")
#
# print("_"*8)
# for i in range(3):
#     age = int(input("age: "))
#     result = "young" if 60 < age < 90 else "old"
#     # result = 60 < age < 90 ? "young" : "old"
#     print(result)
#
# for i in range(3):
#     age = int(input("age: "))
#     result = None
#     if 60 < age < 90:
#         result = "young"
#     else:
#         result = "old"
#     print(result)
# for i in range(4):
#     age = int(input("age: "))
#     print("baby" if age < 13 else "teenager" if age < 18 else "young" if age < 60 else "old")

# for i in range(4):
#     age = int(input("age: "))
#     match age:
#         case 0 | 1|2|10:
#             print("baby")
#         case 60:
#             print("teenager")
#         # case _:
#         #     print("lunatic")

file = open("zen.txt")
line = file.readline()
while line:
    print(len(line), line)
    line = file.readline()

