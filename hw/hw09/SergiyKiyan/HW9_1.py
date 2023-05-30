# # Home_work
import random

number = random.randint(1,100)
for counter in range(10):
    guess_number = int(input("Take a quess, enter your number: "))
    if guess_number == number:
        print(f"Good job,! You won")
        break
    if guess_number>number:
        print("The guessed number is less then you entered")
    else:
        print("The guessed number is greater then you entered")
    if counter ==9:
        print("You lost, max attemption is 10")


