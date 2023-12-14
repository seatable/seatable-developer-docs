# Context

When the script runs, the context object provides the context. The usage is as follows.

!!! info "currentTable"

    Returns the name of the currently selected table.

    ``` js
    base.context.currentTable
    ```

    __Example__

    ``` js
    const name = base.context.currentTable
    output.text(`The name of the current table is: ${name}`)
    ```

!!! info "currentRow"

    Returns the currently selected row and returns the complete row object including `_id`, `_mtime`, `_ctime`. If no row is selected, this function returns `undefined`.

    ``` js
    base.context.currentRow
    ```

    __Example__

    ``` js
    const row = base.context.currentRow
    output.text(row)
    ```
