import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

PRODUCT_URL = "https://www.flipkart.com/vaseline-intensive-care-deep-moisture-body-lotion/p/itm74b8bcc8e4bc8?pid=MSCFKEQ5UYVGXGKS&lid=LSTMSCFKEQ5UYVGXGKS6RMIMX&marketplace=FLIPKART"
EMAIL = "nehaisarockstar93@gmail.com"
PASSWORD = YOUR_EMAIL_PASSWORD


headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Apple WebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/88.0.4324.104 Safari/537.36",
}

response = requests.get(url=PRODUCT_URL, headers=headers)
response.raise_for_status()
link = response.url

soup = BeautifulSoup(response.content, "lxml")
# <div class="_30jeq3 _16Jk6d">₹299</div>
# <span class="B_NuCI">…</span>
price_string = str(soup.find(name="div", class_="_30jeq3 _16Jk6d").getText())
price = int(price_string[1:])
product = soup.find(name="span", class_="B_NuCI").getText()
print(price)

if price < 250:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs="nkrocks93@gmail.com",
                            msg=f"Subject:Low Price Alert!\n\nYour {product} is now at ₹{price}.\n\n{link}".encode("utf-8"))

