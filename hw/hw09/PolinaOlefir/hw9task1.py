import random


number = random.randint(1, 100)


counter = 0
while counter < 10:
  counter += 1
  print("Count is currently " + str(counter))
  guess_number = int(input('Take a guess! Enter your number: '))
  if guess_number == number:
   print("You are a winner!!!")
   break
  elif 1 <= guess_number <= 100 and guess_number < number:
    print('Your number is less.')
  elif 1 <= guess_number <= 100 and guess_number > number:
    print('Your number is more.')
  elif not 1 <=guess_number <= 100:
    print(f"Your number is not in the range 1 to 100. Try again:)")
else:
    print('The number of attempts is used.')