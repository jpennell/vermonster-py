import requests
import json


class Client(object):
    def __init__(self, oauth_id, oauth_secret, token=None):
        self.oauth_id = oauth_id
        self.oauth_secret = oauth_secret
        self.token = token
        self.connection = 'https://api.cheddarapp.com'

        self.lists = ListManager(client=self)
        self.tasks = AllTasksManager(client=self)

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
        lists = []
        for item in json.loads(r.text):
            list = List.decode_from_json(item)
            list.client = self
            lists.append(list)

        if not include_archived:
            lists = filter(lambda l: not l.archived_at, lists)

        return lists

    def get(self, id):
        pass

    def create(self, title):
        pass

    def reorder(self, list_ids):
        pass


class List(object):
    def __init__(self, client=None):
        self.title = None
        self.archived_at = None
        self.client = client
        self.tasks = TaskManager(client=self.client)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def __repr__(self):
        return '<List: %s>' % self.title

    def update(self, title):
        pass

    def archive(self):
        pass

    def create_task(self):
        pass

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

    def update(self, text):
        pass

    def reorder(self, task_ids):
        pass

    def archive_completed(self):
        pass

    def archive_all(self):
        pass

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

    def get(self, id):
        pass

    def create(self, text):
        pass


class AllTasksManager(object):
    def __init__(self, client):
        self.client = client

    def get(self, id):
        pass
