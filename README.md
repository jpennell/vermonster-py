# Vermonster (Python)

Consume all of the [Cheddar (API)](https://cheddarapp.com/developer).

**Want Ruby instead? Check out [vermonster](https://github.com/eturk/vermonster).**
















##General

###Create a client instance

``` python
cheddar = vermonster.Client(oauth_id='oauth-id', oauth_secret='oauth-secret')
```

##Authentication

###Obtain authentication url

``` python
url = cheddar.get_authorization_url()
```

###Obtain an access token

``` python
cheddar.get_token(code)
```

###Determine if you have authenticated

``` python
cheddar.is_authorized()
```

##Lists

###Get all lists

``` python
lists = cheddar.lists.all()
```

###Get a single list

``` python
foo = cheddar.lists.get(id=42)
```

###Get a single list, including the tasks for that list

``` python
foo = cheddar.lists.get(id=42, include_active_tasks=True)
```

###Update the title of a list

``` python
foo = cheddar.lists.get(id=42)
foo.update(title="foobar")
```

###Create a new list
``` python
bar = cheddar.lists.create(title="barfoo")
```

###Archive a list

``` python
foo = cheddar.lists.get(id=42)
foo.archive()
```

###Reorder lists

``` python
cheddar.lists.reorder([42, 45, 78, 89])
```

##Tasks

###Get active tasks for a list
``` python
foo = cheddar.lists.get(id=42)
tasks = foo.tasks.all()

#Another way
tasks = cheddar.tasks.get_for_list(id=42)
```

###Get all tasks for a list

``` python
foo = cheddar.lists.get(id=42)
tasks = foo.tasks.all(include_archived=True)

#Another way
tasks = cheddar.tasks.get_for_list(id=42, include_archived=True)
```

###Get a single task

``` python
task = cheddar.tasks.get(id=23)
```

###Update a task

``` python
task = cheddar.tasks.get(id=23)
task.update(text="foo #bar")
```

###Archive a task

``` python
task = cheddar.tasks.get(id=23)
task.archive()
```

###Reorder tasks

``` python
foo = cheddar.lists.get(id=42)
foo.tasks.reorder([23, 67, 78, 34, 12])
```

###Archive all tasks in a list

``` python
foo = cheddar.lists.get(id=42)
foo.tasks.archive_all()
```

###Archive completed tasks in a list

``` python
foo = cheddar.lists.get(id=42)
foo.tasks.archive_completed()
```

##Users

###Get the currently authenticated user

``` python
user = cheddar.user
```












## Contributing

Vermonster-py is under active development, and we would really appreciate you helping us out! Here's how.

1. Fork this repository.
2. Take a look [at the issues](https://github.com/jpennell/vermonster-py/issues). What needs to be done?
3. Make a topic branch for what you want to do. Bonus points for referencing an issue (like `2-authentication`).
4. Make your changes.
5. Create a Pull Request.
6. Profit!