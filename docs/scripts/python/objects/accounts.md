# Accounts

The account object provides an interface to list workspaces, add/copy/delete bases, and obtain access rights to a base.

!!! info "Specific authentication required"

    Accessing the account object requires a specific authentication.

    ``` python
    from seatable_api import Account # (1)!
    username = 'xxx@email.com' # (2)!
    password = 'xxxxxxx'
    server_url = 'https://cloud.seatable.io/'
    account = Account(username, password, server_url)
    account.auth()
    ```

    1. Don't forget to import `Account` from `seatable_api`

    2. Always be vigilant when exposing your credentials in a script! Prefer as often as possible more secure solutions such as environment variables or \.venv\ files

## Manage workspaces

!!! abstract "list_workspaces"

    Get all your workspaces and its Bases.

    ``` python
    account.list_workspaces()
    ```
    __Output__ Dict with a single `workspace_list` key containing a list of every workspaces and for each a list of tables or shared tables of views

    __Example__

    === "Function call"
    
        ``` python
        import json
        from seatable_api import Account
        username = 'xxx@email.com'
        password = 'xxxxxxx'
        server_url = 'https://cloud.seatable.io/'
        account = Account(username, password, server_url)
        account.auth()
        workspaces = account.list_workspaces()
        print(json.dumps(workspaces, indent=' '))
        ```

    === "Output example"

        ``` json
        {
            "workspace_list": [
                {
                    "id": "",
                    "name": "starred", /* (1)! */
                    "type": "starred",
                    "table_list": []
                },
                {
                    "id": "",
                    "name": "shared",  /* (2)! */
                    "type": "shared",
                    "shared_table_list": [],
                    "shared_view_list": [
                        {
                            "id": 1416,
                            "dtable_name": "MBase",
                            "from_user": "b4980649.....b1311ab4ba2@auth.local",
                            "to_user": "cc7a1d0fcec......df5dcf5b65b99@auth.local",
                            "permission": "rw",
                            "table_id": "ji9k",
                            "view_id": "0000",
                            "shared_name": "Shared MBase",
                            "from_user_name": "Tony Stark",
                            "to_user_name": "Hulk",
                            "from_user_avatar": "",
                            "workspace_id": 34996,
                            "color": null,
                            "text_color": null,
                            "icon": null,
                            "share_id": 1416,
                            "share_type": "view-share"
                        }
                    ],
                    "share_folders": []
                },
                {
                    "id": 84254,
                    "name": "personal",  /* (3)! */
                    "type": "personal",
                    "table_list": [
                        {
                            "id": 198299,
                            "workspace_id": 84254,
                            "uuid": "0959ee9c-6b....8c-a751-c798431ab3ad",
                            "name": "AllColumnsBase",
                            "created_at": "2025-09-04T12:39:08+02:00",
                            "updated_at": "2025-09-25T11:31:48+02:00",
                            "color": null,
                            "text_color": null,
                            "icon": null,
                            "is_encrypted": false,
                            "in_storage": true,
                            "starred": false
                        },
                        {
                            "id": 200036,
                            "workspace_id": 84254,
                            "uuid": "30fd2a69-07.....e-85ee-be3230a87ea2",
                            "name": "Big Data",
                            "created_at": "2025-09-11T12:11:58+02:00",
                            "updated_at": "2025-09-23T11:09:09+02:00",
                            "color": null,
                            "text_color": null,
                            "icon": null,
                            "is_encrypted": false,
                            "in_storage": true,
                            "starred": false
                        },
                        {
                            "id": 202730,
                            "workspace_id": 84254,
                            "uuid": "98e53b22-80....d5-92ca-c44d783d9561",
                            "name": "Ledger",
                            "created_at": "2025-09-23T15:19:30+02:00",
                            "updated_at": "2025-09-23T17:06:48+02:00",
                            "color": "#E91E63",
                            "text_color": null,
                            "icon": "icon-dollar",
                            "is_encrypted": false,
                            "in_storage": true,
                            "starred": false
                        },
                        {
                            "id": 197691,
                            "workspace_id": 84254,
                            "uuid": "4b5ef925-c178-4000-89e2-941aa65cc747",
                            "name": "Test",
                            "created_at": "2025-09-03T09:03:57+02:00",
                            "updated_at": "2025-09-25T10:37:13+02:00",
                            "color": "#656463",
                            "text_color": null,
                            "icon": "icon-research",
                            "is_encrypted": false,
                            "in_storage": true,
                            "starred": false
                        }
                    ],
                    "folders": []
                },
                {
                    "id": 86760,
                    "name": "My group",
                    "type": "group",
                    "group_id": 10339,
                    "group_owner": "cc7a1d0fcec......df5dcf5b65b99@auth.local",
                    "is_admin": true,
                    "table_list": [
                        {
                            "id": 197108,
                            "workspace_id": 86760,
                            "uuid": "eec7ff7b-638......4cb-315489bca05e",
                            "name": "My grouped table",
                            "created_at": "2025-09-01T11:44:49+02:00",
                            "updated_at": "2025-09-01T11:44:49+02:00",
                            "color": null,
                            "text_color": null,
                            "icon": null,
                            "is_encrypted": false,
                            "in_storage": true,
                            "starred": false
                        }
                    ],
                    "group_shared_dtables": [],
                    "group_shared_views": [],
                    "folders": []
                }
            ]
        }
        ```

        1. "Favorites" section

        2. "Shared with me" section

        3. "My bases" section

