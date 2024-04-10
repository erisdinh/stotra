from controller.order_controller import OrderController
from controller.portfolio_controller import PortfolioController
from model.db_client import DBObjectPool
from model.alpaca_client import AlpacaClientObjectPool
from model.order_model import OrderModel
from model.portfolio_model import PortfolioModel
from view.order_view import OrderView
from view.portfolio_view import PortfolioView
from view.user_prompt import UserPromptView

if __name__ == "__main__":
    # Open Azure DB client pool
    db_pool = DBObjectPool()

    # Open Alpaca Trading client pool
    alpaca_client_pool = AlpacaClientObjectPool()

    # Create instance of UserPromptView
    user_prompt_view = UserPromptView()
    input_value = user_prompt_view.display_greeting()

    while input_value != 3:
        if int(input_value) == 1:
            stock_trading_input_value = user_prompt_view.display_stock_trading_options()

            while stock_trading_input_value != 4:
                db_client = db_pool.acquire()
                alpaca_trading_client = alpaca_client_pool.acquire()

                # Create instance of OrderView, OrderModel and OrderController
                order_view = OrderView()
                order_model = OrderModel(db_client=db_client, alpaca_trading_client=alpaca_trading_client)
                order_controller = OrderController(order_model, order_view)

                if int(stock_trading_input_value) == 1:
                    stock_symbol, order_type, quantity = order_view.display_stock_order_request()
                    order_controller.place_order(order_type=order_type, stock_symbol=stock_symbol, quantity=quantity)
                elif int(stock_trading_input_value) == 2:
                    order_controller.cancel_all_orders()
                elif int(stock_trading_input_value) == 3:
                    order_controller.get_all_orders()

                stock_trading_input_value = user_prompt_view.display_stock_trading_options()

                alpaca_client_pool.release(alpaca_trading_client)
                db_pool.release(db_client)
        elif int(input_value) == 2:
            portfolio_management_input_value = user_prompt_view.display_portfolio_management_options()

            while portfolio_management_input_value != 3:
                db_client = db_pool.acquire()
                alpaca_trading_client = alpaca_client_pool.acquire()

                # Create instance of PortfolioView, PortfolioModel and PortfolioController
                portfolio_view = PortfolioView()
                portfolio_model = PortfolioModel(db_client=db_client, alpaca_trading_client=alpaca_trading_client)
                portfolio_controller = PortfolioController(portfolio_model, portfolio_view)

                if int(portfolio_management_input_value) == 1:
                    portfolio_controller.get_portfolio_history()
                    portfolio_management_input_value = user_prompt_view.display_portfolio_management_options()
                elif int(portfolio_management_input_value) == 2:
                    portfolio_controller.get_trade_activities()
                    portfolio_management_input_value = user_prompt_view.display_portfolio_management_options()

                alpaca_client_pool.release(alpaca_trading_client)
                db_pool.release(db_client)

        input_value = user_prompt_view.display_greeting()

    input("See ya! Press any key to exit.")
