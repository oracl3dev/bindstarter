#dell

from telethon import TelegramClient, events

API_ID = '...'
API_HASH = '8873974115:AAHlD2COTyxnOGtJYqeOWmTJrmKyaOGOEQA'

keywords = set()
client = TelegramClient('session', API_ID, API_HASH)

@client.on(events.NewMessage(outgoing=True, pattern=r'\.addkw (.+)'))
async def add_keyword(event):
    kw = event.pattern_match.group(1).strip()
    keywords.add(kw.lower())
    await event.delete()
    print(f"Добавлено: {kw}")

@client.on(events.NewMessage(outgoing=True, pattern=r'\.delkw (.+)'))
async def del_keyword(event):
    kw = event.pattern_match.group(1).strip().lower()
    keywords.discard(kw)
    await event.delete()
    print(f"Удалено: {kw}")

@client.on(events.NewMessage(outgoing=True, pattern=r'\.listkw'))
async def list_keywords(event):
    await event.edit('Keywords: ' + ', '.join(keywords) if keywords else 'Список пуст')

@client.on(events.NewMessage(outgoing=True))
async def auto_delete(event):
    if event.message.text and any(kw in event.message.text.lower() for kw in keywords):
        await event.delete()
        print(f"Удалено: {event.message.text}")

print("Запущен...")
client.start()
client.run_until_disconnected()