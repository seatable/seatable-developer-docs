# Columns

You'll find below all the available methods to interact with the columns of a SeaTable table.

{%
    include-markdown "includes.md"
    start="<!--columnstructure-start-->"
    end="<!--columnstructure-end-->"
%}

## ColumnTypes constants

!!! info "ColumnTypes"

    When you want to insert/add a column or change a column type, you will need to use these `ColumnTypes`.

    ```python
    from seatable_api.constants import ColumnTypes # (1)!

    ColumnTypes.NUMBER              # number
    ColumnTypes.TEXT                # text
    ColumnTypes.LONG_TEXT           # long text
    ColumnTypes.CHECKBOX            # checkbox
    ColumnTypes.DATE                # date & time
    ColumnTypes.SINGLE_SELECT       # single select
    ColumnTypes.MULTIPLE_SELECT     # multiple select
    ColumnTypes.IMAGE               # image
    ColumnTypes.FILE                # file
    ColumnTypes.COLLABORATOR        # collaborator
    ColumnTypes.LINK                # link to other records
    ColumnTypes.FORMULA             # formula
    ColumnTypes.CREATOR             # creator
    ColumnTypes.CTIME               # create time
    ColumnTypes.LAST_MODIFIER       # last modifier
    ColumnTypes.MTIME               # modify time
    ColumnTypes.GEOLOCATION         # geolocation
    ColumnTypes.AUTO_NUMBER         # auto munber
    ColumnTypes.URL                 # URL
    ```

    1. Don't forget this particular import to use `ColumnTypes`!

## Get Column(s)

!!! abstract "get_column_by_name"

    Get the column of the table `table_name`, given the column name `column_name`.

    ``` python
    base.get_column_by_name(table_name, column_name)
    ```

    __Output__ Single column dict (`None` if no column named `column_name` exists, throws an error if no table named `table_name` exists)

    __Example__
        
    ``` python
    from seatable_api import Base, context

    base = Base(context.api_token, context.server_url)
    base.auth()
    column = base.get_column_by_name('Table1', 'Name')
    print(column)
    ```

!!! abstract "list_columns"

    Get the columns of a table (specified by its name `table_name`), optionally from a specific view (specified by its name `view_name`).

    ``` python
    base.list_columns(table_name, view_name=None)
    ```

    __Output__ List of column dicts (throws an error if no table named `table_name` exists or if no view named `view_name` exists)

    __Example__
        
    ``` python
    from seatable_api import Base, context

    base = Base(context.api_token, context.server_url)
    base.auth()
    columns = base.list_columns('Table1', 'Default View')
    print(columns)
    ```

