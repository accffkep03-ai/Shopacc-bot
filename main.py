import os
import threading
import asyncio
from flask import Flask
from telegram.ext import ApplicationBuilder, CommandHandler

app = Flask(__name__)
TOKEN = os.environ.get("TOKEN")

@app.route('/')
def home():
    return "Bot is alive!"

async def start(update, context):
    await update.message.reply_text("Bot chạy rồi nè bro")

def run_bot():
    asyncio.set_event_loop(asyncio.new_event_loop())
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    print("Bot is alive!")  # Dòng này sẽ hiện trong Logs
    application.run_polling()

if __name__ == '__main__':
    threading.Thread(target=run_bot, daemon=True).start()
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
