from alpaca.trading import OrderType, OrderSide
from model.order_model import OrderModel


class OrderController:
    def __init__(self, order_model: OrderModel, order_view):
        self.order_model = order_model
        self.order_view = order_view

    def place_order(self, order_type, stock_symbol, quantity):
        if order_type == 1:
            order_type = OrderSide.BUY
        if order_type == 2:
            order_type = OrderSide.SELL

        order = self.order_model.place_order(order_type, stock_symbol, quantity)

        if order is not None:
            self.order_view.display_order_confirmation(order)

    def get_all_orders(self):
        orders = self.order_model.get_all_orders()

        if orders is not None:
            self.order_view.display_all_orders(orders)

    def cancel_all_orders(self):
        cancel_order_response = self.order_model.cancel_all_orders()
        self.order_view.display_cancel_confirmation(cancel_order_response)

