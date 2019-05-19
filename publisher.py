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
    rate_limit = datetime.timedelta(hours = 1)
    date_format = "%Y-%m-%d %H:%M:%S"

    def __init__(self, keystore):
        self.keystore = keystore

    def publish(self, name, output):
        now = datetime.datetime.now()
        if __should_rate_limit(name, now):
            return
        sns_topic = boto3.resource('sns').Topic(name)
        message = self.__format_output(name, output)
        sns_topic.publish(Message=message)
        formatted = now.strftime(date_format)
        self.keystore.set(name, {'time': formatted})
        return

    def __format_output(self, name, output):
        return "Change detected in: %s".format(name)

    # Don't want to publish more than once per hour
    def __should_rate_limit(self, name, now):
        stored_time = self.keystore.get(name)['time']
        last = now.strptime(date_format)
        if last + self.rate_limit > now:
            return True
        return False


## Publisher that writes to CloudWatch logs
class Logger(Publisher):
    def __init__(self):
        self.logger = logging.getLogger()
        self.message_length = 20
        self.logger.setLevel(logging.INFO)

    def publish(self, name, output):
        formatted = "%s: %s".format(name, output[:self.message_length])
        self.logger.info(formatted)
        return
