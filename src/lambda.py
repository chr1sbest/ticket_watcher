import boto3
from botocore.errorfactory import ResourceNotFoundException

from src.parsers.chappelle_parser import ChappelleParser
from src.parsers.unlv_parser import SummerLeagueUNLVParser
from src.parsers.evenue_parser import SummerLeagueEvenueParser
from src.headless import driver
from src.keystore import DynamoKeyStore
from src.publisher import Logger, SNS_Publisher

# keystore required to store state and track diffs over time
keystore = DynamoKeyStore()

# parsers read HTML to look for specific information
parsers = [
        ChappelleParser(driver),
        SummerLeagueEvenueParser(driver),
        SummerLeagueUNLVParser(),
]

# publishers write to consumers that want to hear about diffs
publishers = [
        Logger(),
        SNS_Publisher(keystore)
]

def lambda_handler(event, context):
    for parser in parsers:
        name = parser.__class__.__name__

        # Check for diff between previous run and current
        new_output = parser.parse()
        try:
            previous_output = keystore.get(name)
            if new_output == previous_output['text']:
                return
        except ResourceNotFoundException:
            pass

        # Publish to each publisher if new diff
        keystore.set(name, {'text': new_output})
        for publisher in publishers:
            publisher.Publish(parser, new_output)
    return
