---
description: JavaScript API reference for managing columns — create, rename, resize, freeze, move, modify types, and configure select options.
---

# Columns

{%
    include-markdown "includes.md"
    start="<!--columnstructure-start-->"
    end="<!--columnstructure-end-->"
%}

## Get Column(s)

!!! abstract "getColumnByName"

    Get the column object of a table, specified by the column name.

    ```js
    base.getColumnByName(table, columnName);
    ```

    __Output__ Single column object (`undefined` if column doesn't exist)

    __Example__
    ```js
    const column = base.getColumnByName('Table1', 'Name');
    ```

!!! abstract "getColumns"

    Get all columns of a table.

    ```js
    base.getColumns(table);
    ```

    __Output__ Array of column objects

    __Example__
    ```js
    const columns = base.getColumns('Table1');
    columns.forEach((column) => {
        console.log(column.name);
    });
    ```

!!! abstract "listColumns"

    Get the columns of a table, optionally filtered by view. If no view is specified, all columns are returned.

    ```js
    base.listColumns(tableName, viewName);
    ```

    __Output__ Array of column objects

    __Example__
    ```js
    const columns = base.listColumns('Table1', 'Default View');
    ```

!!! abstract "getShownColumns :material-tag-outline:{ title='Scripting only' }"

    Get all visible columns of a table in a specific view (hidden columns are excluded). Only available in SeaTable scripts.

    ```js
    base.getShownColumns(table, view);
    ```

    __Output__ Array of column objects

    __Example__
    ```js
    const columns = base.getShownColumns('Table1', 'Default View');
    ```

!!! abstract "getColumnsByType"

    Get all columns of a specific type in a table. See the [API Reference](https://api.seatable.com/reference/models#supported-column-types) for supported column types.

    ```js
    base.getColumnsByType(table, type);
    ```

    __Output__ Array of column objects (empty array if no match)

    __Example__
    ```js
    const textColumns = base.getColumnsByType('Table1', 'text');
    ```

## Add Column

!!! abstract "insertColumn"

    Add a new column to a table.

    ```js
    base.insertColumn(tableName, columnName, columnType, columnKey='', columnData='');
    ```

    __Example__
    ```js
    import { ColumnTypes } from 'seatable-api';

    await base.insertColumn('Table1', 'Notes', ColumnTypes.TEXT);

    // Insert after a specific column
    await base.insertColumn('Table1', 'Notes', ColumnTypes.TEXT, '0000');

    // Create a link column
    await base.insertColumn('Table1', 'Link1', ColumnTypes.LINK, '', {
        'table': 'Table1',
        'other_table': 'Table2'
    });
    ```

## Rename Column

!!! abstract "renameColumn"

    Rename a column, identified by its column key.

    ```js
    base.renameColumn(tableName, columnKey, newColumnName);
    ```

    __Example__
    ```js
    await base.renameColumn('Table1', 'kSiR', 'New Name');
    ```

## Column Settings

!!! abstract "resizeColumn"

    ```js
    base.resizeColumn(tableName, columnKey, newColumnWidth);
    ```

    __Example__
    ```js
    await base.resizeColumn('Table1', 'asFV', 500);
    ```

!!! abstract "freezeColumn"

    ```js
    base.freezeColumn(tableName, columnKey, frozen);
    ```

    __Example__
    ```js
    await base.freezeColumn('Table1', '0000', true);
    ```

!!! abstract "moveColumn"

    Move a column to the right of the target column.

    ```js
    base.moveColumn(tableName, columnKey, targetColumnKey);
    ```

    __Example__
    ```js
    await base.moveColumn('Table1', 'loPx', '0000');
    ```

!!! abstract "modifyColumnType"

    Change the type of an existing column.

    ```js
    base.modifyColumnType(tableName, columnKey, newColumnType);
    ```

    __Example__
    ```js
    import { ColumnTypes } from 'seatable-api';
    await base.modifyColumnType('Table1', 'nePI', ColumnTypes.NUMBER);
    ```

!!! abstract "addColumnOptions"

    Add options to a single-select or multiple-select column.

    ```js
    base.addColumnOptions(tableName, columnName, options);
    ```

    __Example__
    ```js
    await base.addColumnOptions('Table1', 'Status', [
        {"name": "Done", "color": "#73d56e", "textColor": "#000000"},
        {"name": "Open", "color": "#ff8000", "textColor": "#ffffff"},
    ]);
    ```

!!! abstract "addColumnCascadeSettings"

    Add cascade settings to a single-select column, limiting child options based on the parent column's selection.

    ```js
    base.addColumnCascadeSettings(tableName, childColumn, parentColumn, cascadeSettings);
    ```

    __Example__
    ```js
    await base.addColumnCascadeSettings('Table1', 'Sub-Category', 'Category', {
        "Electronics": ["Phones", "Laptops"],
        "Furniture": ["Chairs", "Tables"]
    });
    ```

## Delete Column

!!! abstract "deleteColumn"

    Delete a column, identified by its column key.

    ```js
    base.deleteColumn(tableName, columnKey);
    ```

    __Example__
    ```js
    await base.deleteColumn('Table1', 'bsKL');
    ```