!!! abstract "get_columns_by_type"

    Get all the columns of a specific `column_type` in the table `table_name`. See the [ColumnTypes constants](#columntypes-constants) above or the [API Reference](https://api.seatable.com/reference/models#supported-column-types) for more information about supported column types.
    
    ``` python
    base.get_columns_by_type(table_name, column_type)
    ```
    
    __Output__ List of column dicts (eventually empty; throws an error if no table named `table_name` exists or if `column_type` is not a valid `ColumnTypes` member)

    __Example__
    
    ``` python
    from seatable_api import Base, context
    from seatable_api.constants import ColumnTypes

    base = Base(context.api_token, context.server_url)
    base.auth()
    columns = base.get_columns_by_type('Table1', ColumnTypes.TEXT)
    print(columns)
    ```

## Insert column

!!! abstract "insert_column"

    Insert (inside the table) or append (at the end of the table) a column named `column_name` to the table `table_name`.

    ``` python
    base.insert_column(table_name, column_name, column_type, column_key=None, column_data=None) # (1)!
    ```

    1. `column_type`: See the [ColumnTypes constants](#columntypes-constants) above or the [API Reference](https://api.seatable.com/reference/models#supported-column-types) for more information about supported column types

        `column_key` (optional): argument specifying the key of the *anchor* column for the insertion (the newly created column will appear just to the right of the *anchor* column)

        `column_data` (optional): For some particular `ColumnTypes`, specific column data may be provided in the `column_data` dict. See the [column data](#column-data) above for more information.

    __Output__ Single column dict (throws an error if no table named `table_name` exists, if a column named `column_name` already exists or if `column_type` is not a valid `ColumnTypes` member)

    __Example__
    
    ``` python
    from seatable_api.constants import ColumnTypes
    from seatable_api import Base, context

    base = Base(context.api_token, context.server_url)
    base.auth()
    base.insert_column('Table1', 'New long text column', ColumnTypes.LONG_TEXT)
    ```

    ``` python
    from seatable_api.constants import ColumnTypes
    from seatable_api import Base, context

    base = Base(context.api_token, context.server_url)
    base.auth()
    base.insert_column('Table1', 'Link', ColumnTypes.LINK, column_data={
        'table':'Table1',
        'other_table':'Test_User'
    })
    ```

## Rename column

!!! abstract "rename_column"

    Rename the column in the table `table_name` whose key is `column_key`  with the new name `new_column_name`. Please ensure that you choose a `new_column_name` that doesn't already exists in your table `table_name`.

    ``` python
    base.rename_column(table_name, column_key, new_column_name)
    ```

    __Output__ Single column dict (throws an error if no table named `table_name` exists or if no column with the key `column_key` exists)

    __Example__
    
    ``` python
    from seatable_api import Base, context

    base = Base(context.api_token, context.server_url)
    base.auth()
    base.rename_column('Table1', '0000', 'new column name') # (1)!
    ```

    1. `0000` is always the key of the first column in each table

    ``` python
    from seatable_api import Base, context

    base = Base(context.api_token, context.server_url)
    base.auth()
    column_to_rename = base.get_column_by_name('Table1', 'My Column')
    base.rename_column('Table1', column_to_rename['key'], 'new column name') # (1)!
    ```

    1. Accessing the `key` value of a column you just retrieved (for example with `base.get_column_by_name`), you don't have to explicitly know its `column_key`

## (Un)freeze column

!!! abstract "(Un)freeze_column"

    Freeze ([fix](https://seatable.com/help/adjust-frozen-columns-seatable/)) or unfreeze the column of table `table_name` whose key is `column_key`. 
    
    !!! warning "(Un)freezing a group of columns"
        Please note that this method acts on a single column: to freeze the n-first left columns, please run it **for each column!**

    ``` python
    base.freeze_column(table_name, column_key, frozen) # (1)!
    ```

    1. `column_key`: the key of the column you want to (un)freeze

        `frozen`: `True` to freeze, `False` to unfreeze

    __Output__ Single column dict (throws an error if no table named `table_name` exists or if no column with the key `column_key` exists)

    __Example__
    
    ``` python
    from seatable_api import Base, context

    base = Base(context.api_token, context.server_url)
    base.auth()
    base.freeze_column('Table1', '0000', True)
    ```

## Move column

!!! abstract "move_column"

    Move the column of table `table_name` whose key is `column_key`.

    ``` python
    base.move_column(table_name, column_key, target_column_key) # (1)!
    ```

    1. `column_key`: the key of the column you want to move

        `target_column_key`: the key of the *anchor* column for the move (the column whose key is `column_key` will be moved just to the right of the *anchor* column)

    __Output__ Single column dict (throws an error if no table named `table_name` exists or if no column with the key `column_key` or `target_column_key` exists)
    
    __Example__
    
    ``` python
    from seatable_api import Base, context

    base = Base(context.api_token, context.server_url)
    base.auth()
    base.move_column('Table1', 'loPx', '0000') # (1)!
    ```

    1. In this example, the column with the key `loPx` will be moved to the right of the column `0000`

## Modify column type

!!! abstract "modify_column_type"

    Change the column type of an existing column of table `table_name` whose key is `column_key`.

    !!! warning "Don't change column type to ColumnTypes.LINK"
        This method doesn't allow to pass column data for the moment. Trying to change the column type to `ColumnTypes.LINK` will then lead to a "broken" column (you won't be able to edit the column's settings) as column data is mandatory for link-type columns.

    ``` python
    base.modify_column_type(table_name, column_key, new_column_type) # (1)!
    ```

    1. `column_key` (optional): the key of the column you want to modify the type

        `new_column_type`: See the [ColumnTypes constants](#columntypes-constants) above or the [API Reference](https://api.seatable.com/reference/models#supported-column-types) for more information about supported column types

    __Output__ Single column dict (throws an error if no table named `table_name` exists, if no column with the key `column_key` exists or if `new_column_type` is not a valid `ColumnTypes` member)

    __Example__
 
    ``` python
    from seatable_api.constants import ColumnTypes
    from seatable_api import Base, context

    base = Base(context.api_token, context.server_url)
    base.auth()
    base.modify_column_type('Table1', 'nePI', ColumnTypes.CHECKBOX)
    ```

## Delete column

!!! abstract "delete_column"

    Delete the column whose key is `column_key` in the table `table_name`. You cannot delete the first column as explained [here](https://seatable.com/help/warum-kann-ich-die-erste-spalte-meiner-tabelle-nicht-loeschen/).

    ``` python
    base.delete_column(table_name, column_key)
    ```

    __Output__ Dict containing a single `success` key with the result of the operation  (throws an error if no table named `table_name` exists, if no column with the key `column_key` exists or if you try to delete the first column)

    __Example__
    
    ``` python
    from seatable_api import Base, context

    base = Base(context.api_token, context.server_url)
    base.auth()
    base.delete_column('Table1', 'bsKL')
    ```

## Single- and/or multiple-select columns specific methods

### Add column options

!!! abstract "add_column_options"

    Used by both "single select" or "multiple select"-type columns to add new options to the column `column_name` of the table `table_name`.

    ``` python
    base.add_column_options(table_name, column_name, options) # (1)!
    ```

    1. `options`: list of option dict containing the following keys:

        - `name`: displayed text of the option

        - `color`: background color of the option (hex code)

        - `textColor`: text color of the option (hex code)

    __Output__ Dict containing a single `success` key with the result of the operation  (throws an error if no table named `table_name` exists, if no column named `column_name` exists or if `options` is invalid)
    
    __Example__
    
    ``` python
    from seatable_api import Base, context

    base = Base(context.api_token, context.server_url)
    base.auth()
    base.add_column_options('Table1', 'My choices', [
        {"name": "ddd", "color": "#aaa", "textColor": "#000000"},
        {"name": "eee", "color": "#aaa", "textColor": "#000000"},
        {"name": "fff", "color": "#aaa", "textColor": "#000000"},
    ])
    ```

### Add column cascade settings

!!! abstract "add_column_cascade_settings"

    Used by "single select"-type column, to condition the available options (see cascading in the [user manual](https://seatable.com/help/die-einfachauswahl-spalte/#cascading-a-single-select-column-search) or in the [API Reference](https://api.seatable.com/reference/updatecolumncascade-1)) of a child column `child_column` based on the options of a parent column `parent_column`.

    ``` python
    base.add_column_cascade_settings(table_name, child_column, parent_column, cascade_settings) # (1)!
    ```

    1. `child_column`: name of the column you want to condition the available options for

        `parent_column`: name of the parent column whose options will be used to condition the available options of the child column

        `cascade_settings`: cascade dict using the following structure:

        - each key is the `name` of an option from the parent column

        - each corresponding value is a list of the names of every allowed options from the child column

    __Output__ Dict containing a single `success` key with the result of the operation  (throws an error if no table named `table_name` exists, if no column named `child_column` or `parent_column` exists or if `cascade_settings` is invalid)
    
    __Example__
    
    ``` python
    from seatable_api import Base, context

    base = Base(context.api_token, context.server_url)
    base.auth()
    base.add_column_cascade_settings("Table1", "Child", "Parent", {
        "aaa": ["aaa-1", "aaa-2"], # (1)!
        "bbb": ["bbb-1", "bbb-2"],
        "ccc": ["ccc-1", "ccc-2"]
    })
    ```

    1. If `aaa` is selected in the parent column, the available options for the child column will be `aaa-1` and `aaa-2`
