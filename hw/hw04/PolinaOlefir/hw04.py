# Task 1
# Write a script, which of the two entered numbers will determine which of them is more and which is less.
# Take into account the case of equality of numbers.
first_number = int(input('Enter the first number:'))
second_number = int(input('Enter the second number:'))
if first_number > second_number:
    print("Number " + str(first_number) + " is greater than " + str(second_number))
elif first_number < second_number:
    print("Number " + str(first_number) + " is less than " + str(second_number))
else:
    print("Number " + str(first_number) + " is equal to " + str(second_number))



# Task 2
# Write a script that will check whether the entered number
# is even or odd and display the appropriate message.
number = int(input('Enter a number: '))
if number % 2 == 0:
    print(str(number) + ' is even number')
else:
    print(str(number) + ' is odd number')




# Task 3
#Write a Python program that prompts the user to enter a temperature in
# Celsius and then converts it to Fahrenheit
tem = float(input("Enter the temperature in Celsius: "))
convert = (tem * (9/5) + 32)
absolute_zero = -273.15
if tem < absolute_zero:
    print("Error: Temperature below absolute zero -273.15°C")
else:
    print(str(tem) + " °C is equivalent to " + str(convert) + " °F")