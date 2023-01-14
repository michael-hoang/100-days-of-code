import requests
from bs4 import BeautifulSoup
import smtplib
import os
from dotenv import load_dotenv


load_dotenv()

MY_EMAIL = os.getenv('MY_EMAIL')
APP_PASSWORD = os.getenv('APP_PASSWORD')
TARGET_PRICE = 200


product_url = 'https://www.amazon.com/Orient-Kamasu-Japanese-Automatic-Stainless-Steel/dp/B07QJN1GFX'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76',
    'accept-language': 'en-US,en;q=0.9',
}

response = requests.get(product_url, headers=headers)
content = response.text

soup = BeautifulSoup(content, 'html.parser')

# Get a hold of the span tag that contains the price
span_tag = soup.select(
    'div.a-section.a-spacing-none > span > span.a-offscreen')[0]

price_str = span_tag.string.split('$')[1]
price_float = float(price_str)

# Send email if market price is equal to or below the target price
if price_float <= TARGET_PRICE:
    item_name = soup.select(
        'div#titleSection > h1#title > span#productTitle')[0].string
    page_title = soup.select('title')[0].string.split(
        'Amazon.com: ')[1].split(' :')[0]
    message = f'Subject: Amazon Price Alert - {item_name}\n\n{page_title} is now ${price_float}\n{product_url}'

    with smtplib.SMTP(host='smtp.gmail.com') as connection:
        connection.ehlo()
        connection.starttls()
        connection.ehlo()
        connection.login(user=MY_EMAIL, password=APP_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=message)
