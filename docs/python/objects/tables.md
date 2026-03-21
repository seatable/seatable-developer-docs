# Tables

You'll find below all the available methods to interact with the tables of a SeaTable base.

!!! tip "Examples assume authenticated base"

    All examples on this page assume that `base` has been initialized and authenticated as described on the [introduction](../index.md#authentication) page. For the structure of objects returned by these methods, see the [API model reference](https://api.seatable.com/reference/models).

## Retrieve table(s)

!!! info "Get current table"

    There is no specific method to get the current (selected) table as it is a property from the [context object](./context.md),
    so simply use `context.current_table`.

!!! abstract "list_tables"

    Get all tables of the current base.

    ```python
    base.list_tables()
    ```
    __Output__ List of table dicts

    __Example__
    ```python
    tables = base.list_tables()
    print(tables)
    ```

!!! abstract "get_table_by_name"

    Get a table object by its name.

    ```python
    base.get_table_by_name(table_name)
    ```
    __Output__ Single table dict (`None` if there is no table named `table_name`)
    
    __Example__
    ```python
    table = base.get_table_by_name('Table1')
    print(table)
    ```

## Add table

!!! abstract "add_table"

    Add a table named `table_name` into a base. The `columns` argument is an optional list of [column objects](https://api.seatable.com/reference/models).

    ```python
    base.add_table(table_name, lang='en', columns=[]) # (1)!
    ```

    1. `lang` (optional): can be `en` (default) for English or `zh-cn` for Chinese and will determine the name of the first `Name` column (if no `columns` where specified)
        `columns` (optional): list of [column objects](https://api.seatable.com/reference/models) describing the columns of the new table.

    __Output__ Single table dict (throws an error if a table named `table_name` already exists)

    __Example__
    ```python
    new_table = base.add_table('Investigation', lang='zh-cn')
    print(new_table)
    ```

    ```python
    columns=[
      {
        "column_type" : "text", 
        "column_name": "name"
      }, 
      {
      "column_type": "number",
      "column_name": "age"
      }
    ]

    base.add_table("ScriptTest", lang='en', columns=columns)
    ```

## Rename table

!!! abstract "rename_table"

    Rename an existing table named `table_name` to `new_table_name`.

    ```python
    base.rename_table(table_name, new_table_name)
    ```
    __Output__ Dict containing a single `success` key with the result of the operation  (throws an error if no table named `table_name` exists)

    __Example__
    === "Function call"
        ```python
        print(base.rename_table('Table1', 'Table11'))
        ```
    === "Output"
        ```json
        {'success': True}
        ```

## Delete table

!!! abstract "delete_table"

    Delete a table named `tableName` from the base. By the way, the table can be [restored from the logs](https://seatable.com/help/eine-geloeschte-tabelle-wiederherstellen/). Deleting the last table is not possible.

    ```python
    base.delete_table(table_name)
    ```

    __Output__ Dict containing a single `success` key with the result of the operation  (throws an error if no table named `table_name` exists or if you try to delete the last table)

    __Example__
    ```python
    delete_table_success = base.delete_table('Table1')
    print(delete_table_success)
    ```
