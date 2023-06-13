# from pprint import pprint
# # # f1 = open("data1.txt")
# # #
# # # print(f1)
# # # print(f1.read())
# # # print(f1.read())
# # # print(f1.read())
# # # # f1 = open("data1.txt")
# # # f1.tell()
# # # print(f1.readline())
# # # print(f1.readline())
# # #
# # # for t in open("data1.txt"):
# # #     print(t)
# # #
# # # f1.close()
# # #
# # # # f1 = open("data12.txt")
# # # w1 = open("data/data2.txt", "a")
# # # w1.write("test\n")
# # # w1.write("test")
# # # w1.close()
# # # #
# # # # for t in open("data1.txt", "b+"):
# # # #     print(t)
# # #
# # # try:
# # #     file = open("data/data2.txt")
# # #     for line in file:
# # #         print(line)
# # # finally:
# # #     file.close()
# # # # file = open("data/data2.txt")
# # # with open("data/data2.txt") as file:
# # #     for line in file:
# # #         print(line)
# # #
# # #
# # from pprint import pprint
# # with open("data/users.csv") as file:
# #     colums = file.readline().split(",")
# #     d = []
# #     print(colums)
# #     for line in file:
# #         temp = {}
# #         line = line.split(",")
# #         print(line)
# #         for key, data in zip(colums, line):
# #             temp[key] = data
# #         d.append(temp)
# #     pprint(d, indent=4)
# # import csv
# # with open("data/users.csv") as file:
# #     reader = csv.DictReader(file)
# #     for row in reader:
# #         print(row)
#
# import json
# with open("data/user.json") as file:
#     read = file.read()
#     y = json.loads(read)  # parse x
#     print("Data from JSON: ", y)
#     print(type(y))  # the result is a Python dictionary
#     pprint(y, indent=3)
#     print("Age: ", y["age"])
#
# my_dict = {'course':'python','fee':4000,'duration':'60 days', 22 : {'course':'python','fee':4000,'duration':'60 days'}}
#
# j = json.dumps(my_dict)
# print(j)
# d = json.loads(j)  # parse x
# pprint(d, indent=3)

import json


def read_user_json(file_name):
    try:
        with open(file_name) as file:
            read = file.read()
            return json.loads(read)
    except:
        return None
