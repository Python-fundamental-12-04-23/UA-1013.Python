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


#Task 7
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

#Task 8
# Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!
#
# The function takes a name as its only argument, and returns one of the following strings:

def are_you_playing_banjo(name):
    if name[0] == "r" or name[0] == "R":
        name = name + " plays banjo"
    else:
        name = name + " does not play banjo"
    # Implement me!
    return name

#Task 9
#Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.
def bool_to_word(boolean):
    return "Yes" if boolean else "No"


#Task 10
#Consider an array/list of sheep where some sheep may be missing from their place.
# We need a function that counts the number of sheep present in the array (true means present).
def count_sheeps(sheep):
    sum=0
    for i in sheep:
        if i:
             sum+=i
    return sum

#Task 11
#Some new animals have arrived at the zoo.
# The zoo keeper is concerned that perhaps the animals do not have the right tails.
# To help her, you must correct the broken function to make sure that the second argument (tail),
# is the same as the last letter of the first argument (body) - otherwise the tail wouldn't fit
#If the tail is right return true, else return false.

def correct_tail(body, tail):
    x=0
    for i in body:
        i=body[x]
        x+=1
    if body[x-1]==tail[0]:
        return True
    else:
        return False
