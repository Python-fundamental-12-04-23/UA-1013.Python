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
        Although never is often better than right now.
        If the implementation is hard to explain, it's a bad idea.
        If the implementation is easy to explain, it may be a good idea.
        Namespaces are one honking great idea – let's do more of those!
        """
print("Count of 'better' =", text.count("better"))
print("Count of 'never' =", text.count("never"))
print("Count of 'is' =", text.count("is"))
print(text.upper())
text = text.replace("i","&")
#-------------------------------------------
number = input()
result = 1

for i in list(number):
    result *= int(i)
print(result)
print('reversed =', number[::-1])
print('sorted',"".join(sorted(number)))
#-------------------------------------------
a, b = input(), input()
print("a =", a)
print("b =", b)
a, b = b, a
print("new a =", a)
print("new b =", b)