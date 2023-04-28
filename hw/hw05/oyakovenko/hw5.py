# Task1
def change_to_float(some_list):
    len_list = len(some_list)
    for i in range(len_list):
        some_list[i] = float(some_list[i])
    return some_list


print(change_to_float([1, 2, 3, 4, 5, 6]))

# Task2


def print_fibonachi_sequence_up_to(length):
    first = 0
    second = 1
    print(first, second, end=" ")
    length -= 2
    while length > 0:
        print(first + second, end=" ")
        temp = second
        second = first + second
        first = temp
        length -= 1


print_fibonachi_sequence_up_to(10)


# Task3

def find_factorial_without_rec(number):
    fact = 1
    for i in range(2, number+1):
        fact = fact * i
    print('')
    return fact


print(find_factorial_without_rec(3))
