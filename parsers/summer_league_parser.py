import requests
from bs4 import BeautifulSoup
from base_parser import Parser

url = "https://www.unlvtickets.com/eventInfo/spe/719/2019-nba-summer-league/"

## SummerLeagueParser looks for event updates on the UNLV Page
class SummerLeagueParser(Parser):
    def parse(self):
        result = requests.get(url)
        soup = BeautifulSoup(result.content)
        performances = soup.find_all("div", {"id": "performances"})
        events = performances[0].find_all("li", {"class": "eventinfo"})
        event_array = []
        for event in events:
            event_array.append(str(event))
        return ''.join(event_array)
