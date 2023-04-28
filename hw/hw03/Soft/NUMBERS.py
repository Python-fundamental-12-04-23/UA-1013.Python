def edit_numbers(number):
    product = 1

    while number != 0:
        product = product * (number % 10)
        number = number // 10
    return f"Product of numbers equal to: {product}"


def reversed_number(number):
    reversed_number_string = str(number)[::-1]
    return f"Reversed number equal to: {reversed_number_string}"


def sorted_numbers(list):
    sort_numbers = sorted(list)
    return f"Sorted numbers in ascending order: {sort_numbers}"


print(edit_numbers(123))
print(reversed_number(123))
print(sorted_numbers([1, 10, 5, 100, 9]))
