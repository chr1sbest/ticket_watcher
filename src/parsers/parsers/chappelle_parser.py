import requests
from bs4 import BeautifulSoup
from base_parser import Parser

## ChappelleParser looks for tickets on livenation
url = "https://www.livenation.com/artists/78595/dave-chappelle"
class ChappelleParser(Parser):
    def parse(self):
        result = requests.get(url)
        soup = BeautifulSoup(result.content)
        # TODO run a headless browser to render JS
        return "chappelle"
