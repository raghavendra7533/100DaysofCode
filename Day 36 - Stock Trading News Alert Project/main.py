import requests
from twilio.rest import Client


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = "UG3VS7CI3E20U16D"
NEWSAPI_APIKEY = "f2ab418bae9745c1bb5763f50c75f8f1"

account_sid = 'AC97a375c0d7aca2cd7ba8eb08a5d134d9'
auth_token = '08e298590c0157bc1fa4d8d1aa7d682b'
client = Client(account_sid, auth_token)

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
raw_data = response.json()
print(raw_data)
data_list = [value for (key, value) in raw_data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))


diff_percentage = (difference / float(yesterday_closing_price)) * 100
print(f"{diff_percentage}%")

if diff_percentage < 5:
    print("get news")
    news_params = {
        "apikey": NEWSAPI_APIKEY,
        "qInTitle": COMPANY_NAME,

    }
    news = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news.json()['articles']
    first_three_articles = articles[:3]

news_diff = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
if news_diff > 0:
    for item in range(len(first_three_articles)):
        content = f"{STOCK_NAME}: 🔺{abs(news_diff)}\nHeadline: {first_three_articles[item]['title']}\nBrief: {first_three_articles[item]['description']}"
        message = client.messages.create(from_='+19252739903', body=content, to='+919731154033')

elif news_diff < 0:
    for item in range(len(first_three_articles)):
        content = f"{STOCK_NAME}: 🔻{abs(news_diff)}\nHeadline: {first_three_articles[item]['title']}\nBrief: {first_three_articles[item]['description']}"
        message = client.messages.create(from_='+19252739903', body=content, to='+919731154033')


