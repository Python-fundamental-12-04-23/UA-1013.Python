

odd_num = []
even_num = []
other = []

for i in range(1,11):
    if i % 2 == 0:
        even_num.append(i)
    elif  i % 3 == 0:
        odd_num.append(i)
    elif i % 2 != 0 and i % 3 != 0:
        other.append(i)

print(f'Odd numbers:{odd_num} \nEven numbers:{even_num} \nOther numbers:{other}')
