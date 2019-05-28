import requests
from time import sleep
from bs4 import BeautifulSoup

## SummerLeagueParser looks for event updates on the UNLV Page
class SummerLeagueEvenueParser():
    url  = "https://ev2.evenue.net/cgi-bin/ncommerce3/SEGetEventInfo?ticketCode=GS%3AUNLV%3ATMC%3ATMC071319%3A&linkID=unlv&shopperContext=&pc=&caller=&appCode=&groupCode=NBA&cgc="
    def __init__(self, driver):
        self.driver = driver

    def parse(self):
        self.driver.get(self.url)
        sleep(1)
        html = self.driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
        soup = BeautifulSoup(html, 'html.parser')
        events = soup.find_all("table", {"class": "table-condensed"})
        event_array = []
        for event in events:
            event_array.append(str(event))
        return ''.join(event_array)

"""
Example output:
"""
