C_input = input("Enter the temperature in Celsius: ")
if -273.15 < int(C_input):
    F = (int(C_input) * 9/5)+32
    print(f"{C_input}°C is equivalent to {int(F)}°F")
else:
    print("Error: Temperature below absolute zero (-273.15° C)")