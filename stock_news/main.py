import requests as rq
from twilio.rest import Client
from decouple import config
import os
# Stock Data

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = config("STOCK_API_KEY")
STOCK_PARAMS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}

# News Data

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = config("NEWS_API_KEY")
NEWS_PARAMS = {
    "q": "Tesla",
    "apiKey": NEWS_API_KEY
}

# SMS Data
SMS_SID = config("SMS_SID")
SMS_TOKEN = config("SMS_TOKEN")
SMS_FROM = config("SMS_FROM")
SMS_TO = config("SMS_TO")

# Getting Stock
stock_request = rq.get(url=STOCK_ENDPOINT, params=STOCK_PARAMS)
data = stock_request.json()["Time Series (Daily)"]
data_list = list(data.items())

yesterday_closing_price = float(data_list[0][1]["4. close"])
dbyesterday_closing_price = float(data_list[1][1]["4. close"])

positive_difference = abs(yesterday_closing_price - dbyesterday_closing_price)


if positive_difference > dbyesterday_closing_price * 0.03:
    # Getting News
    news_request = rq.get(url=NEWS_ENDPOINT, params=NEWS_PARAMS)
    news_dict = dict()
    for n in range(3):
        news_title = news_request.json()["articles"][n]["title"]
        news_description = news_request.json()["articles"][n]["description"]
        one_news_dict = {news_title: news_description}
        news_dict.update(one_news_dict)
    output = ""
    for title, description in news_dict.items():
        output += title
        output += ":\n"
        output += description
        output += f"\n\n"
    # Send SMS
    client = Client(SMS_SID, SMS_TOKEN)
    message = client.messages \
                    .create(
                        body=output,
                        from_=SMS_FROM,
                        to=SMS_TO
                    )

    print(message.sid)
