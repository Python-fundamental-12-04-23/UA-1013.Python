print('First Task')
# in the range from 1 to 10 determine
# even numbers that are divisible by 2
# odd numbers which are divisible by 3
# numbers that are not divisible by 2 and 3

list_even_num_div_2 = []
list_odd_num_div_3 = []
list_num_not_div_2_3 = []

for i in range(1, 11):
    if i % 2 == 0:
        list_even_num_div_2.append(i)
    elif i % 3 == 0:
        list_odd_num_div_3.append(i)
    else:
        list_num_not_div_2_3.append(i)

print(list_even_num_div_2)
print(list_odd_num_div_3)
print(list_num_not_div_2_3)


print('Second Task')
# write a script that checks the login that the user enters
# If the login is "First", than greet the users. If the login is different, send an error
# message(need to use loop while)

count = 0
while count < 5:
    login = input('Please, enter your login: ')
    if login == 'First':
        print('Congratulations! You are in!')
        break
    else:
        print('Wrong login. Please try again!')
        count += 1
        if count == 5:
            print('Your account is locked!')
