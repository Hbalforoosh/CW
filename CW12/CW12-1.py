import logging


class Order:
    def __init__(self, order_id, customer_name, amount):
        self.order_id = order_id
        self.customer_name = customer_name
        self.amount = amount
        self.status = None

    def process_order(self):
        if self.amount > 0 and self.amount < 5000:
            self.status = "Processed"
        elif self.amount >= 5000:
            self.status = "Pending Approval"
        else:
            self.status = "Error"


class OrderLogger:
    def __init__(self, log_file="orders.log"):
        logging.basicConfig(
            filename=log_file,
            level=logging.DEBUG,
            format="%(asctime)s %(levelname)s [Order:%(order_id)s] %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        self.logger = logging.getLogger("OrderLogger")

    def log_order(self, order: Order):
        extra_info = {"order_id": order.order_id}

        if order.status == "Processed":
            self.logger.info(
                f"Order processed for {order.customer_name}", extra=extra_info)
        elif order.status == "Pending Approval":
            self.logger.warning(
                f"Order requires approval for {order.customer_name}", extra=extra_info)
        elif order.status == "Error":
            self.logger.error(
                f"Invalid order amount for {order.customer_name}", extra=extra_info)

        self.logger.debug(
            f"Order details: customer={order.customer_name}, amount={order.amount}, status={order.status}",
            extra=extra_info
        )


orders = [
    Order(1, "Arian", 2000),
    Order(2, "Faqihe", 3500),
    Order(3, "Mehdi", 0),
]
