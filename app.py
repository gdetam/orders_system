from service.table_manager import TableManager


def main():
    table_manager = TableManager()
    table_manager.set_raw_table()
    table_manager.set_course_usd()
    table_manager.add_rub_to_table()
    table = table_manager.get_table()
    table_manager.db_manager.add_table_to_db(table)
