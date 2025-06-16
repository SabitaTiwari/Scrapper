#python -m pip install requests
#python -m pip install beautifulsoup4


import requests
from bs4 import BeautifulSoup
import json

url="http://books.toscrape.com/"

def scrape_book(url):
    response=requests.get(url)
    #set encoding explicitly to handle special characters correctly
    response.encoding=response.apparent_encoding
    if response.status_code!=200:
        return
    soup= BeautifulSoup(response.text,"html.parser")
    books= soup.find_all("article",class_="product_pod")
    
    for book in books:
        title=book.h3.a["title"]
       #print(title)
        price_text=book.find("p",class_="price_color").text
        #print(price_text,type(price_text))
        currency=price_text[0]
        price=float(price_text[1:])
        print(title,currency,price)
scrape_book(url)