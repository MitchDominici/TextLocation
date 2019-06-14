from twilio.rest import Client
from GetLocation import main

# Your Account SID from twilio.com/console
account_sid = "Your account Here"
# Your Auth Token from twilio.com/console
auth_token  = "Your Token Here"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="Your Phone Number Here", 
    from_="Your Twilio Number Here",
    body=main())

print(message.sid)
