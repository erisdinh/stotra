class UserPromptView:
    def display_greeting(self):
        print("----------------------------------------------------------------------------------------")
        print("Welcome to StoTra - Your personal stock trading and portfolio management application")
        print("Please choose an option:")
        print("1. Stock Trading")
        print("2. Portfolio Management")
        print("3. Exit")
        input_value = int(input("Your selection: "))
        return input_value

    def display_stock_trading_options(self):
        print("----------------------------------------------------------------------------------------")
        print("Please choose an option:")
        print("1. Place an order")
        print("2. Cancel all orders")
        print("3. View all orders")
        print("4. Back")
        input_value = int(input("Your selection: "))
        return input_value

    def display_portfolio_management_options(self):
        print("----------------------------------------------------------------------------------------")
        print("Please choose an option:")
        print("1. View portfolio gain/loss")
        print("2. Vew trade activities")
        print("3. Back")
        input_value = int(input("Your selection: "))
        return input_value