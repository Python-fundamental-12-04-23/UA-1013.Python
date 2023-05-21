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


def guess_number():
    target_number = random.randint(1, 100)
    attempts = 10

    print("Welcome to the Number Guessing Game!")
    user_name = input('What is your name?')

    print(f'Well, {user_name}, I am thinking of a number between 1 and 100.')

    print("You have 10 attempts to guess the number.")

    while attempts > 0:
        print(f"Attempts left: {attempts}")
        user_guess = int(input("Enter your guess: "))

        if user_guess == target_number:
            print("Congratulations! You guessed the number correctly!")
            return

        if user_guess < target_number:
            print("The number is greater than your guess.")
        else:
            print("The number is less than your guess.")

        attempts -= 1

    print("Game over! You have used all your attempts.")
    print(f"The number I was thinking of was: {target_number}")


guess_number()