import telebot
import os

TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "👋 Welcome to Cyber Awareness!\nI am Digital Detective 254.\nI teach cybersecurity, hacking basics, OSINT and programming.")

@bot.message_handler(func=lambda m: True)
def reply_all(message):
    bot.reply_to(message, "🕵️ Digital Detective 254:\nAsk me anything about cybersecurity, hacking, investigations or programming.")

print("Bot running...")
bot.infinity_polling()