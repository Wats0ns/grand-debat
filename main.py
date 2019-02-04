#!/usr/bin/env python3
from graphqlclient import GraphQLClient
import sys
import ast
sys.path.append('.')
from granddebat.events_request import initial_payload, paginated_payload
import json
from granddebat.db import DbWrapper
import requests
import urllib

url = "https://granddebat.fr/graphql/internal"

headers = {'Content-type': 'application/json'}

db = DbWrapper('config/db.json')


def make_request(payload):
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.status_code)
    info_results = json.loads(response.text)
    info_events = info_results['data']['events']['edges']
    if 'extensions' in info_results:
        print(info_results['extensions'])
    if 'errors' in info_results:
        print(info_results['errors'])
    print(info_results['data']['events']['totalCount'])
    return info_events, info_results, int(info_results['data']['events']['totalCount'])


cursor = None
i = 0
events = []
while True:
    if not cursor:
        payload = initial_payload
    else:
        payload = paginated_payload.replace('cursor_replace', cursor)
    # print(repr(payload))
    # break
    events_results, results, count = make_request(payload)
    # print(events_results, results)
    print(results['data']['events']['pageInfo'])
    # break
    for result in events_results:
        # 500 errors
        if not result:
            print(results)
            print('#####')
            print(events_results)
            continue
        result = result['node']
        #print(result['title'])

        result['commentCount'] = result['comments']['totalCount']
        del result['commentCount']

        result['participantsCount'] = result['participants']['totalCount']
        del result['participants']
        events.append(result)
        if i % 10 == 0:
            print('[{i}/{total}]'.format(i=i, total= count))
            db.upsert_events(events)
            events = []
        i += 1
    if results['data']['events']['pageInfo']['hasNextPage']:
        cursor = results['data']['events']['pageInfo']['endCursor']
    else:
        break
print('[{i}/{total}]'.format(i=i, total=count))
db.upsert_events(events)
