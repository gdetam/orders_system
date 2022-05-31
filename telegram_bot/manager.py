"""Bot manager for send messages with expired orders."""

from telegram_bot.connector import CHAT_ID, bot


class BotManager:

    @staticmethod
    def send_orders_message(message):
        bot.send_message(CHAT_ID, message)
