import requests
from bs4 import BeautifulSoup
from base_parser import Parser

evenue_url = "https://ev2.evenue.net/cgi-bin/ncommerce3/SEGetEventInfo?ticketCode=GS%3AUNLV%3ATMC%3ATMC071319%3A&linkID=unlv&shopperContext=&pc=&caller=&appCode=&groupCode=NBA&cgc="

## SummerLeagueParser looks for event updates on the UNLV Page
class SummerLeagueEvenueParser(Parser):
    def parse(self):
        import ipdb; ipdb.set_trace()
        result = requests.get(evenue_url)
        soup = BeautifulSoup(result.content)
        # BLOCKED BECAUSE NO JS
        # performances = soup.find_all("table", {"class": "table-condensed"})
        # event_array = []
        # for event in events:
        #     event_array.append(str(event))
        # return ''.join(event_array)
        return ""

"""
Example output:
"""
