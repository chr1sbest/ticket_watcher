import requests
from bs4 import BeautifulSoup
from base_parser import Parser

unlv_url = "https://www.unlvtickets.com/eventInfo/spe/719/2019-nba-summer-league/"

## SummerLeagueParser looks for event updates on the UNLV Page
class SummerLeagueUNLVParser(Parser):
    def parse(self):
        result = requests.get(unlv_url)
        soup = BeautifulSoup(result.content)
        performances = soup.find_all("div", {"id": "performances"})
        events = performances[0].find_all("li", {"class": "eventinfo"})
        event_array = []
        for event in events:
            event_array.append(str(event))
        return ''.join(event_array)

"""
Example output:

<li class="nopadtop eventinfo">\r\n\t\t\t\t\t\t\t\t\t\t\t\tJuly 05, 2019 - TIME TBD\t\t\t\t\t\t\t\t\t\t  </li><li class="eventinfo">\r\n\t\t\t\t\t\t\t\t\t\t\t\tJuly 06, 2019 - TIME TBD\t\t\t\t\t\t\t\t\t\t  </li><li class="eventinfo">\r\n\t\t\t\t\t\t\t\t\t\t\t\tJuly 07, 2019 - TIME TBD\t\t\t\t\t\t\t\t\t\t  </li><li class="eventinfo">\r\n\t\t\t\t\t\t\t\t\t\t\t\tJuly 08, 2019 - TIME TBD\t\t\t\t\t\t\t\t\t\t  </li><li class="eventinfo">\r\n\t\t\t\t\t\t\t\t\t\t\t\tJuly 09, 2019 - TIME TBD\t\t\t\t\t\t\t\t\t\t  </li><li class="eventinfo">\r\n\t\t\t\t\t\t\t\t\t\t\t\tJuly 10, 2019 - TIME TBD\t\t\t\t\t\t\t\t\t\t  </li><li class="eventinfo">\r\n\t\t\t\t\t\t\t\t\t\t\t\tJuly 11, 2019 - TIME TBD\t\t\t\t\t\t\t\t\t\t  </li><li class="eventinfo">\r\n\t\t\t\t\t\t\t\t\t\t\t\tJuly 12, 2019 - TIME TBD\t\t\t\t\t\t\t\t\t\t  </li><li class="eventinfo">\r\n\t\t\t\t\t\t\t\t\t\t\t\tJuly 13, 2019 - TIME TBD\t\t\t\t\t\t\t\t\t\t  </li><li class="eventinfo">\r\n\t\t\t\t\t\t\t\t\t\t\t\tJuly 14, 2019 - TIME TBD\t\t\t\t\t\t\t\t\t\t  </li><li class="noborder eventinfo">\r\n\t\t\t\t\t\t\t\t\t\t\t\tJuly 15, 2019 - TIME TBD\t\t\t\t\t\t\t\t\t\t  </li>
"""
