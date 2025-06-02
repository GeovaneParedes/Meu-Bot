#!/usr/bin/env python3
"""
Bot Telegram para gerenciar um supergrupo de Telegram e fornecer cursos 
gratuitos de programação no modo privado, sem poluição de mensagens. 
Entregando conteúdo de forma organizada e interativa em teclas inline.
"""
__version__ = "0.1.0"

import os
import telebot
from handlers import register_handlers
from config import API_TOKEN

if not API_TOKEN:
    raise ValueError("O token do bot não foi definido na variável de ambiente TELEGRAM_BOT_TOKEN")

bot = telebot.TeleBot(API_TOKEN)

register_handlers(bot)

print("Bot rodando... 🚀 ")

bot.infinity_polling()

