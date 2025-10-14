# Links

!!! warning "link id and column key"

    `linkId` should not be mistaken with the column `key`! The `key` value is unique (like an id) whereas the link id will be shared between the two linked columns. Please note that `linkId` is used as argument to add/update/remove links, whereas you'll have to provide `linkColumnKey` (the link column `key`) to get linked records. Both information are available in the column object:
    
    ```json
    {
     "key": "Cp51", /* (1)! */
     "type": "link",
     "name": "Link column",
     "editable": true,
     "width": 200,
     "resizable": true,
     "draggable": true,
     "data": {
      "display_column_key": "0000",
      "is_internal": true,
      "link_id": "UAmR", /* (2)! */
      "table_id": "FJkA",  /* (3)! */
      "other_table_id": "nw8k",  /* (4)! */
      "is_multiple": true,
      "is_row_form_view": false,
      "view_id": "",
      "array_type": "text",
      "array_data": null,
      "result_type": "array"
     },
     "permission_type": "",
     "permitted_users": [],
     "permitted_group": [],
     "edit_metadata_permission_type": "",
     "edit_metadata_permitted_users": [],
     "edit_metadata_permitted_group": [],
     "description": null,
     "colorbys": {}
    }
    ```

    1. The column `key` (referred as `linkColumnKey` in `base.getLinkedRecords` arguments)

    2. The link id of the column (referred as `linkId` in the add/update/remove link(s) methods arguments)

    3. The table whose id is `table_id` is referred later in this section as the *source* table (the table containing this column)

    4. The table whose id is `other_table_id` is referred later in this section as the *target* table

## Get linkId

