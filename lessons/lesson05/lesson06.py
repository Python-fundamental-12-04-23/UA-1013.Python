# list
from copy import deepcopy

print(dir(list))
print([i for i in dir(list) if not i.startswith("_")])
l = []
print(id(l), l)
l.append(10)
l.append([1, 2, 3, 4])
l.append((1, 2, 3, 4))
print(id(l), l)
l.extend((1, 2, 3, 4))
l.extend({1,2,3})
l.extend({"a":10, "b":20})
l.extend({"a":10, "b":20}.items())
# l.extend(1)
# print(id(l), l)
# l.clear()
print(id(l), l)
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
print(l.pop())
print(id(l), l)
print(l.pop(2))
# print(l.pop(200))
print(id(l), l)
print(l.remove(1))
print(id(l), l)
l.reverse()
print(id(l), l)
l2 = list(reversed(l))
print(id(l), l)
print(id(l2), l2)


# sorted()
# reversed()


