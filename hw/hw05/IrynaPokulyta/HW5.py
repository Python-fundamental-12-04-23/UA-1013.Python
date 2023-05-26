#TASK 1
#Create a list that contains elements of integer type, 
#then use the loop to change of these elements to a floating type. Use the built-in float() function


integer_list = [-10, 20, -30, 40, -50]

float_list = []
for num in integer_list:
    float_num = float(num)
    float_list.append(float_num)

print("Original integer list:", integer_list)
print(type(integer_list[0]))

print("Converted float list:", float_list)
print(type(float_list[0]))

#=======================================================

#TASK 2
#Print Fibonacci numbers up to the entered number n, using cycles

n = int(input("Enter a number: "))

first = 0
second = 1

print("Fibonacci numbers up to", n, ":")

if n <= 0:
    print("Please enter a positive integer.")
else:
    print(first)  

    while second <= n:
        print(second)

        fib_next = first + second

        first = second
        second = fib_next

#TASK 3
#Write a script that wil calculate the factorial of the entered number without using recursion

number = int(input("Enter a number: "))

if number < 0:
    print("Error: Please enter a non-negative integer.")
    exit()

factorial = 1
for i in range(1, number + 1):
    factorial *= i

print(f"The factorial of {number} is: {factorial}")
