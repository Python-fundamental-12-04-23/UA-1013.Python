cels = input('Enter the temperature in Celsius: ')

if int(cels) < -273.15:
    print('Error: Temperature below absolute zero (273.15°C)')
else: 
    far = (int(cels) * 9/5) + 32
    print(f'{cels}°C is equivalent to {far}°F')