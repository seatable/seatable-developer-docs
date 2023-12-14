# Tables

All available functions to interact with the tables of a SeaTable base.

## Get Table(s)

!!! question "getActiveTable"

    Get the currently selected table and return a table object.

    ``` js
    base.getActiveTable();
    ```

    __Example__
    ``` js
    const table = base.getActiveTable();
    output.text(`The name of the active table is: ${table.name}`);
    ```

!!! question "getTables"

    Get all tables of this base as `json` object with all rows and metadata.

    ```
    base.getTables();
    ```

    __Example__
    ``` js
    const tables = base.getTables();
    output.text(tables);
    ```

!!! question "getTableByName"

    Get a table object by its name. The object contains all rows and metadata.
    ``` js
    base.getTableByName(tableName: String);
    ```

    __Example__
    ``` js
    const table = base.getTableByName('Table1');
    output.text(`The id of the table is: ${table._id}`);
    ```

## Add Table

!!! question "addTable"

    Add a new table to this base. The table should not exist already in your base.

    ``` js
    base.addTable(tableName: String);
    ```

    __Example__
    ``` js
    base.addTable('New table');
    output.text("Wow, I just added a new table to this base.")
    ```

## Rename Table

!!! question "renameTable"

    Rename an existing table.

    ``` js
    base.renameTable(oldName: String, newName: String);
    ```

    __Example__
    ``` js
    const old_name = "Table1";
    const new_name = "Projects 2023";
    base.renameTable(old_name, new_name);
    output.text(`This base ${old_name} got a new name: ${new_name}`);
    ```

## Delete Table

!!! question "deleteTable"

    Delete a table from the base. By the way, the table can be [restored from the logs](https://seatable.io/docs/arbeiten-in-tabellen/eine-geloeschte-tabelle-wiederherstellen/?lang=auto).

    ``` js
    base.deleteTable(tableName: String);
    ```

    __Example__
    ``` js
    base.deleteTable('Old table');
    ```
