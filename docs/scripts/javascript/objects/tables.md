# Tables

You'll find below all the available methods to interact with the tables of a SeaTable base.

{%
    include-markdown "includes.md"
    start="<!--tablestructure-start-->"
    end="<!--tablestructure-end-->"
%}

You can have a look at the specific [view](./views.md#global-structure), [column](./columns.md#global-structure) or [row](./rows.md#global-structure) structure on the corresponding pages.

## Get Table(s)

!!! abstract "getActiveTable"

    Get the currently selected table.

    ``` js
    base.getActiveTable();
    ```
    __Output__ Single table object

    __Example__
    ``` js
    const table = base.getActiveTable();
    output.text(`The name of the active table is: ${table.name}`);
    ```

!!! abstract "getTables" 

    Get all tables of the current base.

    ```
    base.getTables();
    ```
    __Output__ Array of table objects

    __Example__
    ``` js
    const tables = base.getTables();
    output.text(tables);
    ```

!!! abstract "getTableByName"

    Get a table object by its name.

    ``` js
    base.getTableByName(tableName: String);
    ```

    __Output__ Single table object (`undefined` if table doesn't exist)

    __Example__

    ```js
    const table = base.getTableByName('Table1');
    // Display only table _id
    output.text(`The id of the table is: ${table._id}`);
    // Display whole table structure
    output.text(table);
    ```

## Add Table

!!! abstract "addTable"

    Add a new table to this base, given the new table name `tableName`. Please ensure that you choose a `tableName` that doesn't already exists in your base.

    ``` js
    base.addTable(tableName: String);
    ```
    __Output__ Nothing

    __Example__
    ``` js
    base.addTable('New table');
    output.text("Wow, I just added a new table to this base.")
    ```

## Rename Table

!!! abstract "renameTable"

    Rename an existing table named `oldName` to `newName`. Please ensure that you choose a `newName` that doesn't already exists in your base.

    ``` js
    base.renameTable(oldName: String, newName: String);
    ```

    __Output__ Nothing (throws an error if no table named `oldName` exists)

    __Example__
    ``` js
    const old_name = "Table1";
    const new_name = "Projects 2023";
    base.renameTable(old_name, new_name);
    output.text(`This base ${old_name} got a new name: ${new_name}`);
    ```

## Delete Table

!!! abstract "deleteTable"

    Delete a table named `tableName` from the base. By the way, the table can be [restored from the logs](https://seatable.com/help/eine-geloeschte-tabelle-wiederherstellen/). Deleting the last table is not possible.

    ``` js
    base.deleteTable(tableName: String);
    ```
    __Output__ Nothing (throws an error if no table named `tableName` exists)

    __Example__
    ``` js
    base.deleteTable('Old table');
    ```
