import requests
import json
from datetime import datetime, timedelta
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#STOCK URL Setup
STOCK_API_KEY = "FL3JX0B05047OFBG"
STOCK_API_URL_params = {
    "function":"TIME_SERIES_DAILY", 
    "symbol":STOCK,
    "apikey": STOCK_API_KEY
}
STOCK_API_URL = "https://www.alphavantage.co/query"
date = datetime.now().date()
starting_date = date - timedelta(days=2)
ending_date = date - timedelta(days=1)
formatted_start = starting_date.strftime("%Y-%m-%d")
formatted_end = ending_date.strftime("%Y-%m-%d")



##GET STOCK DATA##
def stock_data():
    r = requests.get(url=STOCK_API_URL, params=STOCK_API_URL_params)
    r.raise_for_status()
    data = r.json()['Time Series (Daily)']
    opening_price = float(list(dict([(label, price) for label, price in data[formatted_start].items() if label == '4. close']).values())[0])
    closing_price = float(list(dict([(label, price) for label, price in data[formatted_end].items() if label == '4. close']).values())[0])
    difference = round((abs(opening_price - closing_price)/ closing_price)*100, 2)
    return difference
    



## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
news_api_key = 'ff151b3396fc4e9d9156483f5892aa1b'
news_api_url = 'https://newsapi.org/v2/everything'
news_api_url_params = {
    "q": STOCK,
    "apiKey": news_api_key
}
def get_news():
    r = requests.get(url=news_api_url, params=news_api_url_params)
    r.raise_for_status()
    articles = r.json()['articles'][:3]
    return articles
    

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
account_sid = 'AC0ababd006aa33543aa421d506429375f'
auth_token = 'ffb59cadb5aa09dc658120421216f83e'
client = Client(account_sid, auth_token)

article_previews = [{data.get('title'): data.get('description')} for data in get_news()]


for article in article_previews:
    description = list(article.values())[0]
    title = list(article.keys())[0]
    message = client.messages.create(
         body=f'{STOCK}: {stock_data()} \n Headline: {title} \n Description: {description}',
         from_='+12053182852',
         to='+16476690292'
     )
    
    
    

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

