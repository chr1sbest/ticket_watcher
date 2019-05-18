import boto3
import os

# keystore required to store state and track diffs over time
keystore = LambdaKeyStore()

# parsers read HTML to look for specific information
parsers = [ChappelleParser(), SummerLeagueParser()]

# publishers write to consumers that want to hear about diffs
publishers = [Logger(), SNS_Publisher(keystore)]

def lambda_handler(event, context):
    for parser in parsers:
        # Check for diff between previous run and current & exit if none
        new_output = parser.parse()
        previous_output = keystore.get(parser.__name__)
        if new_output == previous_output:
            return

        # Publish to each publisher if new diff
        keystore.store(parser.__name__, new_output)
        for publisher in publishers:
            publisher.Publish(parser.__name__, new_output)
    return
