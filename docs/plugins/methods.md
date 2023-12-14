# Methods

This is a list of all available objects and methods in SeaTable you can use in the plugin development.

For a more detailed description of the used parameters, refer to the data model at the [SeaTable API Reference](https://api.seatable.io/reference/models).

## Common

Base represents a table in SeaTable. The `base` object provide a way to read, manipulate and output data in/from your base. The following methods are available.

### Users

??? question "getRelatedUsers"

    Get other users associated with the current base (collaborators of the table, the shared person of the table, etc.)

    ``` js
    dtable.getRelatedUsers()
    ```

    __Example__

    ```js
    const collaborators = dtable.getRelatedUsers();
    ```

??? question "getCollaboratorsName"

    Get a list of names of collaborators

    ``` js
    dtable.getCollaboratorsName(collaborators, value)
    ```
    Arguments

    * collaborators: collaborator list in this base
    * value: email list of collaborators

    __Example__

    ``` js
    const collaborators = dtable.getRelatedUsers();
    const value = ['abc@seafile.com', 'shun@seafile.com'];
    const name = dtable.getCollaboratorsName(collaborators, value); // 'abc, shun'
    ```

### Views

??? question "getViewRowsColor"

    Get the color attributes of the row data in the view

    ``` js
    dtable.getViewRowsColor(rows, view, table)
    ```

    __Arguments__

    * rows: the rows of the color attribute
    * view: view object
    * table: table object

    __Example__

    ``` js
    const tableName = 'tableName';
    const viewName = 'viewName';
    const table = dtable.getTableByName(tableName);
    const view = dtable.getViewByName(table, viewName);
    const rows = dtable.getViewRows(view, table);
    const rowsColor = dtable.getViewRowsColor(rows, view, table);
    ```

### Output

??? question "getTableFormulaResults"

    Get the data in the calculation formula column of the table

    ``` js
    dtable.getTableFormulaResults(table, rows)
    ```

    __Arguments__

    * table: table object
    * rows: row data of the relevant data of the calculation formula column

    __Example__

    ``` js
    const tableName = 'tableName';
    const viewName = 'viewName';
    const table = dtable.getTableByName(tableName);
    const view = dtable.getViewByName(table, viewName);
    const rows = dtable.getViewRows(view, table);
    const formulaResult = dtable.getTableFormulaResults(table, rows);
    ```

??? question "getLinkCellValue"

    Get a list of names of collaborators

    ``` js
    ```

    __Example__

    ``` js
    ```

??? question "getLinkDisplayString"

    Get a list of names of collaborators

    ``` js
    ```

    __Example__

    ``` js
    ```

??? question "getLinkDisplayString"

    Get a list of names of collaborators

    ``` js
    ```

    __Example__

    ``` js
    ```

??? question "getNumberDisplayString"

    Get a list of names of collaborators

    ``` js
    ```

    __Example__

    ``` js
    ```

??? question "getGeolocationDisplayString"

    Get a list of names of collaborators

    ``` js
    ```

    __Example__

    ``` js
    ```

??? question "getDurationDisplayString"

    Get a list of names of collaborators

    ``` js
    ```

    __Example__

    ``` js
    ```

??? question "getDateDisplayString"

    Get a list of names of collaborators

    ``` js
    ```

    __Example__

    ``` js
    ```

## Tables

??? question "addTable"

    Get a list of names of collaborators

    ``` js
    ```

    __Example__

    ``` js
    ```

??? question "deleteTable"

    Get a list of names of collaborators

    ``` js
    ```

    __Example__

    ``` js
    ```

??? question "renameTable"

    Get a list of names of collaborators

    ``` js
    ```

    __Example__

    ``` js
    ```

??? question "getTables"

    Get a list of names of collaborators

    ``` js
    ```

    __Example__

    ``` js
    ```

??? question "getActiveTable"

    Get a list of names of collaborators

    ``` js
    ```

    __Example__

    ``` js
    ```

??? question "getTableByName"

    Get a list of names of collaborators

    ``` js
    ```

    __Example__

    ``` js
    ```

??? question "getTableById"

    Get a list of names of collaborators

    ``` js
    ```

    __Example__

    ``` js
    ```

??? question "importDataIntoNewTable"

    Get a list of names of collaborators

    ``` js
    ```

    __Example__

    ``` js
    ```

## Views

??? question "addView"

    Get a list of names of collaborators

    ``` js
    ```

    __Example__

    ``` js
    ```

??? question "deleteView"

    Get a list of names of collaborators

    ``` js
    ```

    __Example__

    ``` js
    ```

??? question "renameView"

    Get a list of names of collaborators

    ``` js
    ```

    __Example__

    ``` js
    ```

??? question "getViews"

    Get a list of names of collaborators

    ``` js
    ```

    __Example__

    ``` js
    ```

??? question "getNonArchiveViews"

    Get a list of names of collaborators

    ``` js
    ```

    __Example__

    ``` js
    ```

??? question "getActiveView"

    Get a list of names of collaborators

    ``` js
    ```

    __Example__

    ``` js
    ```

??? question "getViewByName"

    Get a list of names of collaborators

    ``` js
    ```

    __Example__

    ``` js
    ```

??? question "getViewById"

    Get a list of names of collaborators

    ``` js
    ```

    __Example__

    ``` js
    ```

??? question "isDefaultView"

    Get a list of names of collaborators

    ``` js
    ```

    __Example__

    ``` js
    ```

??? question "isGroupView"

    Get a list of names of collaborators

    ``` js
    ```

    __Example__

    ``` js
    ```

??? question "isFilterView"

    Get a list of names of collaborators

    ``` js
    ```

    __Example__

    ``` js
    ```

## Columns

??? question "getColumns"

    Get a list of names of collaborators

    ``` js
    ```

    __Example__

    ``` js
    ```

??? question "getShownColumns"

    Get a list of names of collaborators

    ``` js
    ```

    __Example__

    ``` js
    ```

??? question "getColumnsByType"

    Get a list of names of collaborators

    ``` js
    ```

    __Example__

    ``` js
    ```

??? question "getColumnByName"

    Get a list of names of collaborators

    ``` js
    ```

    __Example__

    ``` js
    ```

??? question "getColumnByKey"

    Get a list of names of collaborators

    ``` js
    ```

    __Example__

    ``` js
    ```

??? question "modifyColumnData"

    Get a list of names of collaborators

    ``` js
    ```

    __Example__

    ``` js
    ```

## Rows

??? question "sqlQuery"

    Use sql statement to query a dtable

    ``` js
    dtable.sqlQuery(sql)
    ```

    __Arguments__

    * sql: SQL statement to be executed

    Note: By default, up to 100 results are returned. If you need more results, please add the limit parameter in the sql statement

    Possible errors include

    * ValueError: sql can not be empty
    * ConnectionError: network error
    * Exception: no such table
    * Exception: no such column
    * Exception: columns in group by should match columns in select

    __Example__

    ``` js
    dtable.sqlQuery('select name, price, year from Bill')
    ```

    ```javascript
    [
        {'_id': 'PzBiZklNTGiGJS-4c0_VLw', 'name': 'Bob', 'price': 300, 'year': 2019},
        {'_id': 'Ep7odyv1QC2vDQR2raMvSA', 'name': 'Bob', 'price': 300, 'year': 2021},
        {'_id': 'f1x3X_8uTtSDUe9D60VlYQ', 'name': 'Tom', 'price': 100, 'year': 2019},
        {'_id': 'NxeaB5pDRFKOItUs_Ugxug', 'name': 'Tom', 'price': 100, 'year': 2020},
        {'_id': 'W0BrjGQpSES9nfSytvXgMA', 'name': 'Tom', 'price': 200, 'year': 2021},
        {'_id': 'EvwCWtX3RmKYKHQO9w2kLg', 'name': 'Jane', 'price': 200, 'year': 2020},
        {'_id': 'BTiIGSTgR06UhPLhejFctA', 'name': 'Jane', 'price': 200, 'year': 2021}
    ]
    ```

    __WHERE__

    ```javascript
    dtable.sqlQuery('select name, price from Bill where year = 2021 ')
    ```

    ```javascript
    [
        {'_id': 'Ep7odyv1QC2vDQR2raMvSA', 'name': 'Bob', 'price': 300},
        {'_id': 'W0BrjGQpSES9nfSytvXgMA', 'name': 'Tom', 'price': 200},
        {'_id': 'BTiIGSTgR06UhPLhejFctA', 'name': 'Jane', 'price': 200}
    ]
    ```

    __ORDER BY__

    ```javascript
    dtable.sqlQuery('select name, price, year from Bill order by year')
    ```

    ```javascript
    [
        {'_id': 'PzBiZklNTGiGJS-4c0_VLw', 'name': 'Bob', 'price': 300, 'year': 2019},
        {'_id': 'f1x3X_8uTtSDUe9D60VlYQ', 'name': 'Tom', 'price': 100, 'year': 2019},
        {'_id': 'NxeaB5pDRFKOItUs_Ugxug', 'name': 'Tom', 'price': 100, 'year': 2020},
        {'_id': 'EvwCWtX3RmKYKHQO9w2kLg', 'name': 'Jane', 'price': 200, 'year': 2020},
        {'_id': 'Ep7odyv1QC2vDQR2raMvSA', 'name': 'Bob', 'price': 300, 'year': 2021},
        {'_id': 'W0BrjGQpSES9nfSytvXgMA', 'name': 'Tom', 'price': 200, 'year': 2021},
        {'_id': 'BTiIGSTgR06UhPLhejFctA', 'name': 'Jane', 'price': 200, 'year': 2021}
    ]
    ```

    __GROUP BY__

    ```javascript
    dtable.sqlQuery('select name, sum(price) from Bill group by name')
    ```

    ```javascript
    [
        {'SUM(price)': 600, 'name': 'Bob'},
        {'SUM(price)': 400, 'name': 'Tom'},
        {'SUM(price)': 400, 'name': 'Jane'}
    ]
    ```

    __DISTINCT__

    ```javascript
    dtable.sqlQuery('select distinct name from Bill')
    ```

    ```javascript
    [
        {'_id': 'PzBiZklNTGiGJS-4c0_VLw', 'name': 'Bob'},
        {'_id': 'f1x3X_8uTtSDUe9D60VlYQ', 'name': 'Tom'},
        {'_id': 'EvwCWtX3RmKYKHQO9w2kLg', 'name': 'Jane'}
    ]
    ```

??? question "appendRow"

    Get a list of names of collaborators

    ``` js
    ```

    __Example__

    ``` js
    ```

??? question "deleteRowById"

    Get a list of names of collaborators

    ``` js
    ```

    __Example__

    ``` js
    ```

??? question "deleteRowsByIds"

    Get a list of names of collaborators

    ``` js
    ```

    __Example__

    ``` js
    ```

??? question "modifyRow"

    Get a list of names of collaborators

    ``` js
    ```

    __Example__

    ``` js
    ```

??? question "forEachRow"

    Get a list of names of collaborators

    ``` js
    ```

    __Example__

    ``` js
    ```

??? question "getTableLinkRows"

    Get a list of names of collaborators

    ``` js
    ```

    __Example__

    ``` js
    ```

??? question "getViewRows"

    Get a list of names of collaborators

    ``` js
    ```

    __Example__

    ``` js
    ```

??? question "getGroupRows"

    Get a list of names of collaborators

    ``` js
    ```

    __Example__

    ``` js
    ```

??? question "getInsertedRowInitData"

    Get a list of names of collaborators

    ``` js
    ```

    __Example__

    ``` js
    ```

??? question "getRowsByID"

    Get a list of names of collaborators

    ``` js
    ```

    __Example__

    ``` js
    ```

??? question "getRowById"

    Get a list of names of collaborators

    ``` js
    ```

    __Example__

    ``` js
    ```

??? question "moveGroupRows"

    Get a list of names of collaborators

    ``` js
    ```

    __Example__

    ``` js
    ```

## Plugins

??? question "getPluginSettings"

    Get a list of names of collaborators

    ``` js
    ```

    __Example__

    ``` js
    ```

??? question "updatePluginSettings"

    Get a list of names of collaborators

    ``` js
    ```

    __Example__

    ``` js
    ```

??? question "deletePluginSettings"

    Get a list of names of collaborators

    ``` js
    ```

    __Example__

    ``` js
    ```

## Constants

??? question "ColumnTypes"

    Get a list of names of collaborators

    ``` js
    ```

    __Example__

    ``` js
    ```

??? question "Column icon configs"

    Get a list of names of collaborators

    ``` js
    ```

    __Example__

    ``` js
    ```

??? question "Column options"

    Get a list of names of collaborators

    ``` js
    ```

    __Example__

    ``` js
    ```

??? question "Formula result type"

    Get a list of names of collaborators

    ``` js
    ```

    __Example__

    ``` js
    ```

??? question "Select option colors"

    Get a list of names of collaborators

    ``` js
    ```

    __Example__

    ``` js
    ```

??? question "Table permission type"

    Get a list of names of collaborators

    ``` js
    ```

    __Example__

    ``` js
    ```
