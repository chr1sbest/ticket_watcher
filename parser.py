## Parser uses BS4 to parse an HTML page to detect meaningful differences
class Parser:
    def parse(self):
        return ""

## ChappelleParser looks for tickets on ticketmaster
class ChappelleParser(Parser):
    def parse(self):
        return "chappelle"

## SummerLeagueParser looks for updates on the UNLV Page
class SummerLeagueParser(Parser):
    def parse(self):
        return "summer"
