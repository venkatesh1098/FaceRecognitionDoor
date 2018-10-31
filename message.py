from textmagic.rest import TextmagicRestClient
  
username = "your_textmagic_username"
token = "your_apiv2_key"
client = TextmagicRestClient(username, token)
  
message = client.messages.create(phones="7666402443", text="Hello TextMagic")