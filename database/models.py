"""Orders model."""

from database.connector import Base

from sqlalchemy import Column, Date, Integer


class Orders(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    order = Column(Integer, nullable=False)
    cost_usd = Column(Integer, nullable=False)
    delivery_time = Column(Date)
    cost_rub = Column(Integer, nullable=False)

    def __repr__(self):
        return "<orders(id='%s', order='%s', cost_usd='%s', delivery_time='%s', cost_rub='%s')>" \
               % (self.id, self.order, self.cost_usd, self.delivery_time, self.cost_rub,)
