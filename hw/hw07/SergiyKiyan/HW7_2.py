#task 1
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)

#task 3
#Write a function taking in a string like String should be capitalized and properly spaced.
def filter_words(st):
    return st.capitalize()

# task 4
def number_to_string(num):
    return str(num)

#Task 5
# You need to write a function that reverses the words in a given string. A word can also fit an empty string. If this is not clear enough, here are some examples:
#
# As the input may have trailing spaces, you will also need to ignore unneccesary whitespace.
#
# Example (Input --> Output)
def reverse(st):
    st = st.split()[::-1]
    new = " ".join(st)

    return new

#Task 6
#In this kata you will create a function that takes in a list and returns a list with the reverse order.
def reverse_list(l):
    return l[::-1]
    'return a list with the reverse order of l'

#Task 6
# You were camping with your friends far away from home, but when it's time to go back, you realize that your fuel is running out and the nearest pump is 50 miles away! You know that on average, your car runs on about 25 miles per gallon. There are 2 gallons left.
#
# Considering these factors, write a function that tells you if it is possible to get to the pump or not.
#
# Function should return true if it is possible and false if not.

def zero_fuel(distance_to_pump, mpg, fuel_left):
    dist=mpg*fuel_left
    if dist >= distance_to_pump:
        return True
    else:
        return False
