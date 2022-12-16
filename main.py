import requests
import datetime as dt
from twilio.rest import Client


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

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


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHAVANTAGE_API_KEY = 'yourAlphavantageAPIKey'
NEWSAPI_API_KEY = 'yourNewAPIKey'
# Twilio account info
account_sid = 'yourTwilioAccountSID'
auth_token = 'yourTwilioAuthToken'

alphavantage_endpoint = 'https://www.alphavantage.co/query'
alphavantage_params = {
    'function': 'TIME_SERIES_DAILY_ADJUSTED',
    'symbol': STOCK,
    'apikey': ALPHAVANTAGE_API_KEY,
    }
newsapi_endpoint = 'https://newsapi.org/v2/everything'
newsapi_params = {
    'apiKey': NEWSAPI_API_KEY,
    'q': COMPANY_NAME,
    'searchIn': 'title',
    'sortBy': 'publishedAt',
    'pageSize': 3,
    }


def calc_percent_change() -> float:
    """Returns percent change of closing stock price for the previous 2 market days."""
    prevClosing = float(stockPriceData[prevMarkDay_f]['4. close'])
    b4prevClosing = float(stockPriceData[b4prevMarkDay_f]['4. close'])
    percent_change = (prevClosing - b4prevClosing) / b4prevClosing * 100
    return round(percent_change, 1)

def compose_message() -> str:
    """Returns formatted message with top 3 headlines and briefings for the stock."""
    response = requests.get(url=newsapi_endpoint, params=newsapi_params)
    response.raise_for_status()
    news_data = response.json()['articles']
    if percentChange <=-5:
        triangle = '🔻'
    else:
        triangle = '🔺'

    message = f'{STOCK}: {triangle}{percentChange}%\n'
    for i in range(len(news_data)):
        title = news_data[i]['title']
        description = news_data[i]['description']
        message += f'Headlines: {title}\nBrief: {description}\n\n'
    return message

def send_sms_alert(message):
    """Send SMS notification via Twilio to your phone."""
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=message,
        from_='+yourTwilioPhone#',
        to='+yourPhone#'
        )


response = requests.get(url=alphavantage_endpoint, params=alphavantage_params)
response.raise_for_status()
daily_price_data = response.json()
stockPriceData = daily_price_data['Time Series (Daily)']

# Get previous 2 market days formatted as YYYY-MM-DD.
today = dt.datetime.now()
if today.weekday() == 0: # Monday
    prevMarkDay = today - dt.timedelta(days=3) # Friday
    b4prevMarkDay = today - dt.timedelta(days=4) # Thursday
elif today.weekday() == 1: # Tuesday
    prevMarkDay = today - dt.timedelta(days=1) # Monday
    b4prevMarkDay = today - dt.timedelta(days=4) # Friday
elif today.weekday() == 6: # Sunday
    prevMarkDay = today - dt.timedelta(days=2) # Friday
    b4prevMarkDay = today - dt.timedelta(days=3) # Thursday
else:
    prevMarkDay = today - dt.timedelta(days=1)
    b4prevMarkDay = today - dt.timedelta(days=2)

prevMarkDay_f = prevMarkDay.strftime('%Y-%m-%d')
b4prevMarkDay_f = b4prevMarkDay.strftime('%Y-%m-%d')

if prevMarkDay_f in stockPriceData and b4prevMarkDay_f in stockPriceData:
    percentChange = calc_percent_change()

    if percentChange <= -5 or percentChange >= 5:
        message = compose_message()
        send_sms_alert(message)
