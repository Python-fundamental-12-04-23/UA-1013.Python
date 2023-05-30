print("Part 1")
pyPhilStr = '''1.	Beautiful is better than ugly.
2.	Explicit is better than implicit.
3.	Simple is better than complex.
4.	Complex is better than complicated.
5.	Flat is better than nested.
6.	Sparse is better than dense.
7.	Readability counts.
8.	Special cases aren't special enough to break the rules.
9.	Although practicality beats purity.
10.	Errors should never pass silently.
11.	Unless explicitly silenced.
12.	In the face of ambiguity, refuse the temptation to guess.
13.	There should be one-- and preferably only one --obvious way to do it.
14.	Although that way may not be obvious at first unless you're Dutch.
15.	Now is better than never.
16.	Although never is often better than right now.
17.	If the implementation is hard to explain, it's a bad idea.
18.	If the implementation is easy to explain, it may be a good idea.
19.	Namespaces are one honking great idea! Let's do more of those!'''

print("PYTHON ZEN STATISTICS")
print("Number of occurences of the word 'better' is " + str(pyPhilStr.count('better')))
print("Number of occurences of the word 'never' is " + str(pyPhilStr.count('never')))
print("Number of occurences of the word 'is' is " + str(pyPhilStr.count('is')))
print("PYTHON ZEN IN UPPERCASE")
print(pyPhilStr.upper())
print("PYTHON ZEN REPLACEMENT i -> &")
print(pyPhilStr.replace('i', '&'))

print("Part 2")
fourDigNumber = input("Enter 4-digit number ")
print("Product of its digits is " + str(int(fourDigNumber[0])*int(fourDigNumber[1])*int(fourDigNumber[2])*int(fourDigNumber[3])))
print("Your number in reverse order " + fourDigNumber[::-1])
fourDigNumberList = [fourDigNumber[0], fourDigNumber[1], fourDigNumber[2], fourDigNumber[3]]
fourDigNumberList.sort()
print("Your number in ascending order " + ''.join(fourDigNumberList))

print("Part 3")
firstVar = input("Enter first string ")
secondVar = input("Enter second string ")
print("Your strings: \n" + "First: " + firstVar + "\nSecond: " + secondVar)
firstVar, secondVar = secondVar, firstVar 
print ("Now they swap! \n" + "First: " + firstVar + "\nSecond: " + secondVar)
