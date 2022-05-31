"""Telegram bot connector."""

import os

from dotenv import load_dotenv

import telebot


load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
bot = telebot.TeleBot(TOKEN)
