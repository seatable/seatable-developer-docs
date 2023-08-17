# Basic structure of Python script in SeaTable

The Python script runs on the server side and can be set to automatically run periodically, which is suitable for more complex data processing scenarios.

Python scripts can be run on your local machine or uploaded to the SeaTable cloud to run. Local operation is convenient for development and debugging, and scripts can be easily integrated into larger projects.

SeaTable uses currently Python 3.7 and a specific set of [supported libraries](/scripts/python/common_questions/#list-of-libraries-supported-in-the-cloud-environment).

## Authentication

Every python script must authenticate and requires at least these three lines at the beginning of the script. Read here all details about [authentication in python scripts](...). 

``` python
from seatable_api import Base, context
base = Base(context.api_token, context.server_url)
base.auth()
```

!!! warning "Multiple tokens in SeaTable"

    SeaTable provides multiple tokens to authenticate. But don't let you confuse. If you develop python scripts, just use the predefined variable `content.api_token` or provide a so called `API-Token` of a base. 

    All details can be found in the [SeaTable API Reference](https://api.seatable.io/reference/authentication).

It is even possible to develop a python in the way that it could be [executed in the cloud and local](...) without changing the code. 



## Available objects and methods

...

python braucht kein output object. print is the way to go. pretty json output erklären.

## Let's get concrete

Let's make this concrete and let us look at some basic examples. 

1. Jump to your seatable webinterface
2. Create a new Script of the type `Python`
3. copy the following code
4. run the script

You will learn from these examples, that it is quite easy to read, output and even manipulate the data of a base inside SeaTable with the predefined objects and the corresponding methods.


=== "Add, update and remove a row"

    This following example shows how to operate records in a table.

    ``` python
    from seatable_api import Base, context
    base = Base(context.api_token, context.server_url)
    base.auth() # (1)!

    rows = base.list_rows("Table1")

    row_data = {'name': 'Tom', 'age': 18}
    base.append_row('Table1', row_data)
    base.update_row('Table1', 'U_eTV7mDSmSd-K2P535Wzw', row_data)
    base.delete_row('Table1', 'U_eTV7mDSmSd-K2P535Wzw')
    ```

    1.   These three lines are always required to authorize against the base in SeaTable.

=== "abc"

    ...