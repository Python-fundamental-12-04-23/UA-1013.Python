#TASK1
# In the range from 1 to 10 determine:
# even numbers that are divisible by 2
# odd numbers which are divisible by 3
# numbers that are not divisible by 2 and 3


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
newlist = []
for element in list:
    if element%2 == 0:
        newlist.append(element)

print(newlist)

newlist1 = []
for element in list:
    if element%3 == 0 and not element%2 == 0:
        newlist1.append(element)

print(newlist1)

newlist2 = []
for element in list:
    if not element%3 == 0 or not element%2 == 0:
        newlist2.append(element)

print(newlist2)

#TASK2

# Write a script that checks the login that the user enters. 
# If the login is First, then greet the user. If the login is different, send an error message 
# (need to use loop while)

listlogin = input("Enter your login ")

while not listlogin == "First":
    print("Error")
    listlogin = input("Enter your login ")
else:
    print ("Nice to meet you, " + listlogin + "!")

