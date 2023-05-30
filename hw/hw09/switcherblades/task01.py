import random
n = random.randint(1, 100)
print('Welcome to the game')

def is_valid(number):
    if number.isdigit():
        return True

def game():
    counter = 0
    while counter != 10:

        print('Enter your number from 1 to 100:',)
        num = input()
        if is_valid(num) == True:

            if 1 <= int(num) <= 100:
                if int(num) < n:
                    counter += 1
                    print('Your number is less than expected')
                    print(f'Tries left {10-counter}')

                if int(num) > n:
                    counter += 1
                    print('Your number is greater than expected')
                    print(f'Tries left {10 - counter}')

                if int(num) == n:
                    print(f"Congrats! You're winner! Tries left {10- counter}")
                    print("Would you like to continue ? y/n")
                    option = input()
                    if option == 'y':
                        game()
                    if option == 'n':
                        break
            else:
                print("Please enter number from 1 to 100")
game()