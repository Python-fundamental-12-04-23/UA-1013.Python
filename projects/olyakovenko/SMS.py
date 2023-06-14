from twilio.rest import Client
from secure import *


def sending_sms(text, receiver):
    try:
        client = Client(account_sid, auth_tocken)
        message = client.messages.create(
            body=text,
            from_='+16065176314',
            to=receiver
        )
        print('The message was successfully sent')
    except Exception as ex:
        print('Something was wrong ...')
        print(ex)

