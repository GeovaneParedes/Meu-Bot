import os
import telebot
from handlers import register_handlers
from config import API_TOKEN

if not API_TOKEN:
    raise ValueError("O token do bot não foi definido na variável de ambiente TELEGRAM_BOT_TOKEN")

bot = telebot.TeleBot(API_TOKEN)

register_handlers(bot)

print("Bot rodando...")

bot.infinity_polling()
