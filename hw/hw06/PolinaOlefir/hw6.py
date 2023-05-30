#Task1
#determine
#even numbers that are divisible by 2,
#odd numbers, which are divisible by 3,
# numbers that are not divisible by 2 and 3.

even_num = [i for i in range(1,11) if i%2==0]
num_divisible_by_three = [i for i in range(1,11) if i%3 == 0 and i%2==1]
num_else = [i for i in range(1,11) if i%2 != 0 and i%3 != 0]
print(even_num)
print(num_divisible_by_three)
print(num_else)

print('---------------------------------------------')

#Task2
#checks the login that the user enters

number_of_attempts = 7
count = 0
while count < number_of_attempts:
    count += 1
    print(f'Attempt: {count}')
    login=input('Enter login: ')
    if login == 'First':
        print('Great. It is correct login.')
        break
    else:
        print('Please try again.')
