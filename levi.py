#Credits :- @EminenceCurse and @ishikki_Akabane


from pyrogram import Client, filters, idle
import requests
import random
import asyncio
api_id =  29422639
api_hash = 'e21bccfd64a01c5762ce81c77379dc7f' 

token = '6368969091:AAF-gE8KSbodGuCYIzIvHWYWk0LXjW98pvw' #--Enter Bot Token Here.


START_MSG = """
**Hyy{},
This is a basic bot to react on your messages. 
Use /react while replying on someone's message.**
"""

@Bot.on_message(filters.command('start'))
async def start_cmd(client, message):
    await message.reply(START_MSG.format(message.from_user.mention))

emojis = ["👍", "👎", "❤️", "🔥", "🥰", "👏", "😁", "🤔", "🤯", "😱", "🤬", "😢", "🎉", "🤩", "🤮", "💩", "🙏", "👌", "🕊", "🤡", "🥱", "🥴", "😍", "🐳", "❤️‍🔥", "🌚", "🌭", "💯", "🤣", "⚡️", "🍌", "🏆", "💔", "🤨", "😐", "🍓", "🍾", "💋", "🖕", "😈", "😴", "😭", "🤓", "👻", "👨‍💻", "👀", "🎃", "🙈", "😇", "😨", "🤝", "✍️", "🤗", "🫡", "🎅", "🎄", "☃️", "💅", "🤪", "🗿", "🆒", "💘", "🙉", "🦄", "😘", "💊", "🙊", "😎", "👾", "🤷‍♂️", "🤷", "🤷‍♀️", "😡"]

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=token)

@app.on_message(filters.command("react"))
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
