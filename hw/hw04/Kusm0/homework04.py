import sys

celsius = int(input('Enter the temperature in Celsius:'))
if celsius < -273.15:
    print('Error:Temperature below absolute zero (-273.15)')
    sys.exit()
fahrenheit = (celsius * 9 / 5) + 32
print(celsius, '°C is equivalent to', int(fahrenheit), '°F')
