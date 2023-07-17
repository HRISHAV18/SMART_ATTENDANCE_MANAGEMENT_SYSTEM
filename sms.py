from twilio.rest import Client

SID = 'ACef3eacedeb75f80ac366707a7eff6b6c'
AUTH_TOKEN = '5d21447b955ba6d4e7497d36e27de8b9'

cl = Client(SID, AUTH_TOKEN)

cl.messages.create(body='Your attendance has been marked', from_='+15076903133', to='+918017483866')