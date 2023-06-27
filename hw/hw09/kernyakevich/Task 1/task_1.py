from random import randint

guesses_made = 0
user_name = input('Hello! What is your name?\n')
number = randint(1, 100)

print(f'Well, {user_name}, I am thinking of a number between 1 and 100.')

while guesses_made < 10:
    guess_number = int(input('Take a guess! Enter your number: '))
    guesses_made += 1

    if guess_number == number:
        print(f'Good job, {user_name}! \nYou guessed the number in {guesses_made} attempt! \nYou are a winner!!! \U0001F389')
        break
    elif 1 <= guess_number <= 100 and guess_number < number:
        print('Your number is less \U0001F446')
    elif 1 <= guess_number <= 100 and guess_number > number:
        print('Your number is more \U0001F447')
    elif not 1 <= guess_number <= 100:
        print('Your number is not in the range 1 to 40. Try again \U0001F635')
else:
    print(f"You didn't guess it. Here's the number: {number} \U0001F60F")
