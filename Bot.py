import requests
import time

TOKEN = "7248461148:AAFcCC3y3ndgqWI2k9PkHbGYeevJPil66cw"
CHANNEL_ID = "https://t.me/dollarlin"
URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

def get_dollar_price():
    response = requests.get("https://api.tgju.org/v1/quote/sana/json")
    data = response.json()
    price = data["sana"]["usd"]["p"]
    return price

while True:
    try:
        price = get_dollar_price()
        message = f"قیمت دلار الان: {price} تومان"
        requests.post(URL, data={"chat_id": CHANNEL_ID, "text": message})
    except Exception as e:
        print("خطا:", e)
    time.sleep(1800)
