import os

import emoji
from loguru import logger
from telebot import custom_filters

from src.bot import bot
from src.constants import keyboards, keys
from src.utils.io import write_json
from utils.filters import IsAdmin


class Bot:
    """
    Creating Template for Telegram Bot.
    """
    def __init__(self, telebot):
        self.bot = telebot

        # add custom filters
        self.bot.add_custom_filter(IsAdmin())
        self.bot.add_custom_filter(custom_filters.TextMatchFilter())
        self.bot.add_custom_filter(custom_filters.TextStartsFilter())

        # register handlers
        self.handlers()

        # run bot
        logger.info('Bot is loading...')
        self.bot.infinity_polling()

    def handlers(self):

        @self.bot.message_handler(func=lambda message: True)
        def echo(message):
            self.send_message(
                message.chat.id, message.text,
                reply_markup=keyboards.main
        )


        @self.bot.message_handler(text=[keys.exit])
        def exit(message):
            pass


        @self.bot.message_handler(text=[keys.settings])
        def settings(message):
            pass


        @self.bot.message_handler(is_admin=True)
        def admin_of_group(message):
            self.send_message(message.chat.id, '<strong>You are the admin of this group!</strong>')


    def send_message(self, chat_id, text, reply_markup=None, emojize=True):
        """
        Send message to telegram bot.
        """
        if emojize:
            text = emoji.emojize(text, use_aliases=True)
        self.bot.send_message(chat_id, text, reply_markup=reply_markup)


if __name__ == '__main__':
    logger.info('Bot has started')
    anonntelegram_bot = Bot(telebot=bot)
    #anonntelegram_bot.run()