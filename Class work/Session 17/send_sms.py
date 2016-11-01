# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient

# Find these values at https://twilio.com/user/account
account_sid = "AC89d1043c2c7b8b70639b37c274d83dd7"
auth_token = "ee2bb231f043e049b815ccab912f5fde"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(to="+13522153127", from_="+17817057188",
                                     body="Hello Professor would you like to play a game?")
