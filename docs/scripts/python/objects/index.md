# Predefined Objects and Methods (Python)

Python scripts connects to SeaTable Base with the python library [seatable-api](https://pypi.org/project/seatable-api/). You can find the source code on [GitHub](https://github.com/seatable/seatable-api-python).

This manual list all available objects and methods that are availabe within python scripts in SeaTable.

!!! Hint "Need specific function?"

    The Python class `seatable_api` does not yet cover all available functions of the SeaTable API. If you are missing a special function, please contact us at [support@seatable.io](mailto:support@seatable.io) and we will try to add the missing functions.

For a more detailed description of the used parameters, refer to the data model at the [SeaTable API Reference](https://api.seatable.io/reference/models).

## Authentication

!!! tip "Don't forget to authenticate"

    Every python script requires an authorization. All the examples does not contain the required lines of code.

    ```
    from seatable_api import Base, context
    base = Base(context.api_token, context.server_url)
    base.auth()
    ```

## Base object

Base represents a table in SeaTable. The `base` object provide a way to read, manipulate and output data in/from your base. The following methods are available.