!!! abstract "getColumnLinkId"

    Get the link id of the column `columnName` from the table `tableName`.

    ```js
    base.getColumnLinkId(tableName: String, columnName: String);
    ```

    __Output__ String (throws an error if table `tableName` or column `columnName` doesn't exist)

    __Example__

    ```js
    base.getColumnLinkId('Table1', 'Table2 link');
    ```

## Get linked records

!!! info "Rows and records, source and target"

    Rows and records are basically the same things. However, to make the following description easier to understand, we will differentiate them:

    - Rows are from the *source* table (the table whose id is `tableId`)

    - Records are the rows from the *target* table (the table linked to the *source* table in the column whose `key` is `linkColumnKey` or whose link id is `linkId`)

!!! abstract "getLinkedRecords"

    List the records linked (in the column whose `key` is `linkColumnKey`) to one or more rows of the *source* table. The row(s) you want to get the linked records from are defined in the `linkedRows` object (see below).

    ```js
    await/* (1)! */ base.getLinkedRecords(tableId: String, linkColumnKey: String, linkedRows: Object) /* (2)! */;
    ```

    1. `await` is used for asynchronous functions. This is **required** to ensure that the following operations (or the variable where you store the results) wait for the query's response to arrive before continuing to execute the script
    
    2. `tableId`: the id of *source* table

        `linkColumnKey`: the column **key** of the link-type column of *source* table (**not** the link id from `base.getColumnLinkId`)

        `linkedRows`: an array of objects, each of them containing:
        
        - `row_id`: the id of the row we want to get the linked records from
        
        - `limit`: the maximum number of linked records to get (default is 10)
        
        - `offset`: the number of first linked records not to retrieve (default is 0)
    
    __Output__ A `key`:`value` data structure where each `key` is the id of a row of the *source* table and the corresponding value is an array of link objects (see Output structure example below)
    
    __Example__

    === "Function run"

        ```js
        await base.getLinkedRecords('0000', '89o4', [
        {'row_id': 'FzNqJxVUT8KrRjewBkPp8Q', 'limit': 2, 'offset': 0},
        {'row_id': 'Jmnrkn6TQdyRg1KmOM4zZg', 'limit': 20}
        ]);
        ```

    === "Output structure example"

        ```js
        {
        'FzNqJxVUT8KrRjewBkPp8Q' /* (1)! */: [
            {'row_id': 'LocPgVvsRm6bmnzjFDP9bA', 'display_value': '1'} /* (2)! */,
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

        1. id of a row of the *source* table

        2. link object: 
        
            - `row_id` is the id of the linked record (row from the *target* table)
            - `display_value` is the displayed in the column whose `key` is `linkColumnKey`
            (from a column of the *target* table)

    __Output__ Object containing the linked records for each row (see Output structure example above)

    __Example: Get linked records from current row__

    ```js
        const table = base.getTableByName('Table1');
        const linkColumn = base.getColumnByName(table,'Table2 link');
        const currentRowLinks = await base.getLinkedRecords(table._id, linkColumn.key, [{'row_id': base.context.currentRow._id, 'limit':100  /* (1)! */}]);
        currentRowLinks[base.context.currentRow._id].forEach((link) => {output.text(link)});
    ```

    1. `limit`:100 => the response will return maximum 100 rows


## Add link

!!! abstract "addLink"

    Add link in a link-type column. You'll need the *source* target's name `tableName`, the *target* table's name `linkedTableName`, the `linkId` from the link-type column and both the ids of the rows you want to link: `rowId` for the row from the *source* table and `linkedRowId` for the record from the *target* table.

    ```js
    base.addLink(linkId: String, tableName: String, linkedTableName: String, rowId: String, 
                 linkedRowId: String);
    ```

    __Output__ Nothing

    __Example__

    ```js
    base.addLink('5WeC', 'Team Members', 'Contacts', 'CGtoJB1oQM60RiKT-c5J-g', 'PALm2wPKTCy-jdJNv_UWaQ');
    ```

    __Example: Add link to current row__

    ```js
    // Do not hesitate to store the tables' and columns' names at the beginning of your script,
    // it will make it really easier to update if names change
    const table1Name = "Table1";
    const table1LinkColumnName = "Table2 link";
    const table2Name = "Table2";

    const linId = base.getColumnLinkId(table1Name,table1LinkColumnName); /* (1)! */
    const currentRowId = base.context.currentRow._id;
    base.addLink(linId, table1Name, table2Name, currentRowId, 'J5St2clyTMu_OFf9WD8PbA');
    ```

    1. Remember you can use `base.getColumnLinkId` to get the link id of a specific link-type column.


## Update link(s)

!!! abstract "updateLinks"

    Update the content of the link-type column whose link id is `linkId` for the row with id `rowId` in the table `tableName`. It will remove all existing row links and add new links to records of table `linkedTableName` with ids listed in the `updatedlinkedRowIds` array.

    ```js
    base.updateLinks(linkId, tableName, linkedTableName, rowId, updatedlinkedRowIds: Array of String);
    ```

    __Output__ Nothing

    __Example__

    ```js
    const records = base.getRows('Contacts', 'Default_view');
    // Update links for row from "Team Members" with _id CGtoJB1oQM60RiKT-c5J-g to [records[0]._id, records[1]._id, records[2]._id, records[3]._id]
    // Real-life tip: ensure that the array "records" actually contains at least 4 elements!
    base.updateLinks('5WeC', 'Team Members', 'Contacts', 'CGtoJB1oQM60RiKT-c5J-g', [records[0]._id, records[1]._id, records[2]._id, records[3]._id]);
    ```

## Remove link

!!! abstract "removeLink"

    Delete the link to the record from table `linkedTableName` whose id is `linkedRowId` in the row from table `tableName` whose id is `rowId`. Every arguments are `String`.

    ```js
    base.removeLink(linkId, tableName, linkedTableName, rowId, linkedRowId);
    ```

    __Output__ Nothing

    __Example__

    ```js
    base.removeLink('5WeC', 'Team Members', 'Contacts', 'CGtoJB1oQM60RiKT-c5J-g', 'PALm2wPKTCy-jdJNv_UWaQ');
    ```
