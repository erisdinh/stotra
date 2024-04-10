"""
Stock trading and portfolio management execution are implemented in command pattern
"""

import json
from abc import ABC, abstractmethod
from alpaca.trading import TradingClient, MarketOrderRequest, OrderSide, TimeInForce, GetPortfolioHistoryRequest, \
    PortfolioHistory, Order


class Command(ABC):
    def __init__(self, receiver, alpaca_client: TradingClient):
        self.receiver = receiver
        self.alpaca_client = alpaca_client

    @abstractmethod
    def execute(self):
        pass


class PlaceOrderCommand(Command):
    def __init__(self, receiver, alpaca_client, order_type, stock_symbol, quantity):
        super().__init__(receiver, alpaca_client)
        self.order_type = order_type
        self.stock_symbol = stock_symbol
        self.quantity = quantity

    def execute(self):
        result = self.receiver.place_order(self.alpaca_client, self.order_type, self.stock_symbol, self.quantity)
        return result


class GetAllOrdersCommand(Command):
    def __init__(self, receiver, alpaca_client):
        super().__init__(receiver, alpaca_client)

    def execute(self):
        result = self.receiver.get_all_orders(self.alpaca_client)
        return result


class CancelAllOrdersCommand(Command):
    def __init__(self, receiver, alpaca_client):
        super().__init__(receiver, alpaca_client)

    def execute(self):
        result = self.receiver.cancel_all_orders(self.alpaca_client)
        return result


class GetTradeActivityCommand(Command):
    def __init__(self, receiver, alpaca_client):
        super().__init__(receiver, alpaca_client)

    def execute(self):
        result = self.receiver.get_trade_activities(self.alpaca_client)
        return result


class GetPortfolioHistoryCommand(Command):
    def __init__(self, receiver, alpaca_client):
        super().__init__(receiver, alpaca_client)

    def execute(self):
        portfolio_history = self.receiver.get_portfolio_history(self.alpaca_client)
        return portfolio_history


class Receiver:
    def place_order(self, alpaca_client, order_type, stock_symbol, quantity):
        order_side = None
        if order_type == 'sell':
            order_side = OrderSide.SELL
        elif order_type == 'buy':
            order_side = OrderSide.BUY

        market_order_data = MarketOrderRequest(
            symbol=stock_symbol,
            qty=quantity,
            side=order_side,
            time_in_force=TimeInForce.DAY
        )
        market_order_response = alpaca_client.submit_order(
            order_data=market_order_data
        )

        market_order = Order.parse_obj(market_order_response)

        return market_order

    def get_all_orders(self, alpaca_client):
        orders = alpaca_client.get_orders()
        return orders

    def cancel_all_orders(self, alpaca_client):
        cancel_order_response = alpaca_client.cancel_orders()
        return cancel_order_response

    def get_trade_activities(self, alpaca_client):
        response = alpaca_client.get(path="/account/activities?activity_types=FILL")

        trade_activities = []
        if len(response) > 0:
            trade_activities = json.loads(json.dumps(response))

        return trade_activities

    def get_portfolio_history(self, alpaca_client: TradingClient):
        response = alpaca_client.get(path="/account/portfolio/history")
        portfolio_history = PortfolioHistory.parse_obj(response)
        return portfolio_history


class Invoker:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def execute(self):
        result = self.command.execute()
        return result
