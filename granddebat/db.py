import json
from pymongo import MongoClient, UpdateOne
from bson.objectid import ObjectId
#from pymongo import InsertOne, DeleteMany, ReplaceOne, UpdateOne

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

    def clean_event(self, event):
        """Do not keep personnal data for citizens"""
        if not event['author']['userType'] or event['author']['userType']['id'] == '1':
            event['author']['username'] = None
            event['author']['displayName'] = None
            event['author']['id'] = None
        return event

    def upsert_event(self, event):
        event = self.clean_event(event)
        self.events.update({'id': event['id']}, {'$set': event}, upsert=True)

    def upsert_events(self, events):
        ops = []
        for event in events:
            event = self.clean_event(event)
            ops.append(UpdateOne({'id': event['id']}, {'$set': event}, upsert=True))
        if not ops:
            return None
        self.events.bulk_write(ops)
