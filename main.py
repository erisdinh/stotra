from controller.order_controller import OrderController
from controller.portfolio_controller import PortfolioController
from model.db_client import DBObjectPool
from model.alpaca_client import AlpacaClientObjectPool
from model.order_model import OrderModel
from model.portfolio_model import PortfolioModel
from view.order_view import OrderView
from view.portfolio_view import PortfolioView


def display_greeting():
    print("\n----------------------------------------------------------------------------------------")
    print("Welcome to StoTra - Your personal stock trading and portfolio management application")
    print("Please choose an option:")
    print("1. Stock Trading")
    print("2. Portfolio Management")
    print("3. Exit")
    input_value = int(input("Your selection: "))
    return input_value


if __name__ == "__main__":
    # Open Azure DB client pool
    db_pool = DBObjectPool()

    # Open Alpaca Trading client pool
    alpaca_client_pool = AlpacaClientObjectPool()

    # Create instance of UserPromptView
    input_value = display_greeting()

    while input_value != 3:
        if int(input_value) == 1:
            # Create instance of OrderView and get user response
            order_view = OrderView()
            stock_trading_input_value = order_view.display_stock_trading_options()

            while stock_trading_input_value != 4:
                db_client = db_pool.acquire()
                alpaca_trading_client = alpaca_client_pool.acquire()

                # Create instance of OrderModel and OrderController
                order_model = OrderModel(db_client=db_client, alpaca_trading_client=alpaca_trading_client)
                order_controller = OrderController(order_model, order_view)

                if int(stock_trading_input_value) == 1:
                    stock_symbol, order_type, quantity = order_view.display_stock_order_request()
                    order_controller.place_order(order_type=order_type, stock_symbol=stock_symbol, quantity=quantity)
                elif int(stock_trading_input_value) == 2:
                    order_controller.cancel_all_orders()
                elif int(stock_trading_input_value) == 3:
                    order_controller.get_all_orders()

                alpaca_client_pool.release(alpaca_trading_client)
                db_pool.release(db_client)
                stock_trading_input_value = order_view.display_stock_trading_options()
        elif int(input_value) == 2:
            # Create instance of PortfolioView and get user response
            portfolio_view = PortfolioView()
            portfolio_management_input_value = portfolio_view.display_portfolio_management_options()

            while portfolio_management_input_value != 3:
                db_client = db_pool.acquire()
                alpaca_trading_client = alpaca_client_pool.acquire()

                # Create instance of PortfolioModel and PortfolioController
                portfolio_model = PortfolioModel(db_client=db_client, alpaca_trading_client=alpaca_trading_client)
                portfolio_controller = PortfolioController(portfolio_model, portfolio_view)

                if int(portfolio_management_input_value) == 1:
                    portfolio_controller.get_portfolio_history()
                elif int(portfolio_management_input_value) == 2:
                    portfolio_controller.get_trade_activities()

                alpaca_client_pool.release(alpaca_trading_client)
                db_pool.release(db_client)
                portfolio_management_input_value = portfolio_view.display_portfolio_management_options()

        input_value = display_greeting()

    input("See ya! Press any key to exit.")
