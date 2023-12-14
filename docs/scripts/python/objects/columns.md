# Column

Every table in a base contains columns. The following calls are available to interact with the columns of a table.

## List columns

!!! question "List columns"

    List all rows of the table/view.

    ``` python
    base.list_columns(table_name, view_name=None);
    ```

    __Example__

    ``` python
    base.list_columns('Table1', default)
    ```

## Insert column

!!! question "Insert column"

    Insert or append a column to a table.

    ``` python
    base.insert_column(table_name, column_name, column_type, column_key=None, column_data=None)
    ```

    __Examples__

    ``` python
    base.insert_column('Table1', 'New long text column', 'long text')
    ```

    ``` python
    from seatable_api.constants import ColumnTypes
    base.insert_column('Table1', 'Link', ColumnTypes.LINK, column_data={
        'table':'Table1',
        'other_table':'Test_User'
    })
    ```

## Rename column

!!! question "Rename column"

    Rename a column.

    ``` python
    base.rename_column(table_name, column_key, new_column_name)
    ```

    __Example__

    ``` python
    base.rename_column('Table1', 'kSiR', 'new column name')
    ```

## Freeze column

!!! question "Freeze column"

    Freeze a column.

    ``` python
    base.freeze_column(table_name, column_key, frozen)
    ```

    __Example__

    ``` python
    base.freeze_column('Table1', '0000', True)
    ```

## Move column

!!! question "Move column"

    Move column. In this example, the column with the key `loPx` will be moved to the right of the column `0000`.

    ``` python
    base.move_column(table_name, column_key, target_column_key)
    ```

    __Example__

    ``` python
    base.move_column('Table1', 'loPx', '0000')
    ```

## Modify column types

!!! question "Modify column type"

    Change the column type of an existing column

    ``` python
    base.modify_column_type(table_name, column_key, new_column_type)
    ```

    __Example__

    ``` python
    base.modify_column_type('Table1', 'nePI', 'checkbox')
    ```

## Add column options

!!! question "Add column options"

    Used by single-select or multiple-select type columns to add new options.

    ``` python
    add_column_options(self, table_name, column, options)
    ```

    __Example__

    ``` python
    base.add_column_options('Table1', 'My choices', [
        {"name": "ddd", "color": "#aaa", "textColor": "#000000"},
        {"name": "eee", "color": "#aaa", "textColor": "#000000"},
        {"name": "fff", "color": "#aaa", "textColor": "#000000"},
    ])
    ```

## Add column cascade settings

!!! question "Add column cascade settings"

    Used by single-select column, to add a limitation of child column options according to the option of parent column.

    ``` python
    add_column_cascade_settings(table_name, child_column, parent_column, cascade_settings)
    ```

    __Example__

    ``` python
    base.add_column_cascade_settings("Table1", "single-op-col-c", "single-op-col", {
        "aaa": ["aaa-1", "aaa-2"], # If “aaa” is selected by parent column, the available options of child column are "aaa-1 and aaa-2"
        "bbb": ["bbb-1", "bbb-2"],
        "ccc": ["ccc-1", "ccc-2"]
    })
    ```

## Delete column

!!! question "Delete column"

    Deletes a column from the table.

    ``` python
    base.delete_column(table_name, column_key)
    ```

    __Example__

    ``` python
    base.delete_column('Table1', 'bsKL')
    ```
