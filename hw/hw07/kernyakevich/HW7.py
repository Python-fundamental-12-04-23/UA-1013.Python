#TASK1

def find_largest_number(num1, num2):
    """
    Returns the largest number among the two given numbers.

    Args:
        num1 (float or int): First number.
        num2 (float or int): Second number.

    Returns:
        float or int: The largest number.
    """
    return max(num1, num2)


#TASK2


import math

def обчислити_площу_прямокутника(довжина, ширина):
    """
    Обчислює площу прямокутника.

    Аргументи:
        довжина (float або int): Довжина прямокутника.
        ширина (float або int): Ширина прямокутника.

    Повертає:
        float: Площа прямокутника.
    """
    return довжина * ширина

def обчислити_площу_трикутника(основа, висота):
    """
    Обчислює площу трикутника.

    Аргументи:
        основа (float або int): Основа трикутника.
        висота (float або int): Висота трикутника.

    Повертає:
        float: Площа трикутника.
    """
    return 0.5 * основа * висота

def обчислити_площу_кола(радіус):
    """
    Обчислює площу кола.

    Аргументи:
        радіус (float або int): Радіус кола.

    Повертає:
        float: Площа кола.
    """
    return math.pi * радіус ** 2

# Основна програма
print("1. Прямокутник\n2. Трикутник\n3. Коло")
вибір = int(input("Введіть ваш вибір (1-3): "))

if вибір == 1:
    довжина = float(input("Введіть довжину прямокутника: "))
    ширина = float(input("Введіть ширину прямокутника: "))
    площа = обчислити_площу_прямокутника(довжина, ширина)
    print("Площа прямокутника:", площа)
elif вибір == 2:
    основа = float(input("Введіть основу трикутника: "))
    висота = float(input("Введіть висоту трикутника: "))
    площа = обчислити_площу_трикутника(основа, висота)
    print("Площа трикутника:", площа)
elif вибір == 3:
    радіус = float(input("Введіть радіус кола: "))
    площа = обчислити_площу_кола(радіус)
    print("Площа кола:", площа)
else:
    print("Недійсний вибір!")


#TASK3

def count_characters(string):
    """
    Calculates the number of characters included in a given string.

    Args:
        string (str): The input string.

    Returns:
        dict: A dictionary containing the count of each character.
    """
    char_count = {}
    for char in string:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

input_string = "hello"
output = count_characters(input_string)
print(output)
