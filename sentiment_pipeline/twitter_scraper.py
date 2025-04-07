
import tweepy
from collections import defaultdict
from textblob import TextBlob
from config import TWITTER_BEARER_TOKEN
TICKERS = ["TSLA", "AAPL", "NVDA", "AMD"]
def get_twitter_sentiment():
    auth = tweepy.OAuth2BearerHandler(TWITTER_BEARER_TOKEN)
    api = tweepy.API(auth)
    scores = defaultdict(lambda: {"score": 0})
    for ticker in TICKERS:
        try:
            tweets = api.search_tweets(q=f"${ticker}", lang="en", count=20)
            for tweet in tweets:
                sentiment = TextBlob(tweet.text).sentiment.polarity
                scores[ticker]["score"] += sentiment
        except:
            continue
    return scores
