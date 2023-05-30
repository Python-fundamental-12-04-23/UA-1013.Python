# class MyType:
#     pass
# class MyType():
#     pass
# class MyType(OtherClasss):
#     pass
# class MyType:
#     """
#     this is MyClass
#     """
#     pass
#
# print(MyType.__doc__)
#
# print(type(MyType))
# my1 = MyType()
# my2 = MyType()
#
#
# print(type(my1))
# print(type(my2) is MyType)
# print(isinstance(my1, MyType))
# print(isinstance(my1, object))
# class MyClass:
#     cm = []
#     ci = 10
#     def __init__(self):
#         self.ii = 999
#         self.im = [1]
# obj1 = MyClass()
# obj2 = MyClass()
#
# print(obj1.cm, obj1.ci, obj1.ii, obj1.im)
# print(obj2.cm, obj2.ci, obj2.ii, obj2.im)
# obj1.im.append(99)
# obj2.im.append("jhdsv")
# obj1.ii = 888
# obj2.ii = "test"
# print(obj1.cm, obj1.ci, obj1.ii, obj1.im)
# print(obj2.cm, obj2.ci, obj2.ii, obj2.im)
# obj1.cm.append("Class")
# obj1.ci = "user"
#
# MyClass.ci = 200
# print(obj1.cm, obj1.ci, obj1.ii, obj1.im)
# print(obj2.cm, obj2.ci, obj2.ii, obj2.im)
# obj3 = MyClass()
# print(obj3.cm, obj3.ci, obj3.ii, obj3.im)
# print(dir(obj2))
# print(obj1.__dict__)
# print(obj2.__dict__)
# print(obj3.__dict__)
# print(MyClass.__dict__)



# class A:
#     def echo(self):
#         print("echo", type(self), id(self), self)
#     @classmethod
#     def echo_class(cls):
#         print("echo_class", type(cls), id(cls), cls)
#     @staticmethod
#     def echo_static():
#         print("fooBoo")
# print(id(A), A)
# a1 = A()
# a1.echo()
# a1.echo_class()
# A.echo_class()
# a1.echo_static()
# A.echo_static()

# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def print_instance(s):
#         print(f'{s.x=} {s.y=}')
#
#     def distance(self, poin):
#         return ((self.x - poin.x) ** 2 + (self.y - poin.y) ** 2) ** 0.5
#
#
# p1 = Point(10, 20)
# p1.print_instance()
#
#
# def double_value(obj):
#     obj.x *= 2
#     obj.y *= 2
#
#
# Point.double = double_value
# double_value(p1)
# p1.double()
# p1.print_instance()
# Point.print_instance(p1)
# p = Point.print_instance
# p(p1)
# p2 = Point(40, 90)
# print(p1.distance(p2))
#
# # class Point2:
# #     pass
# # p22 = Point2()
# # p22.x = 2
# # p22.y = 2
# # p23 = Point2()
# # p23.x = 2
# # p23.y = 2


