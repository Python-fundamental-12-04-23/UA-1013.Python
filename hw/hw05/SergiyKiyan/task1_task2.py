#Task1. Create a list that contains elements of integer type, then
# use the loop to change the type of these elements to a floating
# type.
# (Hint: use the built-in float () function)
elements_of_int=list("3432234324")
print(elements_of_int)
i=0
for x in elements_of_int:
    elements_of_int[i]=float(elements_of_int[i])
 #   elements_of_int[i]=x
 #   print(x,elements_of_int[i],i)
    i+=1
print(elements_of_int)

# Task2. Print Fibonacci numbers up to the entered number n,
# using cycles.
# (Sequence of Fibonacci numbers 0, 1, 1, 2, 3, 5, 8, 13, etc.)

fibonacci_result=input("Enter last number in a fibonacci row: ")
try:
    fibonacci_result=int(fibonacci_result)
except:
    print("Please enter a positive integer, starting with 0")
n1=0
n2=1
count=0
if fibonacci_result<0:
    print("Please enter a positive integer, starting with 0")
else:
    print("Fibonacci row, count starts with  :", 0,end=" ")
    while count<fibonacci_result:
        if fibonacci_result==0:
            print(0,end=" ")
            break
        combination=n1+n2
        n1=n2
        n2=combination
        print(combination,end=" ")
        count+=1



