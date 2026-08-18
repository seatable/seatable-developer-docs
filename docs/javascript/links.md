---
description: JavaScript API reference for link columns — retrieve linked records, add, update, and remove links between SeaTable tables.
---

# Links

Link columns connect rows between tables. Most link operations require the `link_id`, which you can retrieve with `getColumnLinkId`.

## Get Link ID

!!! abstract "getColumnLinkId"

    Get the link ID of a link column. You need this ID for all other link operations.

    ```js
    base.getColumnLinkId(tableName, columnName);
    ```

    __Output__ Link ID string (e.g. `'aHL2'`)

    __Example__
    ```js
    const linkId = base.getColumnLinkId('Table1', 'Related Records');
    ```

## Get Linked Records

!!! abstract "getLinkedRecords"

    Get the linked records of one or more rows. Supports pagination per row.

    ```js
    await base.getLinkedRecords(tableId, linkColumnKey, rows);
    ```

    __Output__ Object with row IDs as keys and arrays of linked record info as values.

    __Example__
    ```js
    const linked = await base.getLinkedRecords('0000', '89o4', [
        {'row_id': 'FzNqJxVUT8KrRjewBkPp8Q', 'limit': 10, 'offset': 0},
        {'row_id': 'Jmnrkn6TQdyRg1KmOM4zZg', 'limit': 20}
    ]);

    // Result:
    // {
    //   'FzNqJxVUT8KrRjewBkPp8Q': [
    //       {'row_id': 'LocPgVvsRm6bmnzjFDP9bA', 'display_value': '1'},
    //       ...
    //   ],
    //   'Jmnrkn6TQdyRg1KmOM4zZg': [...]
    // }
    ```

## Add Link

!!! abstract "addLink"

    Create a link between two rows in different tables.

    ```js
    base.addLink(linkId, tableName, otherTableName, rowId, otherRowId);
    ```

    __Example__
    ```js
    base.addLink('5WeC', 'Projects', 'Contacts', 'CGtoJB1oQM60RiKT-c5J-g', 'PALm2wPKTCy-jdJNv_UWaQ');
    ```

## Update Link(s)

!!! abstract "updateLink :material-package-variant-closed:{ title='External client only' }"

    Replace all linked records of a row with a new set.

    ```js
    base.updateLink(linkId, tableName, otherTableName, rowId, otherRowIds);
    ```

    !!! warning "Different name in scripts"

        In a SeaTable script, this method is called `updateLinks` (plural) -- see below. `base.updateLink` is `undefined` in the script context.

    __Example__
    ```js
    base.updateLink('r4IJ', 'Table1', 'Table2', 'BXhEm9ucTNu3FjupIk7Xug', [
        'exkb56fAT66j8R0w6wD9Qg',
        'DjHjwmlRRB6WgU9uPnrWeA'
    ]);
    ```

!!! abstract "updateLinks :material-tag-outline:{ title='Scripting only' }"

    Replace all linked records of a row with a new set. This is the script equivalent of `updateLink`; the parameters are identical.

    ```js
    base.updateLinks(linkId, tableName, otherTableName, rowId, otherRowIds);
    ```

    __Example__
    ```js
    base.updateLinks('r4IJ', 'Table1', 'Table2', 'BXhEm9ucTNu3FjupIk7Xug', [
        'exkb56fAT66j8R0w6wD9Qg',
        'DjHjwmlRRB6WgU9uPnrWeA'
    ]);
    ```

!!! abstract "batchUpdateLinks :material-package-variant-closed:{ title='External client only' }"

    Update links for multiple rows at once.

    ```js
    base.batchUpdateLinks(linkId, tableName, otherTableName, rowIdList, otherRowsIdsMap);
    ```

    __Example__
    ```js
    await base.batchUpdateLinks('WaW5', 'Table1', 'Table2',
        ['fRLglslWQYSGmkU7o6KyHw', 'eSQe9OpPQxih8A9zPXdMVA'],
        {
            'fRLglslWQYSGmkU7o6KyHw': ['MdfUQiWcTL--uMlrGtqqgw', 'E7Sh3FboSPmfBlDsrj_Fhg'],
            'eSQe9OpPQxih8A9zPXdMVA': ['cWHbzQiTR8uHHzH_gVSKIg', 'X56gE7BrRF-i61YlE4oTcw']
        }
    );
    ```

## Remove Link

!!! abstract "removeLink"

    Remove a link between two rows.

    ```js
    base.removeLink(linkId, tableName, otherTableName, rowId, otherRowId);
    ```

    __Example__
    ```js
    base.removeLink('5WeC', 'Projects', 'Contacts', 'CGtoJB1oQM60RiKT-c5J-g', 'PALm2wPKTCy-jdJNv_UWaQ');
    ```
