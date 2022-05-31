import datetime


ACTUAL_DATA = datetime.date.today()


class TimeManager:

    @staticmethod
    def get_expired_orders(orders: list):
        """Check expired_orders."""
        expired_orders = []
        for order in orders:
            if order.delivery_time < ACTUAL_DATA:
                expired_orders.append(order)
        return expired_orders
