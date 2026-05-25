import requests as r
from bs4 import BeautifulSoup
from datetime import datetime
import time
import schedule 

product_list = ['B0DWDRZQYB','B0FN4N9GCK','B0DHSCYDL2']
base_url = "https://www.amazon.in"
url = "https://www.amazon.in/dp/"

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/148.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9"
}

base_response = r.get(base_url, headers=headers)
cookies = base_response.cookies


print(datetime.now())
for prod in product_list:
      product_response = r.get(url+prod, headers=headers, cookies=cookies)
      soup = BeautifulSoup(product_response.text, "lxml")
      price_lines = soup.find_all(class_="a-price-whole")

      final_price = str(price_lines[0])
      final_price = final_price.replace( '<span class="a-price-whole">',"")
      final_price = final_price.replace('<span class="a-price-decimal">.</span></span>',"")
      print(url+prod, final_price)


