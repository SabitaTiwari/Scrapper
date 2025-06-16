#python -m pip install requests
#python -m pip install beautifulsoup4


#go to git bash
#git config --global user name "Sabita Tiwari"
#git config --global user.email "sabita.tiwari613@gmail.com"


#git init ==>initialize git
#git status==> if you want to check what ae the status of files
#git diff==>if you want to check what are the changes
#git add .
#git commit -m "Finish Project"
#copy paste git code from github


#################
#1.change the code
#2.git add .
#3.git commit -m "your message"
#4.git push
###################

import json
import requests
from bs4 import BeautifulSoup


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