import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.environ.get("TOKEN")
print(f"DEBUG: TOKEN tồn tại không = {bool(TOKEN)}")

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot chạy rồi nè bro ✅")

if __name__ == '__main__':
    try:
        app = ApplicationBuilder().token(TOKEN).build()
        app.add_handler(CommandHandler("start", start))
        print("Bot is alive!")
        app.run_polling()
    except Exception as e:
        print(f"LỖI BOT CHÍNH: {e}")
