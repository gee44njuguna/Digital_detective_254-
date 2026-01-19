import os
import threading
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.environ.get("8211711661:AAHctNqA37TY96PxSVMtkXSjqtz0lhRs6Rg")

app = Flask(__name__)

@app.route("/")
def home():
    return "Digital Detective Bot is running!"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🕵️ Digital Detective is LIVE and ready to help you!")

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

def main():
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()

if __name__ == "__main__":
    threading.Thread(target=run_flask).start()
    main()