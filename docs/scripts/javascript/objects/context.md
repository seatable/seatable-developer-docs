# Context

When the script runs, the `context` object context-related elements. The usage is as follows.

!!! abstract "currentTable"

    Currently selected table.

    ``` js
    base.context.currentTable;
    ```

    __Output__ The name of the currently selected table

    __Example__

    ``` js
    const name = base.context.currentTable;
    output.text(`The name of the current table is: ${name}`);
    ```

!!! abstract "currentRow"

    Currently selected row. If the script is launched from a button click, this is the row on which the button was clicked.
    
    ``` js
    base.context.currentRow;
    ```

    __Output__ Complete row object, including `_id`, `_mtime`, `_ctime`. If no row is selected, this function returns `undefined`.

    __Example__

    ``` js
    const row = base.context.currentRow;
    output.text(row);
    ```
