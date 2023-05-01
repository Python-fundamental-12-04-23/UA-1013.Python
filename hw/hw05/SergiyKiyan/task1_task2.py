#Task1. Create a list that contains elements of integer type, then
# use the loop to change the type of these elements to a floating
# type.
# (Hint: use the built-in float () function)
elements_of_int=['3','4','3','str','2','3','4','3','not_int','4']
print(elements_of_int)
i=0
for x in elements_of_int:
    try:
        elements_of_int[i]=float(elements_of_int[i])
    except:
        elements_of_int[i] = elements_of_int[i]
    i+=1
print(elements_of_int)



# Task2. Print Fibonacci numbers up to the entered number n,
# using cycles.
# (Sequence of Fibonacci numbers 0, 1, 1, 2, 3, 5, 8, 13, etc.)

fibonacci_result=input("Enter last number in a fibonacci row: ")
fibonacci_result=int(fibonacci_result)

n1=0
n2=1
count=0
if fibonacci_result<0:
    print("Please enter a positive integer, starting with 0")
elif fibonacci_result==1:
    print("Fibonacci row, count starts with  :", n1)

else:
    print("Fibonacci row, count starts with  :", end=" ")
    while count<=fibonacci_result:
        if fibonacci_result==0:
            print(0,end=" ")
            break
        print(n1, end=" ")
        combination=n1+n2
        n1=n2
        n2=combination
        count+=1



#Task 3
# write a script to calculate the factorial of entered numbers
# Ex: 0!=1, 1!=1, 2!=2, 3!=1*2*3=6


print('\n')
factorial_result=input("Enter last number for a factorial: ")
factorial_result=int(factorial_result)
n1=1
count=1
if factorial_result<0:
    print("Please enter a positive integer, starting with 0")
elif factorial_result==0:
    print("Factorial result  :", n1)
else:
    while n1<=factorial_result:
        count=n1*count
        n1+=1
        print("Factorial result: ",count)








