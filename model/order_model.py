"""
Order Model for data and business logics related to stock trading (orders)
"""
from alpaca.trading import TradingClient
from model.alpaca_commands import Invoker, Receiver, PlaceOrderCommand, GetAllOrdersCommand, CancelAllOrdersCommand
from model.db_client import ReusableDBClient


class OrderModel:
    def __init__(self, alpaca_trading_client: TradingClient, db_client: ReusableDBClient):
        self.__alpaca_trading_client = alpaca_trading_client
        self.__db_client = db_client
        self.__stock_trading_invoker = Invoker()
        self.__stock_trading_receiver = Receiver()

    def place_order(self, order_type, stock_symbol, quantity):
        place_order_command = PlaceOrderCommand(receiver=self.__stock_trading_receiver,
                                                alpaca_client=self.__alpaca_trading_client.trading_client,
                                                order_type=order_type,
                                                stock_symbol=stock_symbol,
                                                quantity=quantity)
        self.__stock_trading_invoker.set_command(place_order_command)
        order = self.__stock_trading_invoker.execute()
        return order

    def get_all_orders(self):
        get_all_orders_command = GetAllOrdersCommand(receiver=self.__stock_trading_receiver,
                                                     alpaca_client=self.__alpaca_trading_client.trading_client)
        self.__stock_trading_invoker.set_command(get_all_orders_command)
        orders = self.__stock_trading_invoker.execute()
        return orders

    def cancel_all_orders(self):
        cancel_all_orders_command = CancelAllOrdersCommand(receiver=self.__stock_trading_receiver,
                                                     alpaca_client=self.__alpaca_trading_client.trading_client)
        self.__stock_trading_invoker.set_command(cancel_all_orders_command)
        cancel_order_response = self.__stock_trading_invoker.execute()
        return cancel_order_response
