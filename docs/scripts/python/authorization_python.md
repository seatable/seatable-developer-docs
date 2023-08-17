# Authorization

Python (in comparision to Javascript) scripts need an authentication. 

You can use two methods to obtain authorization to read and write a base.

1. One way is to use the api token of the base, the token can be directly generated on the web side. Read directly from context.api_token in the cloud environment.

1. Another method is to use your username and password to initialize an `account` object, and then call the `account` interface to get a `base` object. The first method is much easier.

!!! Danger "Protect your credentials"

    Please be aware that a python script is readable for all users, who have access to this base. Therefore be careful if you store your username and password to a python script.

## Authorization with API-Token

``` python
from seatable_api import Base, context
base = Base(context.api_token, context.server_url)
base.auth()
```

## Authorization with account object

``` python
from seatable_api import Account
account = Account(username, password, server_url)
account.auth()
base = account.get_base(workspace_id, base_name)
```