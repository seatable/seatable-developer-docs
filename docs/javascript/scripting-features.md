---
description: SeaTable scripting-only JavaScript features — access the current table and row via context, render output, and use built-in utility helpers.
---

# Scripting Features

These features are only available when running JavaScript scripts inside SeaTable. They provide access to the browser context, output functions, and utility helpers.

## Context

The `base.context` object provides information about the current user interaction.

!!! abstract "currentTable"

    The currently selected table name.

    ```js
    const tableName = base.context.currentTable;
    ```

!!! abstract "currentRow"

    The current row when the script is triggered via a button. Contains the full row data.

    ```js
    const row = base.context.currentRow;
    output.text(row['Name']);
    ```

    !!! warning
        `currentRow` is only available when the script is executed via a [button column](https://seatable.com/help/skript-manuell-per-schaltflaeche-oder-automation-ausfuehren/). When running manually, `currentRow` is `undefined`.

## Output

The `output` object displays results in the script output panel.

!!! abstract "output.text"

    Display text or any variable in the output panel. Accepts strings, numbers, objects, and arrays.

    ```js
    output.text(anything);
    ```

    __Example__
    ```js
    output.text('Hello World');
    output.text(42);
    output.text(row);
    ```

!!! abstract "output.markdown"

    Display markdown-formatted content in the output panel.

    ```js
    output.markdown(markdownString);
    ```

    __Example__
    ```js
    output.markdown('# Title\n\nSome **bold** text.');
    ```

## Utilities

The `base.utils` object provides helper functions.

!!! abstract "formatDate"

    Format a date object to `YYYY-MM-DD`.

    ```js
    base.utils.formatDate(date);
    ```

    __Example__
    ```js
    const today = base.utils.formatDate(new Date());
    // Returns: "2026-03-18"
    ```

!!! abstract "formatDateWithMinutes"

    Format a date object to `YYYY-MM-DD HH:mm`.

    ```js
    base.utils.formatDateWithMinutes(date);
    ```

    __Example__
    ```js
    const now = base.utils.formatDateWithMinutes(new Date());
    // Returns: "2026-03-18 14:30"
    ```

!!! abstract "lookupAndCopy"

    Look up a value in another table and copy it. Similar to VLOOKUP in spreadsheets.

    ```js
    base.utils.lookupAndCopy(targetTable, targetColumn, targetColumnToSearch, sourceTable, sourceColumn, sourceColumnToSearch);
    ```

    __Example__
    ```js
    // Copy "Email" from Contacts table where the Name matches
    base.utils.lookupAndCopy(
        'Orders', 'Customer Email', 'Customer Name',
        'Contacts', 'Email', 'Name'
    );
    ```
