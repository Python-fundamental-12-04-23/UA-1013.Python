# list
from copy import deepcopy

# print(dir(list))
# print([i for i in dir(list) if not i.startswith("_")])
# l = []
# print(id(l), l)
# l.append(10)
# l.append([1, 2, 3, 4])
# l.append((1, 2, 3, 4))
# print(id(l), l)
# l.extend((1, 2, 3, 4))
# l.extend({1,2,3})
# l.extend({"a":10, "b":20})
# l.extend({"a":10, "b":20}.items())
# l.extend(1)
# print(id(l), l)
# l.clear()
# print(id(l), l)
# l = []
# print(id(l), l)
# l2 = l.copy()
# l3 = l[:]
# l4 = deepcopy(l)
# print(id(l), l)
# print(id(l2), l2)
# print(id(l3), l3)
# l[0] = 9999
# l2[0] = "test"
# l[1][0] = "foo"
# print(id(l), l)
# print(id(l2), l2)
# print(id(l3), l3)
# print(id(l4), l4)
# print(l.pop())
# print(id(l), l)
# print(l.pop(2))
# # print(l.pop(200))
# print(id(l), l)
# print(l.remove(1))
# print(id(l), l)
# l.reverse()
# print(id(l), l)
# l2 = list(reversed(l))
# print(id(l), l)
# print(id(l2), l2)
#
#
# # sorted()
# # reversed()
# l = [1, 2, 3, 4]
# print(l[1])
# print(l[:])
# print(l[2:])
# print(l[:3])
# print(l[::2])
#
# l = [1, "33", True]
# print(all(l))
# l = [1, "", True]
# print(all(l))
# false = [0, False, None, "", [], (), set(), {}]
# for element in false:
#     print(element)
# for i in range(len(false)):
#     print(i, false[i])
# false_en = enumerate(false)
# print(list(false_en))
# false_en = enumerate("false")
# print(list(false_en))
# for i, element in enumerate(false):
#     print(i, element)
# l = [1, 5, 2, 3, 7, 4, 3]
# print(sorted(l))
# l = [1,5,"2",3,"7",4,3]
# l = "0 one 0 one one"
# temp = []
# for i in l.split():

#     if "0" == i:
#         temp.append(0)
#     elif "one" == i:
#         temp.append(1)
# print(temp)


# def mys(element):
#     return int(element)


# print(sorted(l, key=mys))
# print(sorted(l, key=lambda x: int(x)))
# print([i for i in dir(list) if not i.startswith("_")])
# print([i for i in dir(tuple) if not i.startswith("_")])

# t = tuple("test")
# print(t)
# t = tuple()
# print(t)
# t = ()
# print(t)
# t = (1,)
# print(t)
# print(sorted((1, 2, 5, 2, 3, 4)))
# t = (1, 2, [1, 2])
# t[0] = 15
# t[2][1] = 999
# print(t)
# l = [i for i in range(999)]
# t = tuple(i for i in range(999))
# print(l.__sizeof__())
# print(t.__sizeof__())
# print([i for i in dir(list) if not i.startswith("_")])
# print([i for i in dir(set) if not i.startswith("_")])
#
# s = set("jb'dvkljsdbnv'dxgjdxfbvjhdbsjhvbjdhsvsfjh")
# print(s)
# s = set()
# print(s)
#
# s = {"q", 1, 1, "qq", "q", 1}
# print(s)
# s = {}
# print(type(s), s)
# s.add("ss")
# print(s)
# print(s.pop())
# print(s)
# print(s.remove("qq"))
# print(s)
# s.update("tt")
# s.add("tt")
# print(s)

# print([i for i in dir(dict) if not i.startswith("_")])
# d = dict()
# print(d)
# d = dict((("a", 1), ("b", 2), ("c", 2)))
# print(d)
# d = {}
# print(d)
# d = {"key_1": "nfdsbkbg",
#      "key_2": 12,
#      1: 12}
# print(d)
#
# # d[[1,2]] = 1 #error
# print(d["key_1"])
# print(d.get("key_1"))
# print(d.get("key_11"))
# print(d.get("key_11", []))
# print(d["key_11"])
# dd = d.fromkeys(["dsfds", 1, 12], [1, 2, 3])
# dd["h"] = "dsf"
# print(dd)
# print(dd.popitem())
# print(dd)
# print(dd.pop(1))
# print(dd)
# dd[99] = 15
# dd[68] = 15
# print(dd)
# print(list(enumerate(dd)))
# dd.update({"aa": 1, "bb": 2})
# print(dd)
# print(dd.keys())
# print(dd.values())
# print(dd.items())
# for key in dd:
#      print(key, dd[key])
# for item in dd.items():
#      print(item)
# for key, value in dd.items():
#      print(key, value)
#
# print("key_2" in dd)
# print("aa" in dd)
#
# for key, value in dd.items():
#      if value == [1, 2, 3]:
#           print(key, value)
#
l = [i**2 for i in range(10)]
print(l)
# l = []
# for i in range(10):
#      l.append(i**2)
# s = {i for i in range(10)}
# print(s)
# d = {i:i**3 for i in range(10)}
# print(d)
#
# t = (i for i in range(10))
# print(t)

# l = [i ** 2 for i in range(10)]
# print(l)
# l = [i ** 2 for i in range(10) if i % 2]
# print(l)
# l = [(i, j, k) for i in range(10) for j in range(i)
#      for k in range(i + j) if (i + j + k) % 2]
# print(l)
# l = []
# for i in range(10):
#     for j in range(i):
#         for k in range(i + j):
#             if (i + j + k) % 2:
#                 l.append((i, j, k))
# print(l)
