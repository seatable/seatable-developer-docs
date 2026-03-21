---
description: JavaScript API reference for row operations — query, append, insert, batch update, delete, and filter rows in SeaTable bases.
---

# Rows

{%
    include-markdown "includes.md"
    start="<!--rowstructure-start-->"
    end="<!--rowstructure-end-->"
%}

## Get Row(s)

!!! abstract "getRow"

    Get a single row by its ID.

    ```js
    base.getRow(table, rowId);
    ```

    __Output__ Single row object

    __Example__
    ```js
    const row = base.getRow('Table1', 'M_lSEOYYTeuKTaHCEOL7nw');
    ```

!!! abstract "getRows"

    Get all rows displayed in a view.

    ```js
    base.getRows(table, view);
    ```

    __Output__ Array of row objects

    __Example__
    ```js
    const rows = base.getRows('Table1', 'Default View');
    ```

!!! abstract "listRows"

    Get rows with optional sorting and pagination. Particularly useful for large tables.

    ```js
    base.listRows(tableName, viewName='', orderBy='', desc='', start='', limit='');
    ```

    __Output__ Array of row objects

    __Example__
    ```js
    // Simple
    const rows = await base.listRows('Table1');

    // With pagination and sorting
    const rows = await base.listRows('Table1', 'Default View', 'Name', true, 0, 100);
    ```

!!! abstract "getGroupedRows :material-tag-outline:{ title='Scripting only' }"

    Get rows grouped according to the view's grouping settings. Only available in SeaTable scripts.

    ```js
    base.getGroupedRows(table, view);
    ```

    __Output__ Array of group objects, each containing a `rows` array

    __Example__
    ```js
    const table = base.getTableByName('Table1');
    const view = base.getViewByName(table, 'Grouped View');
    const groups = base.getGroupedRows(table, view);
    ```

!!! abstract "query"

    Use SQL to query a base. Most SQL syntax is supported -- see the [SQL Reference](../sql/index.md) for details.

    ```js
    await base.query(sql);
    ```

    !!! info "Backticks for special names"
        Escape table or column names that contain spaces or special characters with backticks: `` SELECT * FROM `My Table` ``

    __Output__ Array of row objects

    __Example__
    ```js
    const data = await base.query('SELECT name, price FROM Bill WHERE year = 2021');
    ```

    ```js
    // Aggregation
    const data = await base.query('SELECT name, SUM(price) FROM Bill GROUP BY name');
    ```

!!! abstract "filter :material-tag-outline:{ title='Scripting only' }"

    Filter rows using a filter expression. Returns a QuerySet with chainable methods. Only available in SeaTable scripts.

    ```js
    base.filter(tableName, viewName, filterExpression);
    ```

    __Output__ QuerySet object

    __Example__
    ```js
    // Get all rows where status is "Done"
    const querySet = base.filter('Table1', 'Default View', 'Status = "Done"');
    const rows = querySet.all();
    const count = querySet.count();
    const first = querySet.first();
    ```

    QuerySet methods: `.all()`, `.count()`, `.first()`, `.last()`, `.get(filter)`, `.filter(filter)`, `.delete()`, `.update(rowData)`

## Add Row(s)

!!! abstract "appendRow"

    Append a new row to the end of a table.

    ```js
    base.appendRow(tableName, rowData, applyDefault=false);
    ```

    Set `applyDefault` to `true` to use default column values for unspecified columns.

    __Example__
    ```js
    base.appendRow('Table1', {
        'Name': 'New entry',
        'Status': 'Open'
    });
    ```

!!! abstract "insertRow"

    Insert a row after a specific anchor row.

    ```js
    base.insertRow(tableName, rowData, anchorRowId, applyDefault=false);
    ```

    __Example__
    ```js
    await base.insertRow('Table1', {'Name': 'Inserted row'}, 'U_eTV7mDSmSd-K2P535Wzw');
    ```

!!! abstract "batchAppendRows"

    Append multiple rows at once. More efficient than calling `appendRow` in a loop.

    ```js
    base.batchAppendRows(tableName, rowsData, applyDefault=false);
    ```

    __Example__
    ```js
    await base.batchAppendRows('Table1', [
        {'Name': 'Row 1', 'Status': 'Open'},
        {'Name': 'Row 2', 'Status': 'Done'},
        {'Name': 'Row 3', 'Status': 'Open'}
    ]);
    ```

## Update Row(s)

!!! abstract "updateRow"

    Update a single row identified by its row ID.

    ```js
    base.updateRow(tableName, rowId, rowData);
    ```

    In scripting context, you can also pass a row object instead of a row ID.

    __Example__
    ```js
    base.updateRow('Table1', 'U_eTV7mDSmSd-K2P535Wzw', {
        'Status': 'Done'
    });
    ```

!!! abstract "modifyRows :material-tag-outline:{ title='Scripting only' }"

    Update multiple rows at once in scripting context. Pass two arrays: the rows to update and the corresponding update data.

    ```js
    base.modifyRows(table, rows, updatedRows);
    ```

    __Example__
    ```js
    const table = base.getTableByName('Table1');
    const rows = base.getRows(table, base.getViewByName(table, 'Default View'));
    const selectedRows = rows.filter(row => row['Status'] === 'Open');
    const updates = selectedRows.map(() => ({'Status': 'Archived'}));
    base.modifyRows(table, selectedRows, updates);
    ```

!!! abstract "batchUpdateRows"

    Update multiple rows at once. Each entry specifies a row ID and the data to update.

    ```js
    base.batchUpdateRows(tableName, rowsData);
    ```

    __Example__
    ```js
    await base.batchUpdateRows('Table1', [
        {"row_id": "fMmCFyoxT4GN5Y2Powbl0Q", "row": {"Name": "Updated 1"}},
        {"row_id": "cF5JTE99Tae-VVx0BGT-3A", "row": {"Name": "Updated 2"}}
    ]);
    ```

## Delete Row(s)

!!! abstract "deleteRow"

    Delete a single row by its ID.

    ```js
    base.deleteRow(tableName, rowId);
    ```

    __Example__
    ```js
    base.deleteRow('Table1', 'U_eTV7mDSmSd-K2P535Wzw');
    ```

!!! abstract "batchDeleteRows"

    Delete multiple rows at once.

    ```js
    base.batchDeleteRows(tableName, rowIds);
    ```

    __Example__
    ```js
    await base.batchDeleteRows('Table1', [
        'fMmCFyoxT4GN5Y2Powbl0Q',
        'cF5JTE99Tae-VVx0BGT-3A'
    ]);
    ```
