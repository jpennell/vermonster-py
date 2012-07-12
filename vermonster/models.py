import requests
import json


class Client(object):
    def __init__(self, oauth_id, oauth_secret, token=None):
        self.oauth_id = oauth_id
        self.oauth_secret = oauth_secret
        self.token = token
        self.connection = 'https://api.cheddarapp.com'

        self.lists = ListManager(client=self)
        self.lists.tasks = TaskManager(client=self)

    def ping(self):
        r = requests.get('https://api.cheddarapp.com/')
        return r.status_code

    def get_authorization_url(self):
        return '%s/oauth/authorize?client_id=%s' % (self.connection, self.oauth_id)

    def get_token(self, code):
        #Set up request
        headers = {'grant_type': 'authorization_code', 'code': code}
        url = '%s/oauth/token' % self.connection

        #Make request to api
        r = requests.get(url, auth=(self.oauth_id, self.oauth_secret), headers=headers)

        #Set token
        self.token = r.body['access_token']

    def is_authorized(self):
        return True if self.token else False


class ListManager(object):
    def __init__(self, client):
        self.client = client

    def all(self, include_archived=False):
        #Set up request
        headers = {'Authorization': 'Bearer %s' % self.client.token}
        url = '%s/v1/lists' % self.client.connection

        #Make request to api
        r = requests.get(url, headers=headers)

        #Build lists
        lists = map(List.decode_from_json, json.loads(r.text))
        if not include_archived:
            lists = filter(lambda l: not l.archived_at, lists)
        return lists

    def find(self, id):
        pass


class List(object):
    def __init__(self):
        self.title = None
        self.archived_at = None

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def __repr__(self):
        return '<List: %s>' % self.title

    @staticmethod
    def decode_from_json(json_string):
        list = List()
        list.title = json_string['title']
        list.archived_at = json_string['archived_at']
        return list


class Task(object):
    def __init__(self):
        self.text = None

    def __unicode__(self):
        return self.text

    def __str__(self):
        return self.text

    def __repr__(self):
        return '<Task: %s>' % self.text

    @staticmethod
    def decode_from_json(json_string):
        task = Task()
        task.title = json_string['text']
        return task


class TaskManager(object):
    def __init__(self, client):
        self.client = client

    def all(self):
        pass

    def find(self, id):
        pass
