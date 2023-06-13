from SMS import *
from np_api import NpApi
from datetime import datetime
from secure import *
import time
import os


#get date from console start
cur_date = input("Enter date from what you want to get information in format 05.05.2023. If you want to use current date - enter +: ")

if cur_date == '+':
    now = datetime.now()
    cur_date = now.strftime("%d.%m.%Y")
    print(cur_date)
else:
    try:
        valid_date = time.strptime(cur_date, '%d.%m.%Y')
    except ValueError:
        print(f'You enter invalid date! - {cur_date}')
        raise ValueError

# get response_from_api and send message via viber
responce_np = NpApi.get_information_from_np(key_val, cur_date, base_url)
check = responce_np.json()
dt = check.get('data')
print(dt)

#name of file where we will write information
dir = os.path.abspath(os.curdir)
filename = 'info_po_nakladnum_' + cur_date + '.txt'
f_name = dir + '\info_po_nakladnum\\' + filename
print(f_name)

f = open(f_name, 'w')
counter = 1
for i in dt:
    #create string with information for txt file
    str_r = str(counter) + '\n' + 'Доброго дня! Магазин рослин Экзотичний сад. Посилка з рослинами відправлена! Номер накладної: \n' \
            + i['IntDocNumber'] + '\n' + i['CityRecipientDescription'] \
             + '\n' + i['RecipientAddressDescription'] + '\n' + 'Отримувач: '\
            + i['RecipientContactPerson'] + '\n' + i['RecipientContactPhone']\
            + '\n' + 'Дякуємо за замовлення! \n' + '\n\n'

    # create string with information for SMS
    str_to_send = f"exoticsad.com. Posylka z roslynamy vidpravlena. Deklaratsiya: {i['IntDocNumber']}. Diakyemo za zamovlennia!"
    print(str_r)
    print(str_to_send)

    # send_message_via_SMS
    #phone number for test
    sending_sms(str_to_send, '+380934707497')
    # phone number from api response (need to uncomment)
    # sending_sms(str_to_send, i['RecipientContactPhone'])

    #write information in txt file
    f.write(str_r)
    counter += 1
f.close()
