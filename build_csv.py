from granddebat.db import DbWrapper
from bson.objectid import ObjectId
from granddebat.event import Event
import csv
db = DbWrapper('config/db.json')

def get_events(last: ObjectId = None, size= 10):
    if not last:
        events = db.events.find().limit(size)
    else:
        events = db.events.find({'_id': {'$gt': last}}).limit(size)
    return events

def get_all():
    last = None
    while True:
        events = get_events(last)
        if not events:
            break
        event = None
        for event in events:
            yield Event(event)
        if not event:
            break
        last = event['_id']


events = []
header = ['id', 'fullAddress', 'address ','body', 'participantsCount', 'zipCode', 'city', 'lat', 'lng', 'title', 'startAt', 'endAt', 'createdAt',\
          'commentsCount', 'enabled', 'url', 'themes',
          'authorId', 'authorUsername', 'authorDisplayName', 'authorTotalEventsCount', 'authorVIP', 'authorOpinionsCount', 'authorProjectsCount', 'authorArgumentsCount',\
          'authorProposalsCount', 'authorTypeId', 'authorTypeName', 'authorTotalVotes' ]
filename = 'granddebat.csv'
with open(filename, "w") as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(header)
with open(filename, 'a') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    for event in get_all():
        print(event._id)
        events.append(event)
        if len(events) == 10:
            for event_to_write in events:
                writer.writerow(event_to_write.to_line())
            events = []
    for event_to_write in events:
        writer.writerow(event_to_write.to_line())