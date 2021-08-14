import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = '<url_of_the_item_to_track>'

# type into Google: what is my user agent. Copy it in below
headers = {"User-Agent": '<user_agent>'}
# will be something like this: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36


def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    parsed_price = price[1:7].replace(',', '')
    converted_price = float(parsed_price[0:6])

    # if(converted_price < 1600):
    #     send_mail()

    print(title.strip())
    print(converted_price)
    
    if(converted_price < 1500): # change price to reflect the disired sale price
        send_mail()
   

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('<email_account_to_send_from>', '<password_for_that_account>')
    subject = "Price on your item dropped!"
    body = "Check the link to go to the item <item_url>"
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail('<from_email>', 'to_email', msg)
    print("Hey, email has been sent")
    
    server.quit()

while(True):
    check_price()
    time.sleep(3600)
    
    