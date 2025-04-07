
def stack_signals(conventional, alternative):
    signals = {}
    for symbol in conventional:
        rsi = conventional[symbol]["rsi"]
        sentiment_score = alternative[symbol]["sentiment_score"]
        sentiment = alternative[symbol]["sentiment"]
        rsi_score = 5 if rsi < 30 else (3 if rsi > 70 else 0)
        sentiment_points = round(abs(sentiment_score) * 5)
        total_score = rsi_score + sentiment_points
        signals[symbol] = {"score": total_score, "sentiment": sentiment}
    return signals
