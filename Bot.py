import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.environ.get("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("ShopAccSieuRe xin chào!\nGõ /menu để xem lệnh.")

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("/sodu - Kiểm tra số dư\n/nap - Nạp tiền ATM\n/hotro - Liên hệ admin")

async def sodu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id
    await update.message.reply_text(f"ID: {uid}\nSố dư: 0đ")

async def nap(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id
    await update.message.reply_text(f"NẠP TIỀN\nSTK: 1903xxxxxxx MB Bank\nND: NAP {uid}")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("menu", menu))
app.add_handler(CommandHandler("sodu", sodu))
app.add_handler(CommandHandler("nap", nap))
app.run_polling()
