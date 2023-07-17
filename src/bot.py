import os
import telebot


# Initializing the telegram bot with the provided TOKEN
bot = telebot.TeleBot(os.environ['anonntelegram_bot_TOKEN'], parse_mode='HTML')