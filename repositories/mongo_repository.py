from pymongo import MongoClient
from django.conf import settings


class MongoRepository:
    def __init__(self):
        self.client = MongoClient(
            host=settings.MONGO_DB_CONFIG['HOST'],
            port=settings.MONGO_DB_CONFIG['PORT'],
            username=settings.MONGO_DB_CONFIG['USER'],
            password=settings.MONGO_DB_CONFIG['PASSWORD'],
        )
        self.db = self.client[settings.MONGO_DB_CONFIG['DB_NAME']]

    def find_one(self, collection, query):
        return self.db[collection].find_one(query)

    def insert_one(self, collection, document):
        return self.db[collection].insert_one(document)

    def update_one(self, collection, query, update):
        return self.db[collection].update_one(query, {"$set": update})

    def delete_one(self, collection, query):
        return self.db[collection].delete_one(query)
