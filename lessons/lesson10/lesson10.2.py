# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __del__(self):
#         # print(f"{id(self)} {self} is deleted")
#         pass
#
#     def __str__(self):
#         return f"x={self.x} y={self.y}"
#
#     def __repr__(self):
#         return f"({self.x}, {self.y})"
#
#     def __add__(self, other):
#         return Point(x=self.x + other.x,
#                      y=self.y + other.y)
#
#     def __lt__(self, other):
#         return self.x < other.x
#
#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y
#
#     def print_instance(s):
#         print(f'{s.x=} {s.y=}')
#
#     def distance(self, poin):
#         return ((self.x - poin.x) ** 2 + (self.y - poin.y) ** 2) ** 0.5
#
#     # def distance(self, point_1, point_2):
#     #     return (((self.x - point_1.x) ** 2 + (self.y - point_1.y) ** 2) ** 0.5 +
#     #             ((point_1.x - point_2.x) ** 2 + (point_1.y - point_2.y) ** 2) ** 0.5)
#
#
# p1 = Point()
# points = []
# for _ in range(10, 0, -1):
#     points.append(Point(_, _))
# print(points)
#
#
# def test():
#     p = Point(1, 2)
#
#
# print(points[2] + points[5])
# # points.sort(key=lambda e: e.x)
# points.sort()
# print(points)
# test()
# # del p1
#
# print(p1)
# # print(p1.distance(points[2], points[5]))
# print(p1.distance(points[2]))
# p1 = Point(1, 2)
# p2 = Point(1, 2)
# print(p1 == p2)
#
#
# class Point3D(Point):
#     def __init__(self, x=0, y=0, z=0):
#         super().__init__(x, y)
#         self.z = z
#
#     def __str__(self):
#         return f"{super().__str__()} z={self.z}"
#
#     def __repr__(self):
#         return f"({self.x}, {self.y}, {self.z})"
#
#
# p3d = Point3D(10, 3, 17)
# print(p3d)
# print([Point3D(), Point3D()])

# class A:
#     @classmethod
#     def name(cls):
#         print(cls.__name__)
# class B(A): pass
# class C(A): pass
# class D(B, C): pass
# class G(A): pass
# class F(C): pass
# class E(G, F, D): pass
# class K(E, G): pass
#
# k = K()
# k.name()
# print(K.__mro__)

#
# class Encapsulation(object):
#     def __init__(self, a, b, c):
#         self.public = a
#         self._protected = b
#         self.__private = c
#
#     def __str__(self):
#         return self.__my_str()
#
#     def __my_str(self):
#         return f"{self.public} {self._protected} {self.__private}"
#
#
# a = Encapsulation(1, 2, 3)
# print(a.__dict__)
# print(a.public)
# print(a._protected)
# print(a._Encapsulation__private)
# print(a)
# print(a._Encapsulation__my_str())

class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def _get_x(self):
        print("get_x", self._x)
        return self._x

    def _set_x(self, x):
        print("set_x", x)

        self._x = x

    x = property(_get_x, _set_x)

    @property
    def y(self):
        print("get_y", self._y)
        return self._y

    @y.setter
    def y(self, y):
        print("set_y", self._y)
        self._y = y

    def __str__(self):
        return f"x={self._x} y={self._y}"


p = Point()
print(p.x)
p.x = 55
print(p.x)
print(p.y)
p.y = 99
print(p)
