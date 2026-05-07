import os, logging, threading
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.environ.get("TOKEN")
print(f"DEBUG: TOKEN tồn tại không = {bool(TOKEN)}")
logging.basicConfig(level=logging.INFO)

app_flask = Flask(__name__)
@app_flask.route('/')
def home(): return "Bot dang chay"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot chạy rồi nè bro ✅")

def run_bot():
    try:
        app = ApplicationBuilder().token(TOKEN).build()
        app.add_handler(CommandHandler("start", start))
        print("Bot is alive!")
        app.run_polling()
    except Exception as e:
        print(f"LỖI BOT CHÍNH: {e}")

if __name__ == '__main__':
    threading.Thread(target=run_bot).start()
    app_flask.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))
