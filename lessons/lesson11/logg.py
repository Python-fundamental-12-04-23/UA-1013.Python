# import logging
#
# logging.basicConfig(filename="log.log",
#                     filemode="a",
#                     level=logging.NOTSET,
#                     format='%(process)d\t%(levelname)s\t%(asctime)s\t%(message)s')
# #
# # logging.debug('This is a debug message')
# # logging.info('This is an info message')
# # logging.warning('This is a warning message')
# # logging.error('This is an error message')
# # logging.critical('This is a critical message')
#
#
# while True:
#     try:
#         a = int(input("a:"))
#         logging.info(f"a:{a}")
#         b = int(input("b:"))
#         logging.info(f"b:{b}")
#         c = a / b
#     except ZeroDivisionError as error:
#         logging.error(f"{error}")
#         c = None
#     except ValueError as error:
#         logging.error(f"{error}")
#         c = None
#     logging.debug(f"a/b={c}")
#     print(f"a/b={c}")

# from subprocess import call
# l = call("java logpars.sh")
# def my_range(n):
#     return  [i for i in range(n)]
# print(type(my_range))
# print(my_range)
# print(my_range(10))
# def my_range(n):
#     i = 0
#     while i < n:
#         print(i)
#         yield i
#         i += 1
# print(type(my_range))
# print(my_range)
# print(my_range(10))
# m = my_range(10)
# next(m)
# next(m)
# next(m)
# next(m)
# next(m)
# next(m)
# next(m)
# next(m)
# next(m)
# next(m)
# next(m)
# next(m)