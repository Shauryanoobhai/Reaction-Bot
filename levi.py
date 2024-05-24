from pyrogram import Client, filters, idle
import requests
import random

api_id =  
api_hash = '' 

token = '' #--Enter Bot Token Here.

emojis = ["👍"]

app = Client("Lawda", api_id=api_id, api_hash=api_hash, bot_token=token)

@Lawda.on_message(filters.command("react"))
async def react_to_message(client, message):
    reply = message.reply_to_message
    chat_id = reply.chat.id
    message_id = reply.id
    
   
    random_emoji = random.choice(emojis)
    
    url = f'https://api.telegram.org/bot{token}/setMessageReaction'

  
    params = {
        'chat_id': chat_id,
        'message_id': message_id,
        'reaction': [{
            "type": "emoji",
            "emoji": random_emoji
        }]
    }

    response = requests.post(url, json=params)

    if response.status_code == 200:
        print("Reaction set successfully!")
        print("Response content:", response.content)
    else:
        print(f"Failed to set reaction. Status code: {response.status_code}")
        print("Response content:", response.content)

print("starting...")
app.start()

idle()
