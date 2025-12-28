import os
from pyrogram import Client, filters

# بياناتك مدمجة وجاهزة
API_ID = 30603517
API_HASH = "48dd28ebe48a60483ed1e07e68925115"
BOT_TOKEN = "8310863523:AAEmOFUTwsvYqTD4ZQbPoFihs56CwAgWdvk"

# هذا المتغير سيتغير تلقائياً عند رفعه على السيرفر ليعطيك رابطاً شغالاً
URL = os.environ.get("URL", "https://your-app-name.onrender.com")

app = Client("stream_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.video | filters.document)
async def send_link(client, message):
    file_name = message.video.file_name if message.video else message.document.file_name
    # الرابط الجديد الذي سيقبله 1DM
    direct_link = f"{URL}/dl/{message.id}/{file_name}"
    
    await message.reply_text(f"✅ **الرابط المباشر جاهز للتحميل:**\n\n`{direct_link}`")

app.run()
