import datetime
from twilio.rest import Client

# import calendar
# import time

account_sid = 'AC12610635b3abe37c4e2386dfa6fcd471'
auth_token = '77f5de5b52dd61e15d42e1b44df8a7b1'  

myPhone = '+14237736938'
TwilioNumber = '+12766442244'

client = Client(account_sid, auth_token)

def weekday():
    today = datetime.datetime.today().weekday()
    print("Today's Date:", datetime.date.today())
    # ----------------------------------------- must use this to format the the day of the week
    print("Day of week:", datetime.date.today().strftime("%A"))
    # days of the week monday=0 sunday=6
    if today == 6:
        print("its sunday")
        client.messages.create(
            to=myPhone,
            from_=TwilioNumber,
            body='TEXT MESSAGE GOES HERE ' + u'\U0001f680')

    else:
        print("no")


weekday()
