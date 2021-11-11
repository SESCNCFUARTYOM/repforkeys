import requests

API_link = "https://api.telegram.org/bot2113737812:AAGmvoKlcJVXNMSHG-q_a0g3-i00dVP5rJ4"
updates = requests.get(API_link + "/getUpdates?offset=-1").json()

print(updates)

message = updates["result"][0]["message"]
chat_id = message["from"]["id"]
text = message["text"]

send_message = requests.get(API_link + f"/sendMessage?chat_id={898219767}&text=Привет, я бот, ты написал{text}")
