#1

text = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

# Find the number of occurrences of "better", "never", and "is"
better_count = text.count("better")
never_count = text.count("never")
is_count = text.count("is")

# Display all text in uppercase
text_upper = text.upper()

# Replace all occurrences of "i" with "&"
text_replaced = text_upper.replace("I", "&")

# Print the results
print(f"Occurrences of 'better': {better_count}")
print(f"Occurrences of 'never': {never_count}")
print(f"Occurrences of 'is': {is_count}")
print(f"\nText in uppercase:\n{text_upper}")
print(f"\nText with 'i' replaced with '&':\n{text_replaced}")

#2

print(f"Product of digits: {product}")

# Reverse the number
reverse_number = number[::-1]
print(f"Number in reverse order: {reverse_number}")

# Sort the digits in ascending order and form the number
sorted_number = ''.join(sorted(number))
print(f"Number in ascending order: {sorted_number}")

number = 1234

# Find the product of the digits of the number
product = 1
for digit in str(number):
    product *= int(digit)

# Write the number in reverse order
reverse_number = int(str(number)[::-1])

# Sort the digits in the number in ascending order
sorted_number = int("".join(sorted(str(number))))

# Interchange the values of two variables without using the third variable
a = 5
b = 10

a, b = b, a

print(f"Product of digits of {number}: {product}")
print(f"Reverse of {number}: {reverse_number}")
print(f"Digits of {number} sorted in ascending order: {sorted_number}")
print(f"a: {a}, b: {b}")

#3

a = 1
b = 2
a, b = b, a
print(a, b)

