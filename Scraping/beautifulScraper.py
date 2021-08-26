"""
https://www.youtube.com/watch?v=rONhdonaWUo

https://www.youtube.com/watch?v=ng2o98k983k&t=2237s
"""
import bs4
from bs4 import BeautifulSoup 
import requests as req
import datetime


def parsePrice():
    r = req.get("https://finance.yahoo.com/quote/%5EIXIC?p=^IXIC") #NASDAQ price
    soup = bs4.BeautifulSoup(r.text,"lxml")
    currentPrice = soup.find_all("div", {"class":"My(6px) Pos(r) smartphone_Mt(6px)"})[0].find("span").text
    #print(f'NASDAQ current price: {currentPrice}')
    return currentPrice

while (True):
    now = datetime.datetime.now()
    print(f'The current price of the NASDAQ is: {str(parsePrice())} @  {now}')