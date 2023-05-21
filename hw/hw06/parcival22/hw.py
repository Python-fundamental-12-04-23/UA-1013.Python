# first task
d = {}

for n in range(1, 11):
    if n % 2 == 0:
        d[n] = 'even'
    elif n % 3 == 0:
        d[n] = 'odd'
    else:
        d[n] = 'not 2 or 3 divisible'

for k, v in d.items():
    print(f"Number {k} is {v}")
         
   
# ----------

# second task

while True:
    login = input('Please login yourself: ')

    if login == 'First':
        print(f"Hello, {login}!")
        break
    else:
        print("Ooops, something went wrong with your login, please try again")


# ----------