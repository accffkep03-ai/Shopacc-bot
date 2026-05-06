import os
import threading
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
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    print("Bot is alive!")  # Dòng này để check bot có chạy không
    application.run_polling()

if __name__ == '__main__':
    threading.Thread(target=run_bot).start()
    app.run(host='0.0.0.0', port=10000)
