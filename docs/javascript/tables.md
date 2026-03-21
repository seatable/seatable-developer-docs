# Tables

{%
    include-markdown "includes.md"
    start="<!--tablestructure-start-->"
    end="<!--tablestructure-end-->"
%}

## Get Table(s)

!!! abstract "getActiveTable :material-tag-outline:{ title='Scripting only' }"

    Get the currently selected table. Only available in SeaTable scripts.

    ```js
    base.getActiveTable();
    ```
    __Output__ Single table object

    __Example__
    ```js
    const table = base.getActiveTable();
    output.text(`The name of the active table is: ${table.name}`);
    ```

!!! abstract "getTables"

    Get all tables of the current base.

    ```js
    base.getTables();
    ```
    __Output__ Array of table objects

    __Example__
    ```js
    const tables = base.getTables();
    ```

!!! abstract "getTableByName"

    Get a table object by its name.

    ```js
    base.getTableByName(tableName);
    ```

    __Output__ Single table object (`undefined` if table doesn't exist)

    __Example__
    ```js
    const table = base.getTableByName('Table1');
    ```

## Add Table

!!! abstract "addTable"

    Add a new table to this base. Ensure the name doesn't already exist.

    ```js
    base.addTable(tableName, lang='en', columns=[]);
    ```

    The `lang` and `columns` parameters are optional.

    __Example__
    ```js
    base.addTable('New table');
    ```

## Rename Table

!!! abstract "renameTable"

    Rename an existing table.

    ```js
    base.renameTable(oldName, newName);
    ```

    __Example__
    ```js
    base.renameTable('Table1', 'Projects 2023');
    ```

## Delete Table

!!! abstract "deleteTable"

    Delete a table from the base. The table can be [restored from the logs](https://seatable.com/help/eine-geloeschte-tabelle-wiederherstellen/). Deleting the last table is not possible.

    ```js
    base.deleteTable(tableName);
    ```

    __Example__
    ```js
    base.deleteTable('Old table');
    ```
