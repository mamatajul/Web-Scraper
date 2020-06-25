import time
import requests
from bs4 import BeautifulSoup
import smtplib

# The scraper site link to look for
URL = "https://www.amazon.in/Acer-SF315-52G-15-6-inch-i5-8250U-Integrated/dp/B07P9T6NFD/ref=sr_1_2?dchild=1&keywords=Acer+Swift+3&qid=1592927481&s=computers&sr=1-2"

# Your prefered browser
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0" }

def check_price():
    page = requests.get(URL, headers = headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text().strip()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = (price[2:8])

    if (converted_price < '45,000'):
        send_mail()

    print(title)
    print(converted_price)


    if (converted_price < '45,000'):
        send_mail()

def send_mail():
    # Set up the server
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls() # Encryption
    server.ehlo()

    server.login("mandalmamatajul@gmail.com", "lylqsjoafqnvthsz")

    # Email body
    subject = "The Acer Swift 3 Price Fell Down!"
    body = "Check the Amazon link https://www.amazon.in/Acer-SF315-52G-15-6-inch-i5-8250U-Integrated/dp/B07P9T6NFD/ref=sr_1_2?dchild=1&keywords=Acer+Swift+3&qid=1592927481&s=computers&sr=1-2"

    msg = f"Subject: {subject} \n\n {body}"
    server.sendmail(
        "fromdemoemail@gmail.com",
        "todemoeamil@gmail.com",
        msg
    )
    print("Email has been sent!.")
    server.quit()
# Checks at regular interval
while(True):
    check_price()
    time.sleep(86400)
