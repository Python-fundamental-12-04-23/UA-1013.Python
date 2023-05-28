# Task 1. Write a game script that randomly generates a number from a range of
# 1 to 100 and asks the user to guess that number in 10 tries.
# The program reads the numbers entered by the user and prompts the user
# whether the guessed number is greater or less than the number entered by the
# user. The game must continue until the user has used 10 attempts and guessed
# the number. If the user guessed the number, the program prints a
# congratulatory message, and if 10 attempts have been exhausted and the user
# did not have time to guess the number, then the corresponding message is
# displayed.
# (to perform the task, you need to import the random module,
# and from it the randint() function)

import random 

user_name = input("Hello! What is your name? " )
number = random.randint(1, 40)
counter = 0

while True:
    guess_number = int(input("Take a guess, enter your number: "))
    counter = counter +1
  
    if guess_number == number:
        print(f"Good job, {user_name}! You are the winner!")
        break 
    
    if counter == 10: 
        print('You\'ve made ' + str(counter) + ' attempts already. That\'s enough!')
        break
    
    elif 1<=guess_number<=40 and guess_number < number:
        print("Your number is less. Try again.")
  
    elif 1<=guess_number<=40 and guess_number > number:
        print("Your number is more. Try again.")
  
    elif not 1<=guess_number <=40:
        print("Your number is not in range. Try again.") 