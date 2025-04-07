
import requests
from collections import defaultdict
TICKERS = ["TSLA", "AAPL", "NVDA", "AMD"]
KEYWORDS = ["buying the dip", "short squeeze"]
def get_reddit_sentiment():
    scores = defaultdict(lambda: {"score": 0})
    url = "https://api.pushshift.io/reddit/search/comment/"
    for ticker in TICKERS:
        params = {"q": ticker, "subreddit": "stocks", "after": "1h", "size": 100}
        data = requests.get(url, params=params).json().get("data", [])
        for comment in data:
            text = comment.get("body", "").lower()
            multiplier = sum(1 for kw in KEYWORDS if kw in text)
            scores[ticker]["score"] += 1 + multiplier
    return scores
