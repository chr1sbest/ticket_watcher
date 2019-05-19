import boto3

class KeyStore:
    def get(self, key):
        return
    def set(self, key, value):
        return

class DynamoKeyStore(KeyStore):
    table_name = "page_watcher"

    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table(self.table_name)
        return

    def get(self, key):
        return self.table.get_item(Key={"key": key})["Item"]

    def set(self, key, value):
        value.update({"key": key})
        self.table.put_item(Item=value)
        return
