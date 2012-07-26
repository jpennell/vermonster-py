import requests
import json


class Client(object):
    """
    Vermonster client
    """
    def __init__(self, oauth_id, oauth_secret, token=None):
        """
        Initialize Client

        Parameters

        oauth_id: oauth client id, received when registering an app at http://cheddarapp.com
        oauth_secret: oauth client secret, received when registering an app at http://cheddarapp.com
        token: access token (if already received) default None
        """
        self.oauth_id = oauth_id
        self.oauth_secret = oauth_secret
        self.token = token

    def get_authentication_url():
        """
        Get cheddar authorization url
        """
        pass

    def get_access_token(code):
        """
        Get access token

        Parameters

        code: access code received after user logs in at the authorization url
        """
        pass

    def is_authenticated():
        """
        Is user authenticated?
        """
        pass
