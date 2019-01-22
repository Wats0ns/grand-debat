import json
from pymongo import MongoClient
from bson.objectid import ObjectId


class DbWrapper:
    def __init__(self, filename):
        with open(filename) as json_data:
            data = json.load(json_data)
            self.mongo_config = data
        self.connect()
        self.authors = self.mongo.authors
        self.events = self.mongo.events

    def connect(self):
        """connect to the mongo instance"""
        self.mongo = MongoClient("mongodb://{username}:{password}@{host}:{port}/?readPreference=primary".format(
                                    username=self.mongo_config["username"],
                                    password=self.mongo_config["password"],
                                    host=self.mongo_config["host"],
                                    port=self.mongo_config["port"]))
        self.mongo = self.mongo[self.mongo_config['database']]

    def upsert_event(self, event):
        self.events.update({'id': event['id']}, {'$set': event}, upsert=True)
