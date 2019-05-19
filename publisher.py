import boto3
import os
import logging
import datetime

## Publisher
class Publisher:
    def publish(name, output):
        return


## Publisher that writes to an SNS Topic
class SNS_Publisher(Publisher):
    rate_limit = 1 * time.hour

    def __init__(self, keystore):
        self.keystore = keystore

    def publish(self, name, output)
        if __should_rate_limit(name):
            return
        sns_topic = boto3.resource('sns').Topic(name)
        message = self.__format_output(name, output)
        sns_topic.publish(Message=message)
        self.keystore.set(name, {'time': datetime.datetime.now()})
        return

    def __format_output(self, name, output):
        return "Change detected in: %s".format(name)

    # Don't want to publish more than once per hour
    def __should_rate_limit(self, name):
        last = self.keystore.get(name)
        now = datetime.datetime.now()
        if now - last['time'] < self.rate_limit:
            return True
        return False


## Publisher that writes to CloudWatch logs
class Logger(Publisher):
    def __init__(self):
        self.logger = logging.getLogger()
        self.message_length = 20
        logger.setLevel(logging.INFO)

    def publish(self, name, output)
        logger.info("%s: %s".format(name, output[:self.message_length]))
        return
