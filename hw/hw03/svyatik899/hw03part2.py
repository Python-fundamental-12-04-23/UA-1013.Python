num = 4321
spysok = []
output =[]
num_2 = int(str(num)[0])
print(num_2)
num_3 = int(str(num)[1])
print(num_3)
num_4 = int(str(num)[2])
print(num_4)
num_5 = int(str(num)[3])
print(num_5)
print(num_2 * num_3 * num_4 * num_5)

print(str(num_5)+str(num_4)+str(num_3)+str(num_2))


res = [int(x) for x in str(num)]
print(res)
for x in str(num):
    spysok.append(int(x))

print(spysok)

while spysok:
    smallest = min(spysok)
    index = spysok.index(smallest)
    output.append(spysok.pop(index))

print(output)

# third task

flexball = 20
laptop = 16
# flexball = flexball + laptop #36, 16
# laptop = flexball - laptop #20
# flexball = flexball - laptop #16
# print(flexball, laptop)

flexball, laptop = laptop, flexball
print(flexball, laptop)