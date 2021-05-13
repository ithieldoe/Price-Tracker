import os
import requests
from bs4 import BeautifulSoup
import smtplib
# wwwww
buying_price = 3000

# Scraping the page for price and title
params = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7'
}

response = requests.get(url='https://www.labirint.ru/books/752714/', headers=params)
soup = BeautifulSoup(response.text, 'html.parser')
title = soup.find(name='div', class_='prodtitle').getText().split('\n')[3]
price = int(soup.find(name='span', class_='buying-price-val-number').getText())

# Sending an email when price becomes less then buying price
if price <= buying_price:
    connection = smtplib.SMTP(host='smtp.gmail.com')
    connection.starttls()
    connection.login(user=os.environ.get('USER'), password=os.environ.get('PASSWORD'))
    connection.sendmail(
        from_addr=os.environ.get('USER'),
        to_addrs=os.environ.get('CLIENT'),
        msg=f'Subject:Labirint\nPrice Alert! {title} now is  for {price} RUB!'
    )
    connection.quit()
