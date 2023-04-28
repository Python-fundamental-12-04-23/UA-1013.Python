#open file with text (file should exists in the same directory with the current script)
f = open("Zen.txt", "r")
f_string = f.read()

#find the number of occurrences of the words and print
find_better = f_string.find('better')
find_never = f_string.find('never')
find_is = f_string.find('is')
print(find_better)
print(find_never)
print(find_is)

#display all text in upper case
print(f_string.upper())
print('===========================  end of the text =============================== ')
# replace all occurrences of the symbol 'i' with '&' and display text in upper case
new_string = f_string.replace("i", "&")
print(new_string.upper())



