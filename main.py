
from signal_engine import (
    conventional_signals,
    alternative_signals,
    signal_scoring,
    trade_executor,
    trade_logger,
    notifier
)
import schedule, time

def run_signal_engine():
    print("Running signal engine...")
    conventional = conventional_signals.get_signals()
    alternative = alternative_signals.get_sentiment_scores()
    signals = signal_scoring.stack_signals(conventional, alternative)

    for symbol, data in signals.items():
        if data["score"] >= 8:
            action = "buy" if data["sentiment"] == "bullish" else "sell"
            price = trade_executor.execute_trade(symbol, action)
            trade_logger.log_trade(symbol, action, price, data["score"])
            notifier.send_alert(symbol, action, price, data["score"])

schedule.every(15).minutes.do(run_signal_engine)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)
