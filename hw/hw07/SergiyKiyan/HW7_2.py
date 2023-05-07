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
