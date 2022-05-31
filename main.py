import time

from app import main

from database.manager import DBManager

from service.table_manager import TableManager


ONE_MINUTE = 30
ONE_DAY = 60


if __name__ == '__main__':
    db_manager = DBManager()
    db_manager.create_db()
    count_minutes = 0

    while True:
        main()
        time.sleep(ONE_MINUTE)
        count_minutes += 30

        if count_minutes == ONE_DAY:
            table_manager = TableManager()
            table_manager.check_expired_orders()
