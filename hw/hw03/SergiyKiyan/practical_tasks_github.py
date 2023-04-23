# practical tasks / [github]
# Task1
# You need to write Python's philosophy in the string format:
# - find separately the number of occurrences of the words
# - "better", "never" and "is" in the given line
# - you need to display all text in uppercase (all letters in uppercase)
# - replace all occurrences of the symbol “i” with “&”


# s="Beautiful is better than ugly. \
#     ▪ Explicit is better than implicit. \
#     ▪ Simple is better than complex. \
#     ▪ Complex is better than complicated.\
#     ▪ Flat is better than nested.\
#     ▪ Sparse is better than dense.\
#     ▪ Readability counts.\
#     ▪ Special cases aren't special enough to break the \
#     rules.\
#     ▪ Although practicality beats purity.\
#     ▪ Errors should never pass silently.\
#     ▪ Unless explicitly silenced.\
#     ▪ In the face of ambiguity, refuse the temptation to \
#     ▪ guess.\
#     ▪ There should be one-- and preferably only one --\
#     obvious way to do it.\
#     ▪ Although that way may not be obvious at first \
#     unless you're Dutch.\
#     ▪ Now is better than never.\
#     ▪ Although never is often better than *right* now.\
#     ▪ If the implementation is hard to explain, it's a bad \
#     idea.\
#     ▪ If the implementation is easy to explain, it may be \
#     a good idea.\
#     ▪ Namespaces are one honking great idea -- let's do \
#     more of those\
# "
# print(" occurrences of the words- better ", s.find("better"), "\n", "occurrences of the words- never", s.find("never"), "\n", "occurrences of the words- is", s.find("is"))
# s=s.upper()
# s=s.replace("I", "&")
# print(s)

# Task2
# A four-digit natural number is specified:
# - find the product of the digits of this number
# - write the number in reverse order
# - in ascending order, you need to sort the numbers included in the given number

s=input("Input 4 digit number: ")

product=[int(x) for x in str(s)]
multy=product[0]*product[1]*product[2]*product[3]
print("product of the digits - ",multy)