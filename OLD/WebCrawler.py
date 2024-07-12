import requests
from bs4 import BeautifulSoup
args = features="html.parser"

def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = "https://www.ebay.com/sch/i.html?_from=R40&_sacat=0&_nkw=anki+cozmo&_blrs=spell_check&_pgn=" + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll("a", {"class": "s-item__title"}):
            href = link.get("href")
            print(href)
        page += 1


trade_spider(1)