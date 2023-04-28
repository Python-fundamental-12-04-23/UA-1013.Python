# First task
a = int(input('first number '))
b = int(input('second number '))

if a > b:
    print(f"{a} > {b}")
elif a < b:
    print(f"{a} < {b}")
else:
    print(f"{a} = {b}")


# Second task
num = int(input('enter a number '))

if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")


# Third task / "Temperature Converter"

c = float(input('enter a temperature in Celsius '))

f = (c * 9/5) + 32

abs_zero = -273.15

if c >= abs_zero:
    print(f"{c}°C is equivalent to {f}°F ")
elif c < abs_zero:
    print(f"Error: Temperature below absolute zero ({abs_zero}°C)")
