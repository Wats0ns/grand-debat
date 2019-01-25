class Event:
    def __init__(self, data):
        self._id = data['_id']
        self.data = data
        pass

    def to_line(self):
        data = self.data
        author = data['author']
        # Some users don't have a type...
        if not author['userType']:
            author['userType'] = {'id': None, 'name': None}
        return [
            data['id'],
            data['fullAddress'],
            data['address'],
            data['body'],
            data['participantsCount'],
            data['zipCode'],
            data['city'],
            data['lat'],
            data['lng'],
            data['title'],
            data['startAt'],
            data['endAt'],
            data['createdAt'],
            data['comments']['totalCount'],
            data['enabled'],
            data['url'],
            data['themes'],
            author['events']['totalCount'],
            author['vip'],
            author['opinionsCount'],
            author['projectsCount'],
            author['argumentsCount'],
            author['proposalsCount'],
            author['userType']['id'],
            author['userType']['name'],
            author['votes']['totalCount']
        ]