# Links

## Get Links

!!! question "getLinkedRecords"

    List the linked records of rows. You can get the linked records of multiple rows.

    ```js
    base.getLinkedRecords(table_id, link_column_key, rows)
    ```

    * table_id: the id of link table
    * link_column_key: the column key of the link column of link table ( not link_id )
    * rows: a list, each item of the which contains a row info including row_id, offset (defualt by 0) and limit (default by 10) of link table

    __Example__

    ```js
    base.getLinkedRecords('0000', '89o4', [
    {'row_id': 'FzNqJxVUT8KrRjewBkPp8Q', 'limit': 2, 'offset': 0},
    {'row_id': 'Jmnrkn6TQdyRg1KmOM4zZg', 'limit': 20}
    ])

    // a key-value data structure returned as below
    // key: row_id of link table
    // value: a list which includes the row info of linked table
    {
    'FzNqJxVUT8KrRjewBkPp8Q': [
        {'row_id': 'LocPgVvsRm6bmnzjFDP9bA', 'display_value': '1'},
        {'row_id': 'OA6x7CYoRuyc2pT52Znfmw', 'display_value': '3'},
        ...
    ],
    'Jmnrkn6TQdyRg1KmOM4zZg': [
        {'row_id': 'LocPgVvsRm6bmnzjFDP9bA', 'display_value': '1'},
        {'row_id': 'OA6x7CYoRuyc2pT52Znfmw', 'display_value': '3'},
        ...
    ]
    }
    ```

## Get Link ID

!!! question "getColumnLinkId"

    Get the link id by column name.

    ```js
    base.getColumnLinkId(tableName, columnName)
    ```

    __Example__

    ```js
    base.getColumnLinkId('Table1', 'Record')
    ```

## Add Links

!!! question "addLink"

    Add link, link other table records. Get more information about linking columns from the [SeaTable API Reference](https://api.seatable.io/reference/create-row-link).

    ```js
    base.addLink(linkId, tableName, linkedTableName, rowId, linkedRowId)
    ```

    __Example__

    ```js
    base.addLink('5WeC', 'Table1', 'Table2', 'CGtoJB1oQM60RiKT-c5J-g', 'PALm2wPKTCy-jdJNv_UWaQ')
    ```

## Remove Links

!!! question "removeLink"

    Delete the link row.

    ```js
    base.removeLink(linkId, tableName, linkedTableName, rowId, linkedRowId)
    ```

    __Example__

    ```js
    base.removeLink('5WeC', 'Table1', 'Table2', 'CGtoJB1oQM60RiKT-c5J-g', 'PALm2wPKTCy-jdJNv_UWaQ')
    ```

## Update Links

!!! question "updateLinks"

    Remove all existing row links and add new links.

    ```js
    base.updateLinks(linkId, tableName, linkedTableName, rowId, updatedlinkedRowIds)
    ```

    __Example__

    ```js
    const rows = base.getRows('contact', 'Default_view');
    // Update row links to [rows[0]._id, rows[1]._id, rows[2]._id, rows[3]._id]
    base.updateLinks('5WeC', 'Table1', 'Table2', 'CGtoJB1oQM60RiKT-c5J-g', [rows[0]._id, rows[1]._id, rows[2]._id, rows[3]._id])
    ```

!!! question "batchUpdateLinks"

    Batch update infos of link-type columns

    ```js
    base.batchUpdateLinks(link_id, table_id, other_table_id, row_id_list, other_rows_ids_map)
    ```
