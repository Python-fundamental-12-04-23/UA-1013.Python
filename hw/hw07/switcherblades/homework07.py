# #task1
def largest_number(a, b):
    """
    :param a int:
    :param b int:
    :return: max number of a or b

    """
    return a if a > b else b
print(largest_number(112, 20))
# #task2
def area_of_rectangle(a, b):
    return a*b

def area_of_triangle(a, h):
    return 0.5*a*h

def are_of_circle(r):
    return 3.14*(r**2)

while True:
    print("Which area you would like to calculate ? Type: rectangle / triangle / circle. If you want stop a program input 'q'")
    user_input = input()
    if user_input == "rectangle":
        print("Please input 'a' and 'b' for rectangle: ")
        a, b = int(input()), int(input())
        print(area_of_rectangle(a, b))

    if user_input == "triangle":
        print("Please input 'a' and 'h' for triangle: ")
        a, h = int(input()), int(input())
        print(area_of_triangle(a, h))

    if user_input == "circle":
        print("Please input 'r' for circle: ")
        r = int(input())
        print(are_of_circle(r))
    if user_input == 'q':
        break
#task3
s = "hello"
empty_dict = {}
count = 0
for i in range(len(s)):
    if s[i] not in empty_dict:
        count += 1
        empty_dict[s[i]] = count
        count = 0
    else:
        count = empty_dict[s[i]]
        count += 1
        empty_dict[s[i]] = count
        count = 0

print(empty_dict)
