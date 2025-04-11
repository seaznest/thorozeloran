from telethon import TelegramClient, events

api_id = '11953248'
api_hash = '0bbd91316d9cdac32fb60ec62c82a090'

client = TelegramClient('userbot', api_id, api_hash)

@client.on(events.NewMessage)
async def handler(event):
    message = event.message.text
    print(f"Yeni mesaj: {message}")

    if "X ORAN X TL" in message:
        await client.send_message('KendiGrupAdı', 'Oranlar güncellenmiştir!')
        print("Mesaj kendi gruba gönderildi.")

client.start()
client.run_until_disconnected()
