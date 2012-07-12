# Vermonster (Python)

Consume all of the [Cheddar (API)](https://cheddarapp.com/developer).
Inspired by [Vermonster (Ruby)](https://github.com/eturk/vermonster).

# Objective

``` python
cheddar = VermonsterClient(oauth_id='oauth-id', oauth_secret='oauth-secret')
```

### Authentication

``` python
# Get the URL for the user to authorize the application.
url = cheddar.authorize()

# Do whatever to send the user to that URL...
# It redirects back to whatever you sent as callback URL.

# In your controller (or wherever the callback URL is)...
cheddar.get_token(code)

# You are now authorized!
cheddar.is_authorized()
```