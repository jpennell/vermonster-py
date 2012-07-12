import requests


class Client(object):
    def __init__(self, oauth_id, oauth_secret):
        self.oauth_id = oauth_id
        self.oauth_secret = oauth_secret

    def ping(self):
        r = requests.get('https://api.cheddarapp.com/')
        print 'Pinged:', r.request.url
        print 'Status code:', r.status_code
