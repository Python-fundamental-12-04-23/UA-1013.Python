#Task 1
# Write a script, which of the two entered
# numbers will determine which of them is
# more and which is less. Take into account
# the case of equality of numbers
determin_number1=input("Input 1st number for comparing: ")
determin_number2=input("Input 2st number for comparing: ")
if determin_number1 > determin_number2:
    print("Number ",determin_number1,"is more then", determin_number2)
elif determin_number1 < determin_number2:
    print("Number ", determin_number1, "is less then", determin_number2)
else:
    print("Number ", determin_number1, "is equal ", determin_number2)

#Task 2
# Write a script that will check whether
# the entered number is even or odd and
# display the appropriate message.

even_or_odd=int(input("Enter number to check it on even or odd: "))
even_or_odd=even_or_odd%2
if even_or_odd==0:
    print("Number is even")
else:
    print("Number is odd")


#Task3. "Temperature Converter"
temperature_in_celsius=float(input("enter a temperature in Celsius to converts it to Fahrenheit: "))
if temperature_in_celsius < -273.15:
    print("Temperature below absolute zero, -273.15°C")
else:
    temperature_in_fahrenheit=(temperature_in_celsius*9/5)+32
    print(temperature_in_celsius, "°C is equivalent to", temperature_in_fahrenheit,"°F")

