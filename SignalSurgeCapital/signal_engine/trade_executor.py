
from alpaca_trade_api.rest import REST
from config import ALPACA_API_KEY, ALPACA_SECRET_KEY
api = REST(ALPACA_API_KEY, ALPACA_SECRET_KEY, base_url="https://paper-api.alpaca.markets")
def execute_trade(symbol, side):
    qty = 1
    order = api.submit_order(symbol=symbol, qty=qty, side=side, type='market', time_in_force='gtc')
    return api.get_last_trade(symbol).price
