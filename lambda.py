import boto3
import os

from parsers import ChappelleParser, SummerLeagueParser

# keystore required to store state and track diffs over time
keystore = DynamoKeyStore()

# parsers read HTML to look for specific information
parsers = [
        ChappelleParser(),
        SummerLeagueParser()
]

# publishers write to consumers that want to hear about diffs
publishers = [
        Logger(),
        SNS_Publisher(keystore)
]

def lambda_handler(event, context):
    for parser in parsers:
        name = parser.__class__.__name__

        # Check for diff between previous run and current & exit if none
        new_output = parser.parse()
        previous_output = keystore.get(key)
        if new_output == previous_output['text']:
            return

        # Publish to each publisher if new diff
        keystore.store(key, {'text': new_output})
        for publisher in publishers:
            publisher.Publish(name, new_output)
    return
