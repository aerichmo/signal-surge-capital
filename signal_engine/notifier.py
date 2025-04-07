
import requests
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID
def send_alert(symbol, action, price, score):
    message = f"Signal Alert: {symbol} | Action: {action.upper()} | Price: ${price} | Score: {score}"
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    requests.post(url, data=data)
