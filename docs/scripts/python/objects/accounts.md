# Python Objects: Account

Account provides an interface to list all Workspaces, add/copy/delete Bases, and obtain access rights to a Base.

!!! tip "Separate Authentication required"

    Account requires a separate authentication.

    ```
    from seatable_api import Account
    username = 'xiongxxx@xxx.com'
    password = 'xxxxxxx'
    server_url = 'https://cloud.seatable.cn/'
    account = Account(username, password, server_url)
    account.auth()
    ```

## List of account objects

!!! abstract "List workspaces"

    Get all your workspaces and its Bases.

    ``` python
    account.list_workspaces()
    ```

!!! abstract "Add a base"

    Add a base to a Workspace.

    ``` python
    account.add_base(name, workspace_id=None)
    ```

    __Example__

    ``` python
    account.add_base('new-base', 35)
    ```

!!! abstract "Copy a base"

    Copy a base to a workspace.

    ``` python
    account.copy_base(src_workspace_id, base_name, dst_workspace_id)
    ```

    __Example__

    ``` python
    account.copy_base(35, 'img-file', 74)
    ```

!!! abstract "Get a base"

    Get a base object. Get the Base object named base_name that exists in the workspace whose id is workspace_id.

    ``` python
    account.get_base(workspace_id, base_name)
    ```

    __Example__

    ``` python
    base = account.get_base(35, 'new-base')
    ```
