# Columns

You'll find below all the available methods to interact with the columns of a SeaTable table.

{%
    include-markdown "includes.md"
    start="<!--columnstructure-start-->"
    end="<!--columnstructure-end-->"
%}

## Get Column(s)

!!! abstract "getColumnByName"

    Get the column object of a particular `table`, specified by the column `name`.

    ``` js
    base.getColumnByName(table: Object/String/* (1)! */, name: String);
    ```

    1. `table`: either a table object or the table name

    __Output__ Single column object (`undefined` if column `name` doesn't exist)

    __Example__
    ``` js
    const table  = base.getTableByName('Table1');
    const column = base.getColumnByName(table, 'Column name');
    output.text(column.name);
    ```

    ``` js
    const column = base.getColumnByName('Table1', 'Column name');
    ```

!!! abstract "getColumns"

    Get all the columns of a specific `table`.

    ``` js
    base.getColumns(table: Object/String/* (1)! */);
    ```

    1. `table`: either a table object or the table name

    __Output__ Array of column objects (throws an error if `table` doesn't exist)

    __Example__
    ``` js
    const table  = base.getTableByName('Table1');
    const columns = base.getColumns(table);

    columns.forEach((column) => {
        output.text(column.name);
    })
    ```

    ``` js
    const columns = base.getColumns('Table1');
    ```

!!! abstract "listColumns"

    Get the columns of a table (specified by its name `tableName`), optionally from a specific view (specified by its name `viewName`). If `viewName` is not set, all columns of the table will be returned (equivalent, in this case, to `base.getColumns`).

    ``` js
    base.listColumns(tableName: String, viewName: String);
    ```

    __Output__ Array of column objects (throws an error if `table` doesn't exist)

    __Example__
    ``` js
    const tableName  = 'Table1'
    const viewName = 'Default View'
    const columns = base.listColumns(tableName, viewName);

    columns.forEach((column) => {
        output.text(column.name);
    })
    ```

    ``` js
    const columns = base.listColumns('Table1');
    ```

!!! abstract "getShownColumns"

    Get all the columns of a `table` displayed in a specific `view` (hidden columns are not returned).

    ``` js
    base.getShownColumns(table: Object/String, view: Object/String/* (1)! */);
    ```

    1. `table`: either a table object or the table name
    
        `view` (required): either a view object or the view name

    __Output__ Array of column objects (throws an error if `table` or `view` doesn't exist)

    __Example__
    ``` js
    const table  = base.getTableByName('Table1');
    const view = base.getViewByName(table, 'Default View');
    const columns = base.getShownColumns(table, view);
    columns.forEach((column) => {
        output.text(column.name);
    })
    ```

    ``` js
    const columns = base.getShownColumns('Table1', 'Default View');
    ```

!!! abstract "getColumnsByType"

    Get all the columns of a specific `type` in a `table`.

    ``` js
    base.getColumnsByType(table: Object/String, type: String /* (1)! */);
    ```

    1. `table`: either a table object or the table name
    
        `type` (required): the type of the column (see the [API Reference](https://api.seatable.com/reference/models#supported-column-types) for supported types)

    __Output__ Array of column objects (empty array if no corresponding columns or wrong `type`)

    __Example__
    ``` js
    const table  = base.getTableByName('Table1');
    const columns = base.getColumnsByType(table, 'text');
    output.text(columns.length);
    ```

    ``` js
    const columns = base.getColumnsByType('Table1', 'text');
    output.text(columns.length);
    ```
