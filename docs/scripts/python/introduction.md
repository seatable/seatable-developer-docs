# Introduction

Python scripts connects to SeaTable databases with the python library [seatable-api](https://pypi.org/project/seatable-api/). You can find the source code on [GitHub](https://github.com/seatable/seatable-api-python). Python scripts can be and executed directly in a base using a SeaTable component called Python Pipeline. You can also choose to run scripts locally. Where you run your Python script has consequences on the available libraries and authentication.

!!! warning "Indents are important"

    Please take care of indentations! Indentation is mandatory in Python to define the blocks of statements. The number of spaces must be uniform in a block of code. It is preferred to use whitespaces instead of tabs to indent in Python. If the indentations are wrong, the scripts will throw errors or not work as expected!

## Libraries

The current Python Pipeline ships with Python 3.12 and a bundle of [third party libraries](/scripts/python/common_questions/#list-of-libraries-supported-in-the-cloud-environment). One of the bundled library and the main library to interact with SeaTable bases is [seatable-api](https://github.com/seatable/seatable-api-python).

At a minimum, the Base and context function from the seatable-api library must be imported. Additionally, you can import functions from the bundled libraries.

```python
from seatable_api import Base, context
from datetime import datetime
```

When running Python scripts locally, you can take advantages of the uncountable number of Python libraries. 

## Authentication

Python (in comparison to JavaScript) scripts need an authentication. SeaTable provides multiple tokens to obtain authorization to read and write a base. But let's keep things simple! If you develop Python scripts in SeaTable, just use the context object `context.api_token` or provide a so called `API token` of a base (see [Authorization with API token below](#authorization-with-api-token)). If you want to learn more about authentication, all details can be found in the [SeaTable API Reference](https://api.seatable.com/reference/authentication).

!!! warning "Protect your credentials"

    Please be aware that a python script is readable for all users, who have access to this base. Therefore try to avoid exposing your credentials directly in the code! Use environment variables or `.venv` files instead.

### Authorization with API token

Using this method, you will use the API token of the base. Within SeaTable's integrated Python editor, authentication can be done very simply thanks to the [context object](https://developer.seatable.com/scripts/python/objects/context/). In local environment, the context object is not available. You'll have to provide directly the `api_token` and the `server_url` variables. The API token can be directly [generated in the web interface](https://seatable.com/help/erzeugen-eines-api-tokens/).

=== "SeaTable's integrated Python editor"

    ```python
    from seatable_api import Base, context  # (1)!
    base = Base(context.api_token, context.server_url)
    base.auth()
    ```

    1. Don't forget to import `context`. Thanks to this, you won't have to manually provide any credential.

=== "Local execution"

    ```python
    from seatable_api import Base # (1)!

    API_TOKEN = 'c3c75dca2c369848455a39f4436147639cf02b2d' # (2)!
    SERVER_URL = 'https://cloud.seatable.io'

    base = Base(API_TOKEN, SERVER_URL)
    base.auth()
    ```

    1. No need to import `context` here as it won't actually be available.
    
    2. This is for demonstration purpose only: try to avoid exposing your credentials directly in the code! Use environment variables or `.venv` files instead.

It is even possible to develop a Python script in the way that it could be [executed both in the cloud and locally](/scripts/python/common_questions/#how-to-make-the-script-support-both-local-and-cloud-run) without changing the code.

### Authorization with account object

Instead of using an API token, you can also authenticate using the `account` object. Doing so, you'll have to provide both your `username` and `password` (in addition to the `server_url` variable). 

Whereas the API token is specific to a base, the `account` object is general and gives you access to all your bases (as when you log on SeaTable). To get a specific base, you'll have to use the `get_base` function, given the workspace ID `workspace_id` and the name of the base `base_name`. To get the workspace ID:

1. Go to the SeaTable home page.

2. Click the base whose workspace ID you want to determine.

3. When the selected base has opened, you can read the Workspace ID at the top of the page URL, which actually looks like *https://cloud.seatable.io/workspace/`84254`/dtable/MyBase* (or any `server_url` instead of *https://cloud.seatable.io*).


```python
from seatable_api import Account
account = Account(username, password, server_url)
account.auth()
base = account.get_base(workspace_id, base_name)
```

### Authorization expiration handling

!!! info "This feature works with SeaTable version 3.1+"

In some cases, the program needs to run for a (very) long time, the code of base operations usually being located in a `while` or `for` loop. . In this case, authorization may expire during execution and cause the program to break. We provide an exception called `AuthExpiredError` that can be caught for reauthorization.

```python
from seatable_api import Base, context
from seatable_api.exception import AuthExpiredError

server_url = context.server_url or 'https://cloud.seatable.io'
api_token = context.api_token or 'c3c75dca2c369849455a39f4436147639cf02b2d'

base = Base(api_token, server_url)
base.auth()

while True: # (1)!
    try:
        base.append_row('Table1', {"xxx":"xxx"})
        ...
    except AuthExpiredError:
       base.auth()
```

1. Always be careful with infinite loops!

## Base operations limits

As Python scripts are tailored for huge base manipulations and because they actually rely on the [SeaTable API](https://api.seatable.com), you might encounter [Rate](https://api.seatable.com/reference/limits#general-rate-limits) or [Size](https://api.seatable.com/reference/limits#size-limits) limits if you are not vigilant. Here are few tips to avoid reaching the limits:

- Be always careful with operations in `for` or `while` loops (ensure the ending conditions will be reached)

- Use *batch* operations as often as possible. Replace for example several `base.append_row` calls with a single `base.batch_append_rows` call. Here are the main batch function:

    - `base.batch_append_rows`
    - `base.batch_update_rows`
    - `base.batch_delete_rows`
    - `base.batch_update_links`

- Learn more about [lower your calls](https://seatable.com/api-optimization/)
