#first task
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
