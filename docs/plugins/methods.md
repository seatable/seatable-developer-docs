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

??? question "getCollaboratorsName"

    Get a list of names of collaborators

    ``` js
    ```

    __Example__

    ``` js
    ```

??? question "getCollaboratorsName"

    Get a list of names of collaborators

    ``` js
    ```

    __Example__

    ``` js
    ```

??? question "getCollaboratorsName"

    Get a list of names of collaborators

    ``` js
    ```

    __Example__

    ``` js
    ```

??? question "getCollaboratorsName"

    Get a list of names of collaborators

    ``` js
    ```

    __Example__

    ``` js
    ```
