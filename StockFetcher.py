import requests
import re

from .CrawledStock import CrawledStock
from bs4 import BeautifulSoup

class StockFetcher():
    def fetch(self):
        r = requests.get("https://www.tradegate.de/index2.php")
        doc = BeautifulSoup(r.text, "html.parser")

        all_right_rowlink = doc.find_all(class_="full grid right rowlink")
        for all_right_rowlink_element in all_right_rowlink:
            left_longname = all_right_rowlink_element.find_all(class_="left longname")

            for stock_entry in left_longname:
                '''print(einzelner.prettify())'''
                stock = stock_entry.contents[0]
                if "Penny" in stock.get("id"):
                    yield CrawledStock(stock,stock,stock,stock)
