from model.portfolio_model import PortfolioModel
from view.portfolio_view import PortfolioView


class PortfolioController:
    def __init__(self, portfolio_model: PortfolioModel, portfolio_view: PortfolioView):
        self.portfolio_model = portfolio_model
        self.portfolio_view = portfolio_view

    def get_trade_activities(self):
        activities = self.portfolio_model.get_trade_activities()

        if activities is not None:
            self.portfolio_view.display_trade_activities(activities)

    def get_portfolio_history(self):
        portfolio_history = self.portfolio_model.get_portfolio_history()

        if portfolio_history is not None:
            self.portfolio_view.display_portfolio_history(portfolio_history)