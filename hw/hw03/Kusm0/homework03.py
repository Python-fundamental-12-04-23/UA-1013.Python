# Task 1
zen = """Beautiful is better than ugly.
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

print(zen.upper())
print(zen.replace('i', '&'))
print(zen.count('better'), zen.count('never'), zen.count('is'))

# Task 2

num = input('4 digit number:')

product = int(num[0]) * int(num[1]) * int(num[2]) * int(num[3])
print(product)

revers = num[::-1]
print(revers)

sort_num = sorted(num)
sort_str = ''.join(sort_num)
print(sort_str)

# Task 3
a, b = 23, 34
a, b = b, a
print(a, b)
