# Predefined Objects and Methods (Python)

This is a list of all available objects and methods in SeaTable with python scripts.

For a more detailed description of the used parameters, refer to the data model at the [SeaTable API Reference](https://api.seatable.io/reference/models).

!!! tip "Don't forget to authenticate"

    Every python script requires an authorization. All the examples does not contain the required lines of code.

    ```
    from seatable_api import Base, context
    base = Base(context.api_token, context.server_url)
    base.auth()
    ```

## Base object

Base represents a table in SeaTable. The `base` object provide a way to read, manipulate and output data in/from your base. The following methods are available.
