from telethon import TelegramClient
from telethon.tl.functions.contacts import ImportContactsRequest
from telethon.tl.types import InputPhoneContact

API_ID = '30955557'      # my.telegram.org
API_HASH = '952246e079751c01c142a17d481f8e22'

client = TelegramClient('session', API_ID, API_HASH)

async def lookup_phone(phone: str):
    await client.start()
    
    contact = InputPhoneContact(client_id=0, phone=phone, first_name='', last_name='')
    result = await client(ImportContactsRequest([contact]))
    
    if result.users:
        user = result.users[0]
        print(f"Имя: {user.first_name} {user.last_name or ''}")
        print(f"Юзернейм: @{user.username or 'нет'}")
        print(f"ID: {user.id}")
    else:
        print("Аккаунт не найден или номер скрыт в настройках приватности")
    
    await client.disconnect()

import asyncio
asyncio.run(lookup_phone('+XXXXXXXXXXX'))