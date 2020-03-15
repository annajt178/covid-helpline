from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACbb9da21743fd5f24aa66383a28f269f2'
auth_token = '152985f26d6022ceca088850e1a13b1c'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+18474439371',
                     to='+16362191253'
                 )

print(message.__dict__['_properties'])