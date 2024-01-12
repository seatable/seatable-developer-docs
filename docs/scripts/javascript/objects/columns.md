# Columns

## Get Columns

!!! question "getColumns"

    Get all the columns in the table, and return all the column objects in an array.

    ``` js
    base.getColumns(table: Object/String);
    ```

    __Examples__
    ``` js
    const table  = base.getTableByName('Table1');
    const columns = base.getColumns(table);

    column.forEach((column) => {
        output.text(column.name);
    })
    ```

    ``` js
    const columns = base.getColumns('Table1');
    ```

!!! question "listColumns"

    ````
    Get the columns by name of table and view, if view_name is not set, all columns in table will be returned

    ``` js
    base.listColumns(table_name: String, view_name: String);
    ```

    __Examples__
    ``` js
    const table_name  = 'Table1'
    const view_name = 'Default'
    const columns = base.listColumns(table_name, view_name);

    column.forEach((column) => {
        output.text(column.name);
    })
    ```

    ``` js
    const columns = base.listColumns('Table1');
    ```
    ````

!!! question "getShownColumns"

    Get all the displayed columns in a view, excluding the hidden columns in the view, and return an array.

    ``` js
    base.getShownColumns(table: Object/String, view: Object/String);
    ```

    __Examples__
    ``` js
    const table  = base.getTableByName('Table1');
    const view = base.getViewByName(table, 'view 1');
    const columns = base.getShownColumns(table, view);
    column.forEach((column) => {
        output.text(column.name);
    })
    ```

    ``` js
    const columns = base.getShownColumns('Table1', 'view 1');
    ```

!!! question "getColumnByName"

    Get the column object via its name.

    ``` js
    base.getColumnByName(table: Object/String, name: String);
    ```

    __Examples__
    ``` js
    const column = base.getColumnByName(table, 'Column name');
    output.text(column.name);
    ```

    ``` js
    const column = base.getColumnByName('Table1', 'Column name');
    ```

!!! question "getColumnsByType"

    Get all specific types of columns in the table.

    ``` js
    const columns = base.getColumnsByType(table: Object/String, type: String);
    ```

    __Examples__
    ``` js
    const table  = base.getTableByName('Table1');
    const columns = base.getColumnsByType(table, 'text');
    output.text(column.length);
    ```

    ``` js
    const columns = base.getColumnsByType('Table1', 'text');
    output.text(column.length);
    ```
