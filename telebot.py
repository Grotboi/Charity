from telethon.sync import TelegramClient
import asyncio

# Telebot
api_id = 1
api_hash = 1
phone = 1
channel_username = 1


client = TelegramClient('session_name', api_id, api_hash)

async def get_photo_tg():
    await client.start(phone)
    print("Client Run")
    
    channel = await client.get_entity(channel_username)
    
    async for message in client.iter_messages(channel, limit=1):
     if message.photo:
        photo_url = message.photo.get_input_file()
        return str(photo_url)
    
    return None