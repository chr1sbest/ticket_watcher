import requests
from bs4 import BeautifulSoup
from time import sleep

## ChappelleParser looks for tickets on livenation
class ChappelleParser():
    url  = "https://www.livenation.com/artists/78595/dave-chappelle"

    def __init__(self, driver):
        self.driver = driver

    def parse(self):
        self.driver.get(self.url)
        sleep(1)
        html = self.driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
        soup = BeautifulSoup(html, 'html.parser')
        events = soup.find_all("a", {"class": "event-link"})
        event_array = []
        for event in events:
            if event.text.lower().find('punchline'):
                event_array.append(event.text)
        return ''.join(event_array)
