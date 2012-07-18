def get_authorization_headers(token):
    headers = {'Authorization': 'Bearer %s' % token}
    return headers


def get_request_url_all():
    url = 'https://api.cheddarapp.com/v1/lists'
    return url


def get_request_url_get(id):
    url = 'https://api.cheddarapp.com/v1/lists/%s' % (id)
    return url
