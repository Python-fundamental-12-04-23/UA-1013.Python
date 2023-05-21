# a = "alalal"
# print(id(a), a)
# # a[1] = 'kk'
# # b = a[1:]
# # print(b)
# a = a[1:]
# print(id(a), a)
# a = [1, 2, 3, 4]
# print(id(a), a)
# a.append(99)
# a.extend([1, 2, 3, 4])
# a.append([1, 2, 3, 4])
# print(id(a), a)
#
# i = 1
# s = "stirng"
# d = {"key1": "test",
#      "key2": 99}
# a# print(type(i), type(i) is int, type(i) is str, type(i) is dict)
# print(type(s), type(s) is int, type(s) is str, type(s) is dict)
# print(type(d), type(d) is int, type(d) is str, type(d) is dict)
# print(isinstance(i, int))

# class A:
#      pass
#
# class B(A):
#      pass
#
# a = B()
# print(type(a) is A)
# print(isinstance(a, A))
# print(B.__mro__)

#
# d = {A(): "fjdbk"}
#
# a = A()
# print(a)
# print(id(a))
# print(a.__hash__())
#
# a = 1 + 2 + 3 \
#     + 4 + 5 \
#     + 9
# print(a)
#
# a = (1 + 2 + 3
#      + 4 + 5
#      + 9)
# print(a)
#
# a = ("test1"
#      "test1"
#      "test1")
# print(a)
#
# a = ["test1"
#      "test1",
#      "test1"]
# print(a)
# print('test1',
#       'test2',
#       'test3',
#       end="{}",
#       sep="___")
# a = 1;print(a);b = 1;print(b)
# for a in range(10):
#     print(a)
# a = 1
# b = 2
# c = 3
# a, b, c = 1, 2, 3
# l = [1, 2, 3, 4]
# a, b, c, d = l
#
# l = set(l)
# a, b, c, d = l
# print(a, b, c, d)

#
# t = (1,2,3,4,5)
# print(t[2])
# s = set(t)
# print(3 in s)
# for i in s:
#     print(i)

# print(3 in (1, 2, 34, 5, 3))
#
# a =b = c = "jsdfnlg"
# print(id(a), id(b), id(c), sep='\n')
# print(hash(a), hash(b), hash(c), sep='\n')
#
# t = (1, )
# print(t)
# # t[0] = 1
# t = list(t)

# l = list()
# print(l)
# l = list("test")
# print(l)
# l = []
# print(l)
# l = [1, 2, 3, 4]
# print(l)
#
# t = tuple()
# print(t)
# t = tuple("test")
# print(t)
# t = (1,)
# print(t)
#
# s = set()
# print(s)
# s = set("test")
# print(s)
# s = {1, 2, 3, 4, 1, 2, 3}
# print(s)
# s={}
# print(s, type(s))

# d = dict()
# print(d)
# d = dict([(1, 2), (3, 2)])
# print(d)
# d = {}
# print(d)
# d = {"key": "value",
#      10: "test"}
#
# print(d)

# print((-1)**(0.5))
# print(int("hasfvdj", 32))
# # print(int("hasfvdj", 333))
# import sys
# sys.set_int_max_str_digits(999999)
# print(len(str(99**99999)))
#
# for i in range(90,120):
#      print(i, chr(i))
# for c in  "cbjvhdsb vks":
#      print(c, ord(c))
# a = 99
# print(bin(a))
# print(a)
# print(oct(a))
# print(hex(a))
# print(10+2.5+15)
# print("\u9728nic")
#
# s1 = '''jsdvks
# dvks
# vmlskd
#
# '''
# print(s1)

# f = "%s test %d"
# print(f % ("Liubomyr", 12.5))
# print("{} test {}".format("Liubomyr", 12.5))
# print("{0} test {1} {0}".format("Liubomyr", 12.5))
# print("{name} test {number}".format(name="Liubomyr", number=12.5))
# print("{name} test {number}".format(name="Liubomyr", number=12.5))
# name="Liubomyr"
# number=12.5
# print(f"{name} test {number} {name}")

# s = "programer"
# print(s[0], s[-1])
#
# print(s)
# print(s[0:5])
# print(s[3:5])
# print(s[:5])
# print(s[3:])
# print(s[3::2])
# print(s[-5:3])
# print(s[3:-5])

# s = '<->'.join(['This', 'will', 'join', 'all', 'words', 'into', 'a','string'])
# print(s)
# print(s.split("-"))
# s = "test test,  test"
# print(s.split())
# print(s.find("qq"))
# print(s.find("es"))
# print(s.find("es", 3))
print(__name__)
