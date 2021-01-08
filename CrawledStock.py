class CrawledStock():
    def __init__(self, name, isin, url, stock):
        CrawledStock.name = stock.text
        CrawledStock.isin = (stock.get("href")[-12:-1])
        CrawledStock.url = ("http://www.tradegate.de/" + str(stock.get("href")))
