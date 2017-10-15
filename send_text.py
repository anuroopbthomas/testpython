from twilio import rest

# Your Account SID from twilio.com/console
#Twilio login
#password: rulesarentforeveryone
account_sid = "AC9a8175b3a861b91487885b3bf176e606"
# Your Auth Token from twilio.com/console
auth_token  = "c30481714a42ef68e13a750710e69400"

client = rest.Client(account_sid, auth_token)

message = client.messages.create(
    to="+13096215828",
    from_="+13092858106",
    body="Woah")

print(message.sid)
