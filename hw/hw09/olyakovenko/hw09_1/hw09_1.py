import random

number = random.randint(1, 100)
number_of_attempts = 10
count_attempt = 1
while count_attempt <= number_of_attempts:
    print(f'Attempt number {count_attempt}')
    num_guess = int(input('Guess the number! Enter your variant: '))
    if number == num_guess:
        print('Right! You won!')
        break
    elif number >= num_guess:
        print('Number is bigger than your variant')
    elif number <= num_guess:
        print('Number is less than your variant')
    count_attempt += 1
    if count_attempt == (number_of_attempts+1):
        print('You lost!')

