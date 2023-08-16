# predefined objects

## Base object

Base object provide a way to manipulate data in a base. The following methods are available:

### Table

??? question "getActiveTable"

    Get the currently selected table and return a table object.

    ``` js
    base.getActiveTable();
    ```

    __Example__
    ``` js
    const table = base.getActiveTable();
    output.text(`The name of the active table is: ${table.name}`);
    ```

??? question "getTables"

    Get all tables of this base as `json` object with all rows and metadata.

    ```
    base.getTables();
    ```

    __Example__
    ``` js
    const tables = base.getTables();
    output.text(tables);
    ```

??? question "getTableByName"

    Get a table object by its name. The object contains all rows and metadata.
    ``` js
    base.getTableByName(tableName: String);
    ```

    __Example__
    ``` js
    const table = base.getTableByName('Table1');
    output.text(`The id of the table is: ${table._id}`);
    ```
??? question "addTable"

    Add a new table to this base. The table should not exist already in your base.

    ``` js
    base.addTable(tableName: String);
    ```

    __Example__
    ``` js
    base.addTable('New table');
    output.text("Wow, I just added a new table to this base.")
    ```

??? question "renameTable"

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

??? question "deleteTable"

    Delete a table from the base. By the way, the table can be [restored from the logs](https://seatable.io/docs/arbeiten-in-tabellen/eine-geloeschte-tabelle-wiederherstellen/?lang=auto).

    ``` js
    base.deleteTable(tableName: String);
    ```

    __Example__
    ``` js
    base.deleteTable('Old table');
    ```

### View

??? question "getActiveView"

    Get the current view, the method return a view object.

    ``` js
    base.getActiveView();
    ```

    __Example__
    ``` js
    const view  = base.getActiveView();
    output.text(view._id);
    output.text(view);
    ```

??? question "getViews"

    Get all the views of the current table, and return all the views in an array

    ``` js
    base.getViews(table: Object/String);
    ```

    __Example__
    ``` js
    const table  = base.getTableByName('Table1');
    const views = base.getViews(table);
    output.text(views.length);
    ```

??? question "getViewByName"

    Get a view object via its name, and return a view object.

    ``` js
    base.getViewByName(table: Object/String, viewName: String);
    ```

    __Examples__
    ``` js
    const table  = base.getTableByName('Table1'); 
    const view = base.getViewByName(table, 'view 1');
    output.text(view.name);
    ```

    ``` js
    const view = base.getViewByName('Table1', 'view 1');
    output.text(view.name);
    ```

??? question "addView"

    Add a view to a table.

    ``` js
    base.addView(table: Object/String, viewName: String);
    ```

    __Examples__
    ``` js
    const table  = base.getTableByName('Table1');
    base.addView(table, 'view 2');
    ```

    ``` js
    base.addView('Table1', 'view 2');
    ```

??? question "renameView"

    Rename a view in the table.

    ``` js
    base.renameView(table: Object/String, currentViewName: String, nextViewName: String);
    ```

    __Examples__
    ``` js
    const table  = base.getTableByName('Table1');
    base.renameView(table, 'view1', 'view2');
    ```

    ``` js
    base.renameView('Table1', 'view1', 'view2');
    ```

??? question "deleteView"

    Delete a view.

    ``` js
    base.deleteView(table: Object/String, viewName: String);
    ```

    __Examples__
    ``` js
    const table  = base.getTableByName('Table1');
    base.deleteView(table, 'view2');
    ```

    ``` js
    base.deleteView('Table1', 'view2');
    ```

### Column

??? question "getColumns"

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

??? question "getShownColumns"

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

??? question "getColumnByName"

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

??? question "getColumnsByType"

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

### Row

??? question "getRows"

    .

    ``` js
    ```

    __Example__
    ``` js
    ```

??? question "getGroupedRows"

    .

    ``` js
    ```

    __Example__
    ``` js
    ```

??? question "getRowById"

    .

    ``` js
    ```

    __Example__
    ``` js
    ```

??? question "deleteRowById"

    .

    ``` js
    ```

    __Example__
    ``` js
    ```

??? question "addRow"

    .

    ``` js
    ```

    __Example__
    ``` js
    ```

??? question "modifyRow"

    .

    ``` js
    ```

    __Example__
    ``` js
    ```

??? question "modifyRows"

    .

    ``` js
    ```

    __Example__
    ``` js
    ```

??? question "filter"

    .

    ``` js
    ```

    __Example__
    ``` js
    ```

### Links

??? question "addLink"

    .

    ``` js
    ```

    __Example__
    ``` js
    ```

??? question "removeLink"

    .

    ``` js
    ```

    __Example__
    ``` js
    ```

??? question "getColumnLinkId"

    .

    ``` js
    ```

    __Example__
    ``` js
    ```

??? question "updateLinks"

    .

    ``` js
    ```

    __Example__
    ``` js
    ```

### Query

??? question "BASIC"

    .

    ``` js
    ```

    __Example__
    ``` js
    ```

??? question "WHERE"

    .

    ``` js
    ```

    __Example__
    ``` js
    ```

??? question "GROUP BY"

    .

    ``` js
    ```

    __Example__
    ``` js
    ```

??? question "DISTINCT"

    .

    ``` js
    ```

    __Example__
    ``` js
    ```


---

## Base Utility functions

Utility functions help you to work with data in SeaTable.

### Date and Time

??? success "formatDate"

    .

    ``` js
    ```

    __Example__
    ``` js
    ```

??? success "formatDateWithMinutes"

    .

    ``` js
    ```

    __Example__
    ``` js
    ```

### Lookup and Query

??? success "lookupAndCopy"

    .

    ``` js
    ```

    __Example__
    ``` js
    ```

??? success "query"

    .

    ``` js
    ```

    __Example__
    ``` js
    ```


---

## Output

Output object supports output strings in text or Markdown format.

??? quote "text"

    .

    ``` js
    ```

    __Example__
    ``` js
    ```

??? quote "markdown"

    .

    ``` js
    ```

    __Example__
    ``` js
    ```

---



## Context

When the script runs, the context object provides the context. The usage is as follows:

??? info "currentTable"

    .

    ``` js
    ```

    __Example__
    ``` js
    ```

??? info "currentRow"

    .

    ``` js
    ```

    __Example__
    ``` js
    ```
