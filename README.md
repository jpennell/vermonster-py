# Vermonster (Python)

Consume all of the [Cheddar (API)](https://cheddarapp.com/developer).

**Want Ruby instead? Check out [vermonster](https://github.com/eturk/vermonster).**

# Objective

``` python
cheddar = vermonster.Client(oauth_id='oauth-id', oauth_secret='oauth-secret')
```

### Authentication

``` python
# Get the URL for the user to authorize the application.
url = cheddar.get_authorization_url()

# Do whatever to send the user to that URL...
# It redirects back to whatever you sent as callback URL.

# In your controller (or wherever the callback URL is)...
cheddar.get_token(code)

# You are now authorized!
cheddar.is_authorized()
```

### Lists

``` python
# Get all of your lists.
lists = cheddar.lists.all()

# Get a list called "Foobar" with an ID of 42.
foobar = cheddar.lists.get(id=42)

# Get the tasks in that list.
tasks = foobar.tasks.all()
tasks = cheddar.lists.get(id=42).tasks.all()

# Update that list.
foobar.update(title='Barfoo')

# Make a new list called "Barfoo".
barfoo = cheddar.lists.create(title='Barfoo')

# Reorder your lists.
cheddar.lists.reorder([42, 12, 23])
```

### Tasks

``` python
# Get one task.
task = cheddar.tasks.get(id=42)

# Update that task.
task.update(text='Boom')

# Create a task in a list.
foobar.tasks.create(text='Be awesome!')

# Reorder...
foobar.tasks.reorder([42, 12])

# Archive completed items
foobar.tasks.archive_completed()

# Archive all items!
foobar.tasks.archive_all()
```