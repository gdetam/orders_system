"""Database manager for create db, drop db and upload data."""

from database.connector import Base, Session, engine, get_db
from database.models import Orders

from sqlalchemy_utils import create_database, database_exists


class DBManager:

    def __init__(self):
        self.db: Session = get_db()

    @staticmethod
    def create_db():
        if not database_exists(engine.url):
            create_database(engine.url)
        Base.metadata.create_all(engine)

    @staticmethod
    def drop_db():
        Base.metadata.drop_all(engine)

    def add_table_to_db(self, table):
        """Add data in database."""
        for raw in table:
            try:
                obj = Orders(id=raw[0],
                             order=raw[1],
                             cost_usd=raw[2],
                             delivery_time=raw[3],
                             cost_rub=raw[4])
            except IndexError:
                continue
            self.db.merge(obj)
            self.db.commit()

    def get_order_from_db_by_id(self, id_: int) -> Orders:
        return self.db.query(Orders).filter(Orders.id == id_)

    def get_order_from_db_all(self):
        return self.db.query(Orders).all()