## Manage bases

!!! abstract "get_base"

    Get the base named `base_name` in the workspace whose id is `workspace_id`. You'll be able to interact with this base using all the `base` methods presented in this manual. Please note that the base is authorized.

    ``` python
    account.get_base(workspace_id, base_name)
    ```

    __Output__ base object (throws an error if no workspace with id `workspace_id` or no base `base_name` exists, or if you encounter permission issue)

    __Example__

    ``` python
    from seatable_api import Account
    username = 'xxx@email.com'
    password = 'xxxxxxx'
    server_url = 'https://cloud.seatable.io/'
    account = Account(username, password, server_url)
    account.auth()
    base = account.get_base(35, 'new-base')
    print(base.get_metadata())
    ```

!!! abstract "add_base"

    Add a base named `base_name` to a Workspace. If no `workspace_id` is provided, the base will be created in the "My bases" section (workspace named "personal").

    ``` python
    account.add_base(base_name, workspace_id=None)
    ```

    __Output__ Dict containing the same base metadata as members of the `table_list` of the workspace metadata (throws an error if no workspace with id `workspace_id` exists or if a base named `base_name` already exists in the workspace)
    
    __Example__

    ``` python
    from seatable_api import Account
    username = 'xxx@email.com'
    password = 'xxxxxxx'
    server_url = 'https://cloud.seatable.io/'
    account = Account(username, password, server_url)
    account.auth()
    base_metadata = account.add_base('My New Base', 35)
    print(base_metadata)
    ```

!!! abstract "copy_base"

    Copy the base base_name from the workspace whose id is `src_workspace_id` to the workspace whose id is `dst_workspace_id`.

    ``` python
    account.copy_base(src_workspace_id, base_name, dst_workspace_id)
    ```

     __Output__ Dict containing the same base metadata as members of the `table_list` of the workspace metadata (throws an error if no workspace with id `workspace_id` exists or if a base named `base_name` already exists in the workspace) for the newly created base
    
    __Example__

    ``` python
    from seatable_api import Account
    username = 'xxx@email.com'
    password = 'xxxxxxx'
    server_url = 'https://cloud.seatable.io/'
    account = Account(username, password, server_url)
    account.auth()
    base_metadata = account.copy_base(35, 'My Base', 74)
    print(base_metadata)
    ```
