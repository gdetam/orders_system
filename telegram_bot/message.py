"""Create message body for bot sending."""


class BotMessage:

    @staticmethod
    def message(orders):
        """Create message with expired orders for send."""
        message = ''
        for order in orders:
            message += f'Заказ №{order.order} срок поставки истек {order.delivery_time}\n'
        return message
