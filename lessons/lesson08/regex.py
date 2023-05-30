import re

st = """Python has a built-in package called re, which can be used to work with Regular Expressions.
Import the re module:
"""
# result = re.match(r"Py", st)
# print(result)
# print(result.group(0))
#
# result = re.search(r"re", st)
# print(result)
# print(result.group(0))
#
# result = re.findall(r"re", st)
# print(result)
#
# pattern = re.compile(r"re")
# print(pattern.findall(st))

print(re.split(r"[ar]", st))

# Write a Python program to check the validity of a password (input from users).
# Validation :
# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.

pattern = re.compile(r"[a-z]+[A-Z]+[0-9]")


def check_password_validity(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$#]).{6,16}$'
    return not (re.match(pattern, password) is None)
    # return all([
    #     re.search("[a-z]", password),
    #     re.search("[A-Z]", password),
    #     re.search("\d", password),
    #     re.search("[$#@]", password),
    #     re.search(".{6,16}", password),
    #     # 6 <= len(password) <= 16,
    #
    # ])
print(check_password_validity("Aa123$%"))
print(check_password_validity("Aa123$%aaa"))
print(check_password_validity("Aa3$"))
print(check_password_validity("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAa123$%"))
print(check_password_validity("Aa123$%"))
