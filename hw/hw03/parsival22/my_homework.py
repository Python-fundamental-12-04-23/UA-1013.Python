# variables
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

number = 5836

# first task

count_of_better = zen.count('better')
count_of_never = zen.count('never')
count_of_is = zen.count('is')
replaced_zen = zen.replace('i', '&')
uppercased_zen = zen.upper()

print(count_of_better,
      count_of_never,
      count_of_is,
      replaced_zen,
      uppercased_zen)

"""substring counting function implementation"""
def find_count(str, substr):
    return str.count(substr)

# second task

str = str(number)
arr = list(str)

product = int(str[0]) * int(str[1]) * int(str[2]) * int(str[3])
print(product)

x = arr.copy()
x.reverse()
reversed = ''.join(x)
print(reversed)

sorted = [int(arr[0]), int(arr[1]), int(arr[2]), int(arr[3])]
sorted.sort()
print(sorted)

"""sorting function"""
def sorter(arr, command):
    for i in arr:
        if i.isdigit() is not True:
            arr.remove(i)
        int(i)
    
    if command == 'reverse':
        return arr.reverse()
    
    elif command == 'sort_ascending':
        return arr.sort()
    
    elif command == 'sort_descending':
        return arr.sort(reverse=True)
    
    elif command == 'product':
        product = 1
        for num in arr:
            if type(num) is 'int':
                product = product * num
        return product

# third task
a = 1
b = 2
a, b = b, a
print(a, b)