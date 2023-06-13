This program can get all information about waybills from API Nova Poshta and send numbers of this waybills to customers with some information.

For sending SMS to customers you should run file send_messages_via_SMS.py and enter the date when waybills were created.
SMS will be sent to all customers from waybills which were created in current date.

To use this progrmam you should create a new file with name secure.py
In this file you should declare variables and give them values:

account_sid #account_sid for twillio
auth_tocken  #auth_tocken for twillio
key_val # parametr for all requests tocken Nova Poshta
base_url #base url to sent HTTP requests to NP

