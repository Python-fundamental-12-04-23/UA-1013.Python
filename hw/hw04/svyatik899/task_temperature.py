cels = int(input('Enter the temperature in cels: '))
far = (cels * 9 / 5) + 32
if cels < -273.15:
    print("Temperature below absolute zero (-273.15°C)")
    exit()
print(f"{cels} is equivalent to {far}")