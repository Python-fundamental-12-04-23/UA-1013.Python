from random import randint

bot = randint(1, 100)
attempt = 10

while attempt > 0:
    answer = int(input("Guess the number! "))

    if answer > bot:
        attempt -= 1
        print(f"Number is too high! Attempts left: {attempt}")
        print("_" * 20)

    elif answer < bot:
        attempt -= 1
        print(f"Number is too low! Attempts left: {attempt}")
        print("_" * 20)

    else:
        print("YOU WON")
        break

if attempt == 0:
    print(f"You ran out of attempts! The number was {bot}. Wish you luck next time!")
