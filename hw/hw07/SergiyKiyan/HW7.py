#write a function that returns the largest number of two numbers
#use Docstring documenattion strinf in a function

def largest_number(x1,x2):
    """The function that returns the largest number of two numbers"""
    if x1>x2:
        largest=x1
    elif x1==x2:
        print(x1,"=",x2)
        largest="the numbers are equal"

    else:
        largest=x2

    return largest

print(largest_number(555,333))
