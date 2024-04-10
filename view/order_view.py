"""
Order View for displaying stock trading output
"""
class OrderView:
    def display_stock_trading_options(self):
        print("\n----------------------------------------------------------------------------------------")
        print("Please choose an option:")
        print("1. Place an order")
        print("2. Cancel all orders")
        print("3. View all orders")
        print("4. Back")
        input_value = int(input("Your selection: "))
        return input_value

    def display_stock_order_request(self):
        stock_symbol = input("Enter a stock symbol (AAPL, MSFT, etc.): ")
        order_type = int(input("Order type:\n1. Buy\n2. Sell\nEnter order type: "))
        quantity = int(input("Enter quantity: "))
        return stock_symbol.upper(), order_type, quantity

    def display_order_confirmation(self, order):
        print(f"\n----------------------------------------------------------------------------------------\n"
              f"SUCCESSFUL: Market Order has been placed: \n"
              f"Order ID: {order.client_order_id}\n"
              f"Stock Symbol: {order.symbol}\n"
              f"Class: {order.asset_class}\n"
              f"Quantity: {order.qty}\n"
              f"Filled Quantity: {order.filled_qty}\n"
              f"Order Type: {order.order_type}\n"
              f"Order Side: {order.side}\n"
              f"Status: {order.status}\n"
              f"Created at: {order.created_at}\n"
              f"Submitted at: {order.submitted_at}\n"
              f"Filled at: {order.filled_at}")

    def display_error(self, msg):
        print(f"\n----------------------------------------------------------------------------------------\n"
              f"FAILED: Market Order was not placed.")

    def display_cancel_confirmation(self, cancel_order_response):
        if cancel_order_response is not None and len(cancel_order_response) > 0:
            for order in cancel_order_response:
                print(f"\n----------------------------------------------------------------------------------------\n"
                      f"Market Order: \n"
                      f"Order ID: {order.id}\n"
                      f"Status: {order.status}")
        else:
            print(f"\n----------------------------------------------------------------------------------------\n"
                  f"No orders were canceled.")


    def display_all_orders(self, orders):
        if len(orders) == 0:
            print(f"\n----------------------------------------------------------------------------------------\n"
                  f"No orders.")
        else:
            for order in orders:
                print(f"\n----------------------------------------------------------------------------------------\n"
                      f"Market Order: \n"
                      f"Order ID: {order.client_order_id}\n"
                      f"Stock Symbol: {order.symbol}\n"
                      f"Class: {order.asset_class}\n"
                      f"Quantity: {order.qty}\n"
                      f"Filled Quantity: {order.filled_qty}\n"
                      f"Order Type: {order.order_type}\n"
                      f"Order Side: {order.side}\n"
                      f"Status: {order.status}\n"
                      f"Created at: {order.created_at}\n"
                      f"Submitted at: {order.submitted_at}\n"
                      f"Filled at: {order.filled_at}")
