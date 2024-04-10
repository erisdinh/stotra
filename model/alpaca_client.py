"""
Connects to Alpaca Trading API using TradingClient
"""
from alpaca.trading.client import TradingClient


# This will be our re-usable Alpaca Client resource that the object pool will manage
# It will be a connection to Alpaca Trading API
class ReusableAlpacaClient:
    # create the connection
    def __init__(self):
        try:
            self.trading_client = TradingClient('PKC79UD89RIXC0P4AUQ6', '7baNy30xSWFvJdZ4fALsYnlqM71UILsHb92kxZWe', paper=True)
            print('Connected to Alpaca Trading')
        except Exception as e:
            print('Could not connect to Alpaca Trading')


# Manages the pool of objects, offers acquire and release operations to
# give the objects to client code and accept them back
class AlpacaClientObjectPool:
    # initialize the pool... in our case, just one re-usable object
    def __init__(self):
        self.__reusables = [ReusableAlpacaClient()]

    # give the resource to a client
    def acquire(self):
        return self.__reusables.pop()

    # accept the resource back from a client
    def release(self, reusable):
        self.__reusables.append(reusable)
