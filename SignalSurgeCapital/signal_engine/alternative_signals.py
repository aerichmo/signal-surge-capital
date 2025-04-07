
from sentiment_pipeline.reddit_scraper import get_reddit_sentiment
from sentiment_pipeline.twitter_scraper import get_twitter_sentiment
def get_sentiment_scores():
    reddit_scores = get_reddit_sentiment()
    twitter_scores = get_twitter_sentiment()
    combined = {}
    for symbol in reddit_scores:
        r_score = reddit_scores[symbol].get("score", 0)
        t_score = twitter_scores.get(symbol, {}).get("score", 0)
        sentiment = "bullish" if (r_score + t_score) > 0 else "bearish"
        combined[symbol] = {
            "sentiment_score": (r_score + t_score) / 2,
            "sentiment": sentiment
        }
    return combined
