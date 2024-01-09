# Views

Every table in a base contains views. The following calls are available to interact with the views of a table.

## List views

!!! question "List views"


    ``` python
    base.list_views(table_name)
    ```

    __Example__
    
    ``` python
    base.list_views('Table1')
    ```

!!! question "Get view by name"

    ``` python
    base.get_view_by_name(table_name, view_name)
    ```

    __Example__

    ``` python
    base.get_view_by_name('Table1', 'MyView')
    ```

## Add view

!!! question "Add view"

    
    ``` python
    base.add_view(table_name, view_name)
    ```

    __Examples__

    ``` python
    base.add_view('Table1', 'New view')
    ```

## Rename view

!!! question "Rename view"


    ``` python
    base.rename_view(table_name, view_name, new_view_name)
    ```

    __Example__

    ``` python
    base.rename_view('Table1', 'MyView', 'NewView')
    ```

## Delete view

!!! question "Delete view"


    ``` python
    base.delete_view(table_name, view_name)
    ```

    __Example__

    ``` python
    base.delete_view('Table1', 'MyView')
    ```
