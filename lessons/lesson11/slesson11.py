# while True:
#     try:
#         a = int(input("a:"))
#         b = int(input("b:"))
#         c = a / b
#     except ValueError:
#         print("a or b is not number")
#     except ZeroDivisionError:
#         print("zero")
#         c = None
#     except ArithmeticError:
#         print("ArithmeticError")
#         c = None
#     except Exception:
#         pass
#
#     print("a/b=", c)
#
# while True:
#     try:
#         a = int(input("a:"))
#         b = int(input("b:"))
#         c = a / b
#     # except ArithmeticError as error:
#     #     print("ArithmeticError", type(error), error)
#     #     c = None
#     # except Exception as error:
#     #     print("Exception", type(error), error)
#     #     c = None
#     except (ArithmeticError, ValueError) as error:
#         c = None
#         a/b
#         print("ArithmeticError, ValueError ->", type(error), error)
#     else:
#         print("Ura")
#     finally:
#         print("finally")
#     print("a/b=", c)

# def f(name):
#     try:
#         print("try")
#         name*2
#     except:
#         return "error"
#     else:
#         print("else")
#         return name
#     finally:
#         print("finally")
#         return name*3
#
# x = f("a")
# print(x)
# def division(a, b):
#     if b <= 0:
#         raise KeyError(f"b < 0, b={b}")
#     return a/b
#
# try:
#     division(5, 0)
# except KeyError as err:
#     print(err)
# else:
#     print("Bead")

class SergiyError(Exception):
    def __init__(self, data=None):
        if data:
            self.data = data
        else:
            self.data = "SergiyError"
class SergiyError2(SergiyError):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return str(type(self)) + repr(self.data)


def division(a, b):
    if b == 0:
        raise SergiyError()
    elif b<0:
        raise SergiyError2("s2")
    return a/b

try:
    division(5, 0)
except SergiyError as err:
    print(err.__repr__())
else:
    print("Bead")
