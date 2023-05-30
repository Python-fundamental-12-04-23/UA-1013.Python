#enter four-digit natural number
m_num = input('Enter four-digit natural number: ')
print('You have entered: ' + m_num)

#find the product of the digits of this number
m_prod = int(m_num[0])*int(m_num[1])*int(m_num[2])*int(m_num[3])
print('The product of the digits of this number is ' + str(m_prod))

#write the number in reverse order
n_num = m_num[::-1]
print('The reverse order of digits of this number is ' + n_num)

#sort the numbers in ascending order
print('This is numbers in ascending order ' + str(sorted(m_num)))

