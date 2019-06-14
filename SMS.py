from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACc935b5d5ee25fda4b683b04027684753"
# Your Auth Token from twilio.com/console
auth_token  = "7d7652064a705e067b2d065461cf8d9e"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+15039547309", 
    from_="+15412303658",
    body="")

print(message.sid)