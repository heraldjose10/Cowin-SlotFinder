from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv('.env')

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
sender = os.getenv('SENDER')

client = Client(account_sid, auth_token)


def message(body, reciever,sender=sender, Client=client):
    message = client.messages.create(
        body =body,
        from_ = '{}'.format(sender),
        to = '{}'.format(reciever)
    )
    print(message.sid)

# for i in text:
#     message(client, i, reciever, sender)
# body = 'Your appointment is coming up on {} at {}'.format('10','12')
