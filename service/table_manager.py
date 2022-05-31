import datetime

from database.manager import DBManager

from google_sheets.reader import GoogleSheetsReader

from service.course_manager import CourseUSD
from service.time_manager import TimeManager

from telegram_bot.manager import BotManager
from telegram_bot.message import BotMessage


class TableManager(CourseUSD, GoogleSheetsReader, BotManager):

    def __init__(self):
        self.bot_message = BotMessage()
        self.bot_manager = BotManager()
        self.db_manager = DBManager()
        self.time_manager = TimeManager()
        self._course_usd = None
        self._table = None

    def set_raw_table(self):
        self._table = self.get_google_sheets_table()

    def set_course_usd(self):
        self._course_usd = self.get_course_usd()

    def get_table(self):
        return self._table

    def add_rub_to_table(self):
        for row in self._table:
            try:
                row[0] = int(row[0])
                row[1] = int(row[1])
                row[2] = int(row[2])
                row[3] = datetime.datetime.strptime(row[3], '%d.%m.%Y').date()
                rub = row[2] * self._course_usd
                row.append(rub)
            except IndexError:
                continue

        return self._table

    def check_expired_orders(self):
        orders = self.db_manager.get_order_from_db_all()
        expired_orders = self.time_manager.get_expired_orders(orders)
        if expired_orders:
            message = self.bot_message.message(expired_orders)
            self.bot_manager.send_orders_message(message)
