# Views

You'll find below all the available methods to interact with the views of a SeaTable table.

{%
    include-markdown "includes.md"
    start="<!--viewstructure-start-->"
    end="<!--viewstructure-end-->"
%}

## Get view(s)

!!! abstract "get_view_by_name"

    Get a view of the table `table_name`, specified by its name `view_name`.

    ``` python
    base.get_view_by_name(table_name, view_name)
    ```
    __Output__ Single view dict (throws an error if no view called `view_name` exists or if no table named `table_name` exists)

    __Example__

    ``` python
    from seatable_api import Base, context

    base = Base(context.api_token, context.server_url)
    base.auth()
    view = base.get_view_by_name('Table1', 'Default View')
    print(view)
    ```

!!! abstract "list_views"

    Get all the views of the table named `table_name`.

    ``` python
    base.list_views(table_name)
    ```

    __Output__ Dict with a single `views` key containing a list of the table's views (throws an error if no table named `table_name` exists)

    __Example__
    
    ``` python
    from seatable_api import Base, context

    base = Base(context.api_token, context.server_url)
    base.auth()
    views = base.list_views('Table1')
    print(views)
    ```

## Add view

!!! abstract "add_view"

    Add a view named `view_name` to the table `table_name`.
    
    ``` python
    base.add_view(table_name, view_name)
    ```

    __Output__ Single view dict (throws an error if a view called `view_name` already exists or if no table named `table_name` exists)

    __Example__

    ``` python
    from seatable_api import Base, context

    base = Base(context.api_token, context.server_url)
    base.auth()
    view = base.add_view('Table1', 'New view')
    print(view)
    ```

## Rename view

!!! abstract "rename_view"

    Rename a view in the table `table_name` specified by its current name `view_name` and its new name `new_view_name`. Please ensure that no view named `new_view_name` already exists in the table `table_name`.

    ``` python
    base.rename_view(table_name, view_name, new_view_name)
    ```

    __Output__ Single view dict (throws an error if no view called `view_name` exists or if no table named `table_name` exists)

    __Example__

    ``` python
    from seatable_api import Base, context

    base = Base(context.api_token, context.server_url)
    base.auth()
    view = base.rename_view('Table1', 'MyView', 'NewView')
    print(view)
    ```

## Delete view

!!! abstract "delete_view"

    Delete a view in the table `table_name`, specified by its name `view_name`. **DO NOT** try to delete the last view or you might no longer be able to access your table!

    ``` python
    base.delete_view(table_name, view_name)
    ```

    __Output__ Dict containing a single `success` key with the result of the operation  (throws an error if no table named `table_name` exists). Be careful, `{'success':True}` will be returned even if no view named `view_name` exists!

    __Example__

    ``` python
    from seatable_api import Base, context

    base = Base(context.api_token, context.server_url)
    base.auth()
    print(base.delete_view('Table1', 'MyView'))
    ```
