import shutil
txt_path = r'E:\workspace\pycharm_projects\pythonFundamental\UA-1013.Python\hw\hw01\switcherblades\Zen.txt'
dst_path = r'E:\workspace\pycharm_projects\pythonFundamental\UA-1013.Python\hw\hw03\switcherblades'
shutil.copy(txt_path, dst_path)
with open("Zen.txt") as file:
    text = file.read()
print("Count of 'better' =", text.count("better"))
print("Count of 'never' =", text.count("never"))
print("Count of 'is' =", text.count("is"))
#-------------------------------------------
number = input()
result = 1

for i in list(number):
    result *= int(i)
print(result)
print('reversed =', number[::-1])
print('sorted',"".join(sorted(number)))