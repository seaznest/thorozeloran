from telethon import TelegramClient, events
import re
import aiohttp
import asyncio

api_id = 11953248
api_hash = '0bbd91316d9cdac32fb60ec62c82a090'
source_channel = 'https://t.me/bonuspopsozeloranresmi'
target_channel = 'https://t.me/bonusthorozeloran'

client = TelegramClient("userbot_session", api_id, api_hash)

@client.on(events.NewMessage(chats=source_channel))
async def handler(event):
    message_text = event.message.message
    link = None

    oran_var = re.search(r"\d+\s+ORAN\s+(MAX\s+)?\d+\s*TL", message_text.upper())
    if not oran_var:
        return

    for entity in event.message.entities or []:
        if isinstance(entity, type(event.message.entities[0])) and entity.url:
            if "bet" in entity.url.lower():
                link = entity.url
                break

    if not link:
        return

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(link, allow_redirects=True) as resp:
                final_url = str(resp.url)
    except:
        final_url = link

    caption = f"{message_text}\n\n🔗 [Siteye Git]({final_url})"

    await client.send_message(target_channel, caption, link_preview=False)

print("Bot hazır. Telegram'a bağlanılıyor...")
client.start()
client.run_until_disconnected()
