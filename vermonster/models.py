import requests
import json


class Client(object):
    """
    Vermonster client
    - A consumer of the Cheddar API (http://cheddarapp.com)
    """
    def __init__(self, oauth_id, oauth_secret, token=None):
        """
        Initialize Client

        Parameters

        oauth_id: oauth client id, received when registering an app at http://cheddarapp.com
        oauth_secret: oauth client secret, received when registering an app at http://cheddarapp.com
        token: access token (if already received) default None
        """

        if not oauth_id or not isinstance(oauth_id, str):
            raise ValueError('Expected valid oauth_id')

        if not oauth_secret or not isinstance(oauth_secret, str):
            raise ValueError('Expected valid oauth_secret')

        if token and not isinstance(token, str):
            raise ValueError('Expected valid token')

        self.oauth_id = oauth_id
        self.oauth_secret = oauth_secret
        self.token = token

    def get_authentication_url(self, redirect_uri=None, state=None):
        """
        Get cheddar authorization url

        Parameters

        redirect_uri: An optional redirect URI. If none is provided, the one used when you registered your app will be used. If one is provided, it must contain the app's redirect URI as its prefix.
        state: Put whatever you want here. It will be passed back when the users authorized or declines your request. A common practice is to use some sort of identifier to identify the user making the request. This value will be truncated to 255 characters.
        """

        if redirect_uri and not isinstance(redirect_uri, str):
            raise ValueError('Expected valid redirect_uri')

        if state and not isinstance(state, str):
            raise ValueError('Expected valid state')

        url = "https://api.cheddarapp.com/oauth/authorize?client_id=%s" % self.oauth_id

        if redirect_uri:
            url = url + "&redirect_uri=%s" % redirect_uri

        if state:
            url = url + "&state=%s" % state

        return url

    def get_access_token(self, code):
        """
        Get access token

        Parameters

        code: access code received after user logs in at the authorization url
        """
        pass

    def is_authenticated(self):
        """
        Is user authenticated?
        """
        return True if self.token else False
