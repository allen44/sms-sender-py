from twilio.rest import Client
from sys import argv

#Make sure to install the Twilio lobrary first with: pip install twilio
# You'll need to get your own account info from Twilio

account_sid = '________'
auth_token = '___________'
client = Client(account_sid, auth_token)

message = client.messages.create(
                                from_ = '+1nnnnnnnnnn',
                                body = 'Hello Worlds',
                                to = '+1nnnnnnnnnn'
                                )
                    
print(message.sid)

