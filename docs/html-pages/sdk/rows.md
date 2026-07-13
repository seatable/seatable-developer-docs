---
description: seatable-html-page-sdk reference for row operations — list, add, update, delete, and batch-modify rows in a base from an HTML page.
---

# Rows

Row operations on the `seatable-html-page-sdk`. All methods are asynchronous — `await` them. The `sdk` instance below is created and initialized as shown in [Initialization](initialization.md).

!!! warning "Response format"

    Row methods resolve to the underlying HTTP response — the payload is under `.data`, not the return value itself. For example, `listRows` gives you the rows via `res.data.results` and the column metadata via `res.data.metadata`. The `Returns` sections below describe the shape of `.data`.

!!! tip "Single- and multi-select values"

    Single-select and multi-select fields — including those returned via linked records and lookup formulas — return the **option names**, not their internal IDs.

## List rows

!!! abstract "listRows"

    List rows from a specific table, with pagination.

    ```js
    sdk.listRows({ tableName, start, limit });
    ```

    __Parameters__

    `tableName`
    :   string — name of the target table

    `start`
    :   number — starting index for pagination

    `limit`
    :   number — number of rows to retrieve

    __Returns__ `.data` holds `{ metadata, results }` — `results` is the array of row objects, `metadata` the column definitions.

    __Example__
    ```js
    const res = await sdk.listRows({ tableName: "Employees", start: 0, limit: 50 });
    const rows = res.data.results;
    const columns = res.data.metadata;
    ```

## Add rows

!!! abstract "addRow"

    Add a new row to the specified table.

    ```js
    sdk.addRow({ tableName, rowData });
    ```

    __Parameters__

    `tableName`
    :   string — name of the target table

    `rowData`
    :   object — key-value pairs of column names and values

    __Returns__ `.data` holds `{ row }` — the newly created row object.

    __Example__
    ```js
    const res = await sdk.addRow({
      tableName: "Employees",
      rowData: {
        Name: "Jane Smith",
        Age: 28,
        Department: "Engineering",

        // IDs of records linked in the Manager field
        Manager: ["NSPa_fd4SEqRESqOZzRqyg", "eA6rQDuxQyGITmD1hrfyzw"],
      },
    });
    ```

    !!! tip "Linked record fields"

        Set a link column with `{ "link_column_name": ["linked_row_id1", "linked_row_id2", ...] }`.

!!! abstract "batchAddRows"

    Add multiple rows to the specified table in one call.

    ```js
    sdk.batchAddRows({ tableName, rowsData });
    ```

    __Parameters__

    `tableName`
    :   string — name of the target table

    `rowsData`
    :   array — an array of row objects

    __Returns__ `.data` holds `{ rows }` — the list of created row objects. Each row carries its new `_id`, which you can use to populate link fields in a follow-up call.

    __Example__
    ```js
    await sdk.batchAddRows({
      tableName: "Employees",
      rowsData: [
        {
          Name: "Jane Smith",
          Age: 28,
          Department: "Engineering",
          Manager: ["NSPa_fd4SEqRESqOZzRqyg", "eA6rQDuxQyGITmD1hrfyzw"],
        },
        {
          Name: "Tom",
          Age: 24,
          Department: "Product Management",
          Manager: ["QgK2KMf8Sxad8duPcq6gQA", "bBDbhbzXReSPWpcxq225xA"],
        },
      ],
    });
    ```

## Update rows

!!! abstract "updateRow"

    Update an existing row.

    ```js
    sdk.updateRow({ tableName, rowId, rowData });
    ```

    __Parameters__

    `tableName`
    :   string — name of the target table

    `rowId`
    :   string — the unique ID of the row to update

    `rowData`
    :   object — the fields to update

    __Returns__ `.data` holds `{ success: true, row: {...} }`

    __Example__
    ```js
    await sdk.updateRow({
      tableName: "Employees",
      rowId: "fcHIocncTsOygA3FjL-toQ",
      rowData: { Age: 18 },
    });
    ```

!!! abstract "batchUpdateRows"

    Update multiple rows in one call.

    ```js
    sdk.batchUpdateRows({ tableName, rowsData });
    ```

    __Parameters__

    `tableName`
    :   string — name of the target table

    `rowsData`
    :   array — objects containing a `row_id` and the updated `row` data

    __Returns__ `.data` holds `{ success: true, rows: [{...}, ...] }`

    __Example__
    ```js
    await sdk.batchUpdateRows({
      tableName: "Employees",
      rowsData: [
        { row_id: "fcHIocncTsOygA3FjL-toQ", row: { Age: 18 } },
        { row_id: "BIXJ_dUMS1OW8Lyoxrx4Fw", row: { Age: 24 } },
      ],
    });
    ```

## Delete rows

!!! abstract "deleteRow"

    Delete a single row.

    ```js
    sdk.deleteRow({ tableName, rowId });
    ```

    __Parameters__

    `tableName`
    :   string — name of the target table

    `rowId`
    :   string — the unique ID of the row to delete

    __Returns__ `.data` holds `{ success: true }`

    __Example__
    ```js
    await sdk.deleteRow({
      tableName: "Employees",
      rowId: "fcHIocncTsOygA3FjL-toQ",
    });
    ```

!!! abstract "batchDeleteRows"

    Delete multiple rows in one call.

    ```js
    sdk.batchDeleteRows({ tableName, rowsIds });
    ```

    __Parameters__

    `tableName`
    :   string — name of the target table

    `rowsIds`
    :   array — the row IDs to delete

    __Returns__ `.data` holds `{ success: true }`

    __Example__
    ```js
    await sdk.batchDeleteRows({
      tableName: "Employees",
      rowsIds: ["fcHIocncTsOygA3FjL-toQ", "BIXJ_dUMS1OW8Lyoxrx4Fw"],
    });
    ```
