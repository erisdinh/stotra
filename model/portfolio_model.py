"""
Portfolio Model for data and business logics related to portfolio management (portfolio gain/loss and trade activities)
"""
from alpaca.trading import TradingClient
from model.alpaca_commands import Invoker, Receiver, GetTradeActivityCommand, GetPortfolioHistoryCommand
from model.db_client import ReusableDBClient


class PortfolioModel:
    def __init__(self, alpaca_trading_client: TradingClient, db_client: ReusableDBClient):
        self.__alpaca_trading_client = alpaca_trading_client
        self.__db_client = db_client
        self.__portfolio_management_invoker = Invoker()
        self.__portfolio_management_receiver = Receiver()

    def get_trade_activities(self):
        get_activity_command = GetTradeActivityCommand(receiver=self.__portfolio_management_receiver,
                                                 alpaca_client=self.__alpaca_trading_client.trading_client)
        self.__portfolio_management_invoker.set_command(get_activity_command)
        activities = self.__portfolio_management_invoker.execute()
        return activities

    def get_portfolio_history(self):
        get_activity_command = GetPortfolioHistoryCommand(receiver=self.__portfolio_management_receiver,
                                                  alpaca_client=self.__alpaca_trading_client.trading_client)
        self.__portfolio_management_invoker.set_command(get_activity_command)
        portfolio_history = self.__portfolio_management_invoker.execute()

        if portfolio_history is not None:
            sql_query = "INSERT INTO [dbo].[portfolio_history] (base_value, profit_loss) VALUES (?,?)"
            self.__db_client.cursor.execute(sql_query,portfolio_history.base_value, portfolio_history.profit_loss[-1])
            self.__db_client.cursor.commit()

        return portfolio_history
