# Users

!!! tip "Examples assume authenticated base"

    All examples on this page assume that `base` has been initialized and authenticated as described on the [introduction](../index.md#authentication) page.

## Get user info

!!! abstract "get_user_info"

    Returns the name of the user and their ID. The username you have to provide is a unique identifier ending with `@auth.local`. This is **neither** the email address of the user **nor** their name.

    ``` python
    base.get_user_info(username)
    ```python

    __Output__ Dict containing `id_in_org` and `name` keys

    __Example__

    ``` python
    user_info = base.get_user_info("aea9e807bcfd4f3481d60294df74f6ee@auth.local")
    print(user_info)
    ```

## Get related users

!!! abstract "get_related_users"

    Get a list of users related to the current base (collaborators who have access).

    ``` python
    base.get_related_users()
    ```python

    __Output__ List of user dicts

    __Example__

    ``` python
    users = base.get_related_users()
    for user in users:
        print(user)
    ```
