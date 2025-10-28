# Tables

You'll find below all the available methods to interact with the tables of a SeaTable base.

{%
    include-markdown "includes.md"
    start="<!--tablestructure-start-->"
    end="<!--tablestructure-end-->"
%}

You can have a look at the specific [view](./views.md#global-structure), [column](./columns.md#global-structure) or [row](./rows.md#global-structure) structure on the corresponding pages.

## Retrieve table(s)

!!! info "Get current table"

    There is no specific method to get the current (selected) table as it is a property from the [context object](./context.md),
    so simply use `context.current_table`.

!!! abstract "list_tables"

    Get all tables of the current base.

    ``` python
    base.list_tables()
    ```
    __ Output__ List of table dicts

    __Example__
    ``` python
    from seatable_api import Base, context

    base = Base(context.api_token, context.server_url)
    base.auth()
    tables = base.list_tables()
    print(tables)
    ```

!!! abstract "get_table_by_name"

    Get a table object by its name.

    ``` python
    base.get_table_by_name(table_name)
    ```
    __Output__ Single table dict (`None` if there is no table named `table_name`)
    
    __Example__
    ``` python
    from seatable_api import Base, context

    base = Base(context.api_token, context.server_url)
    base.auth()
    table = base.get_table_by_name('Table1')
    print(table)
    ```

## Add table

!!! abstract "add_table"

    Add a table named `table_name` into a base. The `columns` argument is an optional list of [column objects](./columns.md#global-structure).

    ``` python
    base.add_table(table_name, lang='en', columns=[]) # (1)!
    ```

    1. `lang` (optional): can be `en` (default) for English or `zh-cn` for Chinese and will determine the name of the first `Name` column (if no `columns` where specified)
        `columns` (optional): list of [column objects](./columns.md#global-structure) describing the columns of the new table.

    __Output__ Single table dict (throws an error if a table named `table_name` already exists)

    __Example__
    ``` python
    from seatable_api import Base, context

    base = Base(context.api_token, context.server_url)
    base.auth()
    new_table = base.add_table('Investigation', lang='zh-cn')
    print(new_table)
    ```

    ``` python
    from seatable_api import Base, context

    base = Base(context.api_token, context.server_url)
    base.auth()

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

    ``` python
    base.rename_table(table_name, new_table_name)
    ```
    __Output__ Dict containing a single `success` key with the result of the operation  (throws an error if no table named `table_name` exists)

    __Example__
    === "Function call"
        ``` python
        from seatable_api import Base, context

        base = Base(context.api_token, context.server_url)
        base.auth()
        print(base.rename_table('Table1', 'Table11'))
        ```
    === "Output"
        ```python
        {'success': True}
        ```

## Delete table

!!! abstract "delete_table"

    Delete a table named `tableName` from the base. By the way, the table can be [restored from the logs](https://seatable.com/help/eine-geloeschte-tabelle-wiederherstellen/). Deleting the last table is not possible.

    ``` python
    base.delete_table(table_name)
    ```

    __Output__ Dict containing a single `success` key with the result of the operation  (throws an error if no table named `table_name` exists or if you try to delete the last table)

    __Example__
    ``` python
    from seatable_api import Base, context

    base = Base(context.api_token, context.server_url)
    base.auth()
    delete_table_success = print(base.delete_table('Table1'))
    print(delete_table_success)
    ```
