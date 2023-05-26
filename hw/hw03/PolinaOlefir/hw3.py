#Task 1
zen = """
    1.Beautiful is better than ugly.
    2.Explicit is better than implicit.
    3.Simple is better than complex.
    4.Complex is better than complicated.
    5.Flat is better than nested.
    6.Sparse is better than dense.
    7.Readability counts.
    8.Special cases aren't special enough to break the rules.
    9.Although practicality beats purity.
    10.Errors should never pass silently.
    11.Unless explicitly silenced.
    12.In the face of ambiguity, refuse the temptation to guess.
    13.There should be one-- and preferably only one --obvious way to do it.
    14.Although that way may not be obvious at first unless you're Dutch.
    15.Now is better than never.
    16.Although never is often better than *right* now.
    17.If the implementation is hard to explain, it's a bad idea.
    18.If the implementation is easy to explain, it may be a good idea.
    19.Namespaces are one honking great idea -- let's do more of those!
    20.Beautiful is better than ugly.
    21.Explicit is better than implicit.
    22.Simple is better than complex.
    23.Complex is better than complicated.
    24.Flat is better than nested.
    25.Sparse is better than dense.
    26.Readability counts.
    27.Special cases aren't special enough to break the rules.
    28.Although practicality beats purity.
    29.Errors should never pass silently.
    30.Unless explicitly silenced.
    31.In the face of ambiguity, refuse the temptation to guess.
    32.There should be one-- and preferably only one --obvious way to do it.
    33.Although that way may not be obvious at first unless you're Dutch.
    34.Now is better than never.
    35.Although never is often better than *right* now.
    36.If the implementation is hard to explain, it's a bad idea.
    37.If the implementation is easy to explain, it may be a good idea.
    38.Namespaces are one honking great idea -- let's do more of those!Beautiful is better than ugly.
    39.Explicit is better than implicit.
    40.Simple is better than complex.
    41.Complex is better than complicated.
    42.Flat is better than nested.
    43.Sparse is better than dense.
    44.Readability counts.
    45.Special cases aren't special enough to break the rules.
    46.Although practicality beats purity.
    47.Errors should never pass silently.
    48.Unless explicitly silenced.
    49.In the face of ambiguity, refuse the temptation to guess.
    50.There should be one-- and preferably only one --obvious way to do it.
    51.Although that way may not be obvious at first unless you're Dutch.
    52.Now is better than never.
    53.Although never is often better than *right* now.
    54.If the implementation is hard to explain, it's a bad idea.
    55.If the implementation is easy to explain, it may be a good idea.
    56.Namespaces are one honking great idea -- let's do more of those!
"""

print(zen.find('better'))
print(zen.find('never'))
print(zen.find('is'))

zen = zen.upper()
zen= zen.replace('I','&')
print(zen)

#Task 2
four_digit = input('Enter four-digit number: ')
product_of_digits = int(four_digit[0])*int(four_digit[1])*int(four_digit[2])*int(four_digit[3])
print(product_of_digits)
print(f'Number in in reverse order: {four_digit[::-1]}')
sort_num = sorted(four_digit)
print(f'Numbers in ascending order: {"".join(sort_num)}')


#Task 3
first_number = int(input('Enter first number = '))
second_number = int(input('Enter second number = '))
first_number, second_number = second_number,first_number
print(f'After the exchange first_number = {first_number}')
print(f'After the exchange second_number = {second_number}')

