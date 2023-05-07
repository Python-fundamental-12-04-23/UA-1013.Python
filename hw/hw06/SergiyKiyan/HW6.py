#Task 1. In the range from 1 to 10 frtermaine:
# even number that a divisible by 2
# odd munber whicj are divisible by 3
# number that are not divisible by 2 and 3

for x in range(1,11):
    if not x%2:
        print("It is even number divisible by 2 :  ",x)
    elif not x%3:
        print("It is odd number divisible by 3 :  ",x)
    else:
        print("number that are not divisible by 2 and 3 : ",x)


# Task2. Write a script that checks the login that the user enters.
# If the login is "First", then greet the users. If the login is
# different, send an error message.
# (need to use loop while

print()
login=input("Enter login name: ")
true_login="First"
while login!=true_login:
    print("login is not correct, please try again")
    login = input("Enter login name: ")
print("Greeting, login name is correct")
