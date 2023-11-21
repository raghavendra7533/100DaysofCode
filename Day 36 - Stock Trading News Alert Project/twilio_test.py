from twilio.rest import Client
import newsapi

account_sid = 'AC97a375c0d7aca2cd7ba8eb08a5d134d9'
auth_token = '08e298590c0157bc1fa4d8d1aa7d682b'
client = Client(account_sid, auth_token)
NEWSAPI_APIKEY = "f2ab418bae9745c1bb5763f50c75f8f1"
newsapi = newsapi.NewsApiClient(api_key='f2ab418bae9745c1bb5763f50c75f8f1')

message = client.messages.create(from_='+19252739903', body='Hello', to='+919731154033')
all_articles = newsapi.get_top_headlines(q='bitcoin',
                                         sources='bbc-news,the-verge',
                                         language='en',
                                         country='us'
                                         )

print(all_articles)
