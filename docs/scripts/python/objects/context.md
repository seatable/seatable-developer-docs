# Context

When the script is running in the cloud, the context object provides a context environment. Here's how to use it

## server_url

!!! info "server_url"

    Server URL, used to initialize Base.

    ``` python
    context.server_url
    ```

    __Example__

    ``` python
    from seatable_api import context
    print(context.server_url)
    ```

## api_token

!!! info "api_token"

    API token for access a base.

    ``` python
    context.api_token
    ```

    __Example__

    ``` python
    from seatable_api import context
    print(context.api_token)
    ```

## current_table

!!! info "current_table"

    The name of the table that the current user is viewing when the user runs a script manually.

    ``` python
    context.current_table
    ```

    __Example__

    ``` python
    from seatable_api import context
    print(context.current_table)
    ```

## current_row

!!! info "current_row"

    When the user manually runs a script, the line where the cursor is currently located.

    ``` python
    context.current_row
    ```

    __Example__

    ``` python
    from seatable_api import context
    print(context.current_row)
    ```

## current_username

!!! info "current_username"

    The System ID of the user who runs the script manually (in old verison, it is called current_user_id).

    ``` python
    context.current_username
    ```

    __Example__

    ``` python
    from seatable_api import context
    print(context.current_username)
    ```

## current_id_in_org

!!! info "current_id_in_org"

    The id of the user in the team, it can be set by the team admin via Web UI.

    ``` python
    context.current_id_in_org
    ```

    __Example__

    ``` python
    from seatable_api import context
    print(context.current_id_in_org)
    ```
