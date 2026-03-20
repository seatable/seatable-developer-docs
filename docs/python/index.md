# Python

Python scripts connect to SeaTable bases with the library [seatable-api](https://pypi.org/project/seatable-api/). The source code is available on [GitHub](https://github.com/seatable/seatable-api-python).

The same library is used both **inside SeaTable scripts** and in **external Python programs**. The only difference is how you authenticate. All objects and methods work identically in both contexts.

!!! info "Relationship to the SeaTable API"

    Every `seatable-api` method is a wrapper around the [SeaTable REST API](https://api.seatable.com). The library covers the most common base operations but not every API endpoint (e.g. admin, webhooks, or team management). For anything not covered by this library, you can call the [API](https://api.seatable.com) directly. For column type formats and data models, see the [API model reference](https://api.seatable.com/reference/models).

## Installation

```
pip install seatable-api
```

!!! info "Not needed for scripts inside SeaTable"

    When running scripts directly in SeaTable (via the built-in Python editor), `seatable-api` is already available. No installation required.

## Script vs. External Client

| | Script in SeaTable | External client |
|---|---|---|
| Authentication | `context.api_token` (automatic) | API token or account credentials (manual) |
| `context` object | Available | Not available |
| `current_row` (button execution) | Available | Not available |
| Python version | 3.12 | Your choice |
| Available libraries | [Predefined set](https://seatable.com/help/supported-python-libraries/) | Unlimited |
| Execution | SeaTable server (Python Pipeline) | Your own machine/server |

## Authentication

### In a SeaTable script

Within SeaTable's integrated Python editor, the `context` object provides the authentication credentials automatically:

```python
from seatable_api import Base, context
base = Base(context.api_token, context.server_url)
base.auth()
```

### In an external program

When running Python on your own machine or server, you provide the API token and server URL directly. API tokens can be [generated in the SeaTable web interface](https://seatable.com/help/create-api-tokens/).

```python
from seatable_api import Base

API_TOKEN = 'your-api-token'  # (1)!
SERVER_URL = 'https://cloud.seatable.io'

base = Base(API_TOKEN, SERVER_URL)
base.auth()
```

1. Avoid exposing credentials directly in the code. Use environment variables or `.env` files instead.

??? question "Authentication with account credentials"

    Instead of using an API token (which is specific to a base), you can authenticate with your SeaTable account credentials. This gives you access to all your bases.

    ```python
    from seatable_api import Account
    account = Account(username, password, server_url)
    account.auth()
    base = account.get_base(workspace_id, base_name)
    ```

    To find the `workspace_id`, open the base in your browser. The URL looks like `https://cloud.seatable.io/workspace/84254/dtable/MyBase`.

??? question "Handling authorization expiration"

    For long-running programs, authorization may expire. Catch `AuthExpiredError` to re-authenticate:

    ```python
    from seatable_api import Base, context
    from seatable_api.exception import AuthExpiredError

    base = Base(context.api_token, context.server_url)
    base.auth()

    while True:
        try:
            base.append_row('Table1', {"xxx": "xxx"})
            ...
        except AuthExpiredError:
            base.auth()
    ```

## Rate and Size Limits

Since every method call is an API request, scripts are subject to [rate](https://api.seatable.com/reference/limits#general-rate-limits) and [size](https://api.seatable.com/reference/limits#size-limits) limits. Tips to stay within limits:

- Be careful with operations in `for` or `while` loops
- Use **batch operations** whenever possible:
    - `base.batch_append_rows`
    - `base.batch_update_rows`
    - `base.batch_delete_rows`
    - `base.batch_update_links`
- Learn more about [optimizing your API calls](https://seatable.com/api-optimization/)
