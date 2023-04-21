val = int(input('Please, enter the temperature in Celsius: '))

print(f'Enter the temperature in Celsius: {val}')
far_t = round((val*9/5)+32)
if val < -273.15:
    print('Error: Temperature below absolute zero (-273.15°C)')
else:
    print(f'{val}°C is equivalent to {far_t}°F')
