# Authorization

Python (in comparision to Javascript) scripts need an authentication.

You can use two methods to obtain authorization to read and write a base.

1. One way is to use the api token of the base, the token can be directly generated on the web side. Read directly from context.api_token in the cloud environment.

1. Another method is to use your username and password to initialize an `account` object, and then call the `account` interface to get a `base` object. The first method is much easier.

!!! Danger "Protect your credentials"

    Please be aware that a python script is readable for all users, who have access to this base. Therefore be careful if you store your username and password to a python script.

## Authorization with API-Token

```python
from seatable_api import Base, context
base = Base(context.api_token, context.server_url)
base.auth()
```

## Authorization with account object

```python
from seatable_api import Account
account = Account(username, password, server_url)
account.auth()
base = account.get_base(workspace_id, base_name)
```

## Authorization expiration handling

!!! note "Note, this feature works with SeaTable version 3.1+"

In some cases, the program need to run for a long time, we put the base operation code into a while or for loop. Authorization may expire during execution and cause the program to break. We provide an exception called `AuthExpiredError` that can be caught for reauthorization.

```python
from seatable_api import Base, context
from seatable_api.exception import AuthExpiredError

server_url = context.server_url or 'https://cloud.seatable.io'
api_token = context.api_token or 'c3c75dca2c369849455a39f4436147639cf02b2d'

base = Base(api_token, server_url)
base.auth()

while True:
    try:
        base.append_row('Table1', {"xxx":"xxx"})
        ...
    except AuthExpiredError:
       base.auth()
```
