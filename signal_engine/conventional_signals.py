
import yfinance as yf
def get_signals():
    symbols = ["TSLA", "AAPL", "NVDA", "AMD"]
    result = {}
    for symbol in symbols:
        data = yf.download(symbol, period="5d", interval="1h")
        rsi = compute_rsi(data["Close"])
        result[symbol] = {"rsi": rsi[-1]}
    return result
def compute_rsi(series, period=14):
    delta = series.diff()
    gain = delta.where(delta > 0, 0).rolling(window=period).mean()
    loss = -delta.where(delta < 0, 0).rolling(window=period).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))
