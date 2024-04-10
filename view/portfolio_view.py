class PortfolioView:
    def display_portfolio_history(self, portfolio_history):
        print(f"\n----------------------------------------------------------------------------------------\n"
              f"Portfolio: \n"
              f"Base Value: {portfolio_history.base_value}\n"
              f"Gain/Loss: {portfolio_history.profit_loss[-1]}")

    def display_trade_activities(self, activities):
        for activity in activities:
            print(f"\n----------------------------------------------------------------------------------------\n"
                  f"Activity: \n"
                  f"Type: {activity["type"]}\n"
                  f"Transaction Time: {activity["transaction_time"]}\n"
                  f"Price: {activity["price"]}\n"
                  f"Quantity: {activity["qty"]}\n"
                  f"Side: {activity["side"]}\n"
                  f"Symbol: {activity["symbol"]}\n"
                  f"Leaves Quantity: {activity["leaves_qty"]}\n"
                  f"Order Id: {activity["order_id"]}\n"
                  f"Cumulative Quantity: {activity["cum_qty"]}\n"
                  f"Order Status: {activity["order_status"]}")

