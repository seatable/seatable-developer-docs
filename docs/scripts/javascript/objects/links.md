# Links

!!! question "addLink"

    Add link, link other table records. Get more information about linking columns from the [SeaTable API Reference](https://api.seatable.io/reference/create-row-link).

    ``` js
    base.addLink(linkId, tableName, linkedTableName, rowId, linkedRowId)
    ```

    __Example__

    ``` js
    base.addLink('5WeC', 'Table1', 'Table2', 'CGtoJB1oQM60RiKT-c5J-g', 'PALm2wPKTCy-jdJNv_UWaQ')
    ```

!!! question "removeLink"

    Delete the link row.

    ``` js
    base.removeLink(linkId, tableName, linkedTableName, rowId, linkedRowId)
    ```

    __Example__

    ``` js
    base.removeLink('5WeC', 'Table1', 'Table2', 'CGtoJB1oQM60RiKT-c5J-g', 'PALm2wPKTCy-jdJNv_UWaQ')
    ```

!!! question "getColumnLinkId"

    Get the link id by column name.

    ``` js
    base.getColumnLinkId(tableName, columnName)
    ```

    __Example__

    ``` js
    base.getColumnLinkId('Table1', 'Record')
    ```

!!! question "updateLinks"

    Remove all existing row links and add new links.

    ``` js
    base.updateLinks(linkId, tableName, linkedTableName, rowId, updatedlinkedRowIds)
    ```

    __Example__

    ``` js
    const rows = base.getRows('contact', 'Default_view');
    // Update row links to [rows[0]._id, rows[1]._id, rows[2]._id, rows[3]._id]
    base.updateLinks('5WeC', 'Table1', 'Table2', 'CGtoJB1oQM60RiKT-c5J-g', [rows[0]._id, rows[1]._id, rows[2]._id, rows[3]._id])
    ```
