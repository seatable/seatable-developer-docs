---
description: seatable-html-page-sdk reference for incrementally adding and removing linked records from link columns in an HTML page.
---

# Links

Link operations on the `seatable-html-page-sdk`. Use these methods to add or remove particular relationships without replacing the entire value of a link column. All methods are asynchronous — `await` them. The `sdk` instance below is created and initialized as shown in [Initialization](initialization.md).

!!! warning "Response format"

    Link methods resolve to the underlying HTTP response. Read the payload from `.data`. Single-row methods return the updated source row in `.data.row`; batch methods return updated source rows in `.data.rows`.

## Add and delete one link

!!! abstract "addLink"

    Add one linked record to a link-column cell without replacing its existing links.

    ```js
    sdk.addLink({ tableName, rowId, linkColumnName, otherRowId });
    ```

    __Parameters__

    `tableName`
    :   string — name of the table containing the link column

    `rowId`
    :   string — the `_id` of the source row in `tableName`

    `linkColumnName`
    :   string — name of the link column; use its display name, not its internal key

    `otherRowId`
    :   string — the `_id` of the record to add from the link column's configured target table

    __Returns__ `.data` holds `{ success: true, row }` — `row` is the updated source row.

    __Example__
    ```js
    const res = await sdk.addLink({
      tableName: "Tasks",
      rowId: "fcHIocncTsOygA3FjL-toQ",
      linkColumnName: "Related projects",
      otherRowId: "NSPa_fd4SEqRESqOZzRqyg",
    });
    const updatedRow = res.data.row;
    ```

!!! abstract "deleteLink"

    Delete one linked record from a link-column cell without changing its other links.

    ```js
    sdk.deleteLink({ tableName, rowId, linkColumnName, otherRowId });
    ```

    __Parameters__

    `tableName`
    :   string — name of the table containing the link column

    `rowId`
    :   string — the `_id` of the source row in `tableName`

    `linkColumnName`
    :   string — name of the link column; use its display name, not its internal key

    `otherRowId`
    :   string — the `_id` of the record to remove from the link column's configured target table

    __Returns__ `.data` holds `{ success: true, row }` — `row` is the updated source row.

    __Example__
    ```js
    const res = await sdk.deleteLink({
      tableName: "Tasks",
      rowId: "fcHIocncTsOygA3FjL-toQ",
      linkColumnName: "Related projects",
      otherRowId: "NSPa_fd4SEqRESqOZzRqyg",
    });
    const updatedRow = res.data.row;
    ```

## Add and delete links in batches

!!! abstract "batchAddLinks"

    Add links to one or more rows in the same source table.

    ```js
    sdk.batchAddLinks({ tableName, linksData });
    ```

    __Parameters__

    `tableName`
    :   string — name of the table containing the link columns

    `linksData`
    :   array — row-oriented link changes. Each item has a `row_id` source-row ID and a `links` object. Each `links` key is a link column display name and its value is an array of linked row IDs.

    __Returns__ `.data` holds `{ success: true, rows }` — `rows` is the array of updated source rows.

    __Example__
    ```js
    const res = await sdk.batchAddLinks({
      tableName: "Tasks",
      linksData: [
        {
          row_id: "fcHIocncTsOygA3FjL-toQ",
          links: {
            "Related projects": ["NSPa_fd4SEqRESqOZzRqyg", "eA6rQDuxQyGITmD1hrfyzw"],
            Reviewers: ["bBDbhbzXReSPWpcxq225xA", "NSPa_fd4SEqRESqOZzRqyg"],
          },
        },
        {
          row_id: "BIXJ_dUMS1OW8Lyoxrx4Fw",
          links: {
            "Related projects": ["eA6rQDuxQyGITmD1hrfyzw", "QgK2KMf8Sxad8duPcq6gQA"],
          },
        },
      ],
    });
    const updatedRows = res.data.rows;
    ```

!!! abstract "batchDeleteLinks"

    Delete specified links from one or more rows in the same source table. Links not listed in `linksData` remain unchanged.

    ```js
    sdk.batchDeleteLinks({ tableName, linksData });
    ```

    __Parameters__

    `tableName`
    :   string — name of the table containing the link columns

    `linksData`
    :   array — row-oriented link changes. Each item has a `row_id` source-row ID and a `links` object. Each `links` key is a link column display name and its value is an array of linked row IDs to remove.

    __Returns__ `.data` holds `{ success: true, rows }` — `rows` is the array of updated source rows.

    __Example__
    ```js
    const res = await sdk.batchDeleteLinks({
      tableName: "Tasks",
      linksData: [
        {
          row_id: "fcHIocncTsOygA3FjL-toQ",
          links: {
            "Related projects": ["NSPa_fd4SEqRESqOZzRqyg", "eA6rQDuxQyGITmD1hrfyzw"],
          },
        },
        {
          row_id: "BIXJ_dUMS1OW8Lyoxrx4Fw",
          links: {
            "Related projects": ["eA6rQDuxQyGITmD1hrfyzw"],
          },
        },
      ],
    });
    const updatedRows = res.data.rows;
    ```

## Notes

- Use `updateRow` or `batchUpdateRows` from [Rows](rows.md) when you want to replace a link-column value with the complete array of linked row IDs while updating other fields. Use the APIs on this page for incremental additions or removals.
