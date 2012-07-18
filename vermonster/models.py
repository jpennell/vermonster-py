import requests
import json


class Client(object):
    """
    Vermonster Client
    - A consumer of the Cheddar API (http://cheddarapp.com)
    """
    def __init__(self, oauth_id, oauth_secret, token=None):

        if not oauth_id:
            raise ValueError('Expected valid oauth_id')

        if not isinstance(oauth_id, str):
            raise ValueError('Expected valid oauth_id')

        if not oauth_secret:
            raise ValueError('Expected valid oauth_secret')

        if not isinstance(oauth_secret, str):
            raise ValueError('Expected valid oauth_secret')

        if token is not None:
            if not isinstance(token, str):
                raise ValueError('Expected valid token')

        self.oauth_id = oauth_id
        self.oauth_secret = oauth_secret
        self.token = token
        self.connection = 'https://api.cheddarapp.com'

        self.lists = ListManager(client=self)
        self.tasks = AllTasksManager(client=self)

    def ping(self):
        """
        Ping Cheddar api and return a status code
        """
        r = requests.get('https://api.cheddarapp.com/')
        return r.status_code

    def get_authorization_url(self):
        """
        Get Cheddar api authorization url
        """
        return '%s/oauth/authorize?client_id=%s' % (self.connection, self.oauth_id)

    def get_token(self, code):
        """
        Get authorization token for code from oauth endpoint
        """
        #Set up request
        headers = {'grant_type': 'authorization_code', 'code': code}
        url = '%s/oauth/token' % self.connection

        #Make request to api
        r = requests.get(url, auth=(self.oauth_id, self.oauth_secret), headers=headers)

        #Set token
        self.token = r.body['access_token']

    def is_authorized(self):
        """
        Check if user is authorized
        """
        return True if self.token else False


class ListManager(object):
    """
    List manager: Manages Cheddar lists from api
    """
    def __init__(self, client):

        if not client:
            raise ValueError('Expected valid client')

        if not isinstance(client, Client):
            raise ValueError('Expected valid client')

        self.client = client

    def _get_authorization_headers(self):
        headers = {'Authorization': 'Bearer %s' % self.client.token}
        return headers

    def _get_request_url_all(self):
        url = '%s/v1/lists' % self.client.connection
        return url

    def _get_lists_from_json(self, json_list, include_archived):

        if not isinstance(include_archived, bool):
            raise ValueError('Expected valid include_archived')

        if not json_list:
            return []
        else:
            if not isinstance(json_list, list):
                raise ValueError('Expected valid json_list')

        #Build lists
        lists = []
        for item in json_list:
            item = List.decode_from_json(item)
            item.client = self.client
            lists.append(item)

        #Filter lists
        if not include_archived:
            lists = filter(lambda l: not l.archived_at, lists)

        return lists

    def all(self, include_archived=False):
        """
        Get all Cheddar lists

        Parameters:

        include_archived=False
        - Set to True if you wish to return all lists, even if they are archived
        """
        #Set up request
        headers = self._get_authorization_headers()
        url = self._get_request_url_all()

        #Make request to api
        r = requests.get(url, headers=headers)
        json_string = json.loads(r.text)
        return self._get_lists_from_json(json_string=json_string, include_archived=include_archived)

    def get(self, id):
        """
        Get a single Cheddar list

        Parameters:

        id:
        - Id of the cheddar list, ie '42'
        """
        pass

    def create(self, title):
        """
        Create a cheddar list

        Parameters:

        title:
        - Title of the list to create
        """
        pass

    def reorder(self, list_ids):
        """
        Reorder Cheddar lists

        Parameters:

        list_ids:
        - Ordered list of list ids
        """
        pass


class List(object):
    """
    List model
    """
    def __init__(self, client=None):
        self.title = None
        self.archived_at = None
        self.client = client
        self.tasks = ListTaskManager(client=self.client)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def __repr__(self):
        return '<List: %s>' % self.title

    def update(self, title):
        """
        Update list

        Parameters:

        title:
        - New title for the list
        """
        pass

    def create_task(self, text):
        """
        Create task

        Parameters:

        text:
        - Text for the task
        """
        pass

    @staticmethod
    def decode_from_json(json_string):
        """
        Decode list from JSON
        """
        list = List()
        list.title = json_string['title']
        list.archived_at = json_string['archived_at']
        return list


class Task(object):
    """
    Task model
    """
    def __init__(self):
        self.text = None

    def __unicode__(self):
        return self.text

    def __str__(self):
        return self.text

    def __repr__(self):
        return '<Task: %s>' % self.text

    def update(self, text):
        """
        Update task

        Parameters:

        text:
        - Text for the task
        """
        pass

    @staticmethod
    def decode_from_json(json_string):
        """
        Decode task model from JSON
        """
        task = Task()
        task.title = json_string['text']
        return task


class ListTaskManager(object):
    def __init__(self, client):
        self.client = client

    def all(self):
        """
        Get all tasks
        """
        pass

    def create(self, text):
        """
        Create task

        Parameters:

        text:
        - Text for task
        """
        pass

    def reorder(self, task_ids):
        """
        Reorder tasks

        Parameters:

        task_ids:
        - Ordered list of task ids
        """
        pass

    def archive_completed(self):
        """
        Archive completed tasks
        """
        pass

    def archive_all(self):
        """
        Archive all tasks
        """
        pass


class AllTasksManager(object):
    """
    All tasks manager
    """
    def __init__(self, client):
        self.client = client

    def get(self, id):
        """
        Get task

        Parameters:

        id:
        - Id of task
        """
        pass
