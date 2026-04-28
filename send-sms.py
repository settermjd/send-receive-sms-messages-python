# /usr/bin/env python
import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

# Find these values at https://twilio.com/user/account
# To set up environmental variables, see http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
recipient = os.environ['RECIPIENT']
sender = os.environ['TWILIO_PHONE_NUMBER']

client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to=recipient,
    from_=sender,
    body="This is the ship that made the Kessel Run in fourteen parsecs?"
)
