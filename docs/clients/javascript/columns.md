# Columns

Every table in a base contains columns. The following calls are available to interact with the columns of a table.

## Get Columns

!!! question "listColumns"

    ```js
    base.listColumns(table_name, (view_name = ""));
    ```

    **Example**

    ```js
    const columns1 = await base.listColumns("Table1");
    const columns2 = await base.listColumns("Table1", (view_name = "default"));
    ```

!!! question "getColumnByName"

    ``` js
    base.getColumnByName(table_name, column_name);
    ```

    __Example__
    ``` js
    const col = await base.getColumnsByName('Table1', 'Name');
    ```

!!! question "getColumnsByType"

    ``` js
    base.getColumnsByType(table_name, col_type);
    ```

    __Example__
    ``` js
    const cols = await base.getColumnsByType('Table1', 'number')
    ```

## Add Column

!!! question "insertColumn"

    ``` js
    base.insertColumn(table_name, column_name, column_type, column_key='', column_data='')
    ```

    __Example__
    ``` js
    import { ColumnTypes } from 'seatable-api';
    await base.insertColumn('Table1', 'seatable-api', ColumnTypes.TEXT)
    await base.insertColumn('Table1', 'seatable-api', ColumnTypes.TEXT, '0000')
    await base.insertColumn('Table1', 'Link1', ColumnTypes.LINK, column_data={
            'table':'Table1',
            'other_table':'Test_User'
        })
    ```

## Rename Column

!!! question "renameColumn"

    ``` js
    base.renameColumn(table_name, column_key, new_column_name)
    ```

    __Example__
    ``` js
    await base.renameColumn('Table1', 'kSiR', 'new-seatable-api')
    ```

## Column Settings

!!! question "resizeColumn"

    ``` js
    base.resizeColumn(table_name, column_key, new_column_width)
    ```

    __Example__
    ``` js
    await base.resizeColumn('Table1', 'asFV', 500)
    ```

!!! question "freezeColumn"

    ``` js
    base.freezeColumn(table_name, column_key, frozen)
    ```

    __Example__
    ``` js
    await base.freezeColumn('Table1', '0000', true)
    ```

!!! question "moveColumn"

    ``` js
    base.moveColumn(table_name, column_key, target_column_key)
    ```

    __Example__
    In this example, the 'loPx' column will be moved to the right of the '0000' column
    ``` js
    await base.moveColumn('Table1', 'loPx', '0000')
    ```

!!! question "modifyColumnType"

    ``` js
    base.modifyColumnType(table_name, column_key, new_column_type)
    ```

    __Example__
    ``` js
    import { ColumnTypes } from 'seatable-api';
    await base.modifyColumnType('Table1', 'nePI', ColumnTypes.NUMBER)
    ```

!!! question "addColumnOptions"

    Used by "single select" or "multiple select"-type columns
    ``` js
    base.addColumnOptions(table_name, column, options)
    ```

    __Example__
    ``` js
    await base.addColumnOptions('Table1', 'My choices', [
            {"name": "ddd", "color": "#aaa", "textColor": "#000000"},
            {"name": "eee", "color": "#aaa", "textColor": "#000000"},
            {"name": "fff", "color": "#aaa", "textColor": "#000000"},
    ])
    ```

!!! question "addColumnCascadeSettings"

    Used by "single select"-type column, to add a limitation of child column options according to the option of parent column
    ``` js
    base.addColumnCascadeSettings(table_name, child_column, parent_column, cascade_settings)
    ```

    __Example__
    ``` js
    await base.addColumnCascadeSettings("Table1", "single-op-col-c", "single-op-col", {
    "aaa": ["aaa-1", "aaa-2"], # If “aaa” is selected by parent column, the available options of child column are "aaa-1 and aaa-2"
    "bbb": ["bbb-1", "bbb-2"],
    "ccc": ["ccc-1", "ccc-2"]
    })
    ```

## Delete Column

!!! question "deleteColumn"

    ``` js
    base.deleteColumn(table_name, column_key)
    ```

    __Example__
    ``` js
    await base.deleteColumn('Table1', 'bsKL')
    ```
