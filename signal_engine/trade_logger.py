
import csv
from datetime import datetime
def log_trade(symbol, action, price, score):
    with open("data/logs/trade_log.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.utcnow().isoformat(), symbol, action, price, score])
