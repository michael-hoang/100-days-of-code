import requests
from bs4 import BeautifulSoup


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
    'div.a-section.a-spacing-none > span > span.a-offscreen')
print(span_tag)
