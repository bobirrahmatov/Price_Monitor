#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#change the emails, from and to and CC before using
import requests
from bs4 import BeautifulSoup
import smtplib
import time

# set the headers and user string
headers = {
"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
}

response = requests.get('https://www.amazon.com/DJI-Mavic-Pro-Quadcopter-Battery/dp/B01MUAWOXB/ref=sr_1_1?keywords=drone+dji&qid=1584831724&sr=8-1', headers=headers)
soup = BeautifulSoup(response.content, "lxml")

# change the encoding to utf-8
soup.encode('utf-8')

def price_check():
  title = soup.find(id="productTitle").get_text()
  price = soup.find(id="priceblock_ourprice").get_text().replace(',', '').replace('$', '').replace(' ', '').strip()
  print(price)
  
  converted_price = float(price[0:5])
  print(converted_price)
  if(converted_price < 1000):
    notification_send()
  print(title.strip())

def notification_send():
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.ehlo()
  server.starttls()
  server.ehlo()

  server.login('youremailhere@gmail.com', 'yourpassword')

  subject = 'Drone price has been updated on Amazon'
  body = "Please go to this link to see the new price on Amazon: https://www.amazon.com/DJI-Mavic-Pro-Quadcopter-Battery/dp/B01MUAWOXB/ref=sr_1_1?keywords=drone+dji&qid=1584831724&sr=8-1 "

  msg = f"Subject: {subject}\n\n{body}"
  
  server.sendmail(
    'fromwhomemailhere@gmail.com',
    'towhomemailhere@gmail.com',
    msg
  )
  print('The Noticiation has been sent now')
  server.quit()

while(True):
  price_check()
  time.sleep(60*60)
