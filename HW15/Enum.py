import logging
from enum import Enum

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


class OrderStatus(Enum):
    PENDING = 'Заказ ожидает обработки'
    IN_PROGRESS = 'Заказ готовится'
    READY = 'Заказ готов'
    COMPLETED = 'Заказ выдан'
    CANCELLED = 'Заказ отменён'


class Order:
    def __init__(self, order_id, status=OrderStatus.PENDING):
        self.order_id = order_id
        self.status = status

    def update_status(self, new_status):
        if isinstance(new_status, OrderStatus):
            self.status = new_status
        else:
            logging.info("Неккоректный статус")

    def display_status(self):
        logging.info(self.status.value)


order = Order(1)
order.display_status()

order.update_status(OrderStatus.IN_PROGRESS)
order.display_status()

order.update_status(OrderStatus.READY)
order.display_status()

order.update_status('Заказ отменён')

order.update_status(OrderStatus.COMPLETED)
order.display_status()
