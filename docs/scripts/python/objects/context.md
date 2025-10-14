# Context

When the script is running in the cloud, the context object provides a context environment. Here's how to use it.

!!! warning "Function import required"

    To use these functions, the context module must be imported.

    ```
    from seatable_api import context
    ```

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

    The name of the table that the current user is viewing when the script is run.

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

    The line which triggered the script run:
    
    - the line where the cursor is currently located (if the script is run manually)
    - the line from which the button to launch the script was clicked (if the script is run from a button-type column click)
    - each line triggering the automation (if the script is run by an automation rule)

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

    The system ID of the user who runs the script manually (it was previously called `current_user_id`). It is a unique identifier ending by `@auth.local`.

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

    The id of the user in the team, it can be set by the team admin via the web interface.

    ``` python
    context.current_id_in_org
    ```

    __Example__

    ``` python
    from seatable_api import context
    print(context.current_id_in_org)
    ```
