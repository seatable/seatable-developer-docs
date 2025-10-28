# Links

!!! warning "link id and column key"

    `link_id` should not be mistaken with the column `key`! The `key` value is unique (like an id) whereas the link id will be shared between the two linked columns. Please note that `link_id` is used as argument to add/update/remove links, whereas you'll have to provide `link_column_key` (the link column `key`) to get linked records. Both information are available in the column object:
    
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

    1. The column `key` (referred as `link_column_key` in `base.get_linked_records` arguments)

    2. The link id of the column (referred as `link_id` in the add/update/remove links operations)

    3. The table whose id is `table_id` is referred later in this section as the *source* table (the table containing this column)

    4. The table whose id is `other_table_id` is referred later in this section as the *target* table

## Get link id

!!! abstract "get_column_link_id"

    Get the link id of the column `column_name` from the table `table_name`.

    ``` python
    base.get_column_link_id(table_name, column_name)
    ```

    __Output__ String (throws an error if no table named `table_name` exists or if no column named `column_name` exists)

    __Example__
    
    ``` python
    from seatable_api import Base, context

    base = Base(context.api_token, context.server_url)
    base.auth()
    link_id = base.get_column_link_id('Table1', 'Link column')
    print(link_id)
    ```

## Get linked records

!!! info "Rows and records, source and target"

    Rows and records are basically the same things. However, to make the following description easier to understand, we will differentiate them:

    - Rows are from the *source* table (the table whose id is `table_id`)

    - Records are the rows from the *target* table (the table linked to the *source* table in the column whose `key` is `link_column_key` or whose link id is `link_id`)

!!! abstract "get_linked_records"

    List the records linked (in the column whose `key` is `link_column_key`) to one or more rows of the *source* table. The row(s) you want to get the linked records from are defined in the `rows` objects (see below).

    ``` python
    base.get_linked_records(table_id, link_column_key, rows) # (1)!
    ```

    1. `table_id`: the id of *source* table

        `link_column_key`: the column **key** of the link-type column of *source* table (**not** the link id from `base.get_column_link_id`)

        `rows`: a list of dicts, each of them containing:
        
        - `row_id`: the id of the row we want to get the linked records from
        
        - `limit`: the maximum number of linked records to get (default is 10)
        
        - `offset`: the number of first linked records not to retrieve (default is 0)
    
    __Output__ Single dict where each `key` is the id of a row of the *source* table and the corresponding value is a list of link dicts (see Output structure example below)

    __Example__

    === "Function run"
    
        ```python
        import json
        from seatable_api import Base, context

        base = Base(context.api_token, context.server_url)
        base.auth()
        linked_records = base.get_linked_records('0000', '89o4', rows=[
            {'row_id': 'FzNqJxVUT8KrRjewBkPp8Q', 'limit': 2, 'offset': 0},
            {'row_id': 'Jmnrkn6TQdyRg1KmOM4zZg', 'limit': 20}
        ])
        print(json.dumps(linked_records, indent=' ')) 
        ```
    
    === "Output structure example"

        ```json
        {
            "FzNqJxVUT8KrRjewBkPp8Q" /* (1)! */: [
                {"row_id": "LocPgVvsRm6bmnzjFDP9bA", "display_value": "1"} /* (2)! */,
                {"row_id": "OA6x7CYoRuyc2pT52Znfmw", "display_value": "3"},
                ...
            ],
            "Jmnrkn6TQdyRg1KmOM4zZg": [
                {"row_id": "LocPgVvsRm6bmnzjFDP9bA", "display_value": "1"},
                {"row_id": "OA6x7CYoRuyc2pT52Znfmw", "display_value": "3"},
                ...
            ]
        }
        ```

        1. id of a row of the *source* table

        2. link object: 
        
            - `row_id` is the id of the linked record (row from the *target* table)
            - `display_value` is the displayed in the column whose `key` is `link_column_key`
            (from a column of the *target* table)

## Add link

!!! abstract "add_link"

    Add link in a link-type column. You'll need the *source* target's name `table_name`, the *target* table's name `other_table_name`, the link id from the link-type column and both the ids of the rows you want to link: `row_id` for the row from the *source* table and `other_row_id` for the record from the *target* table.

    ``` python
    base.add_link(link_id, table_name, other_table_name, row_id, other_row_id)
    ```

    __Output__ Dict containing a single `success` key with the result of the operation (throws an error if no column with ink id `link_id` exists in the *source* table, if no table named `table_name` or `other_table_name` exists or if no row with id `row_id` or `other_row_id` exists in their respective tables)

    __Example__

    ```python
    base.add_link('5WeC', 'Team Members', 'Contacts', 'CGtoJB1oQM60RiKT-c5J-g', 'PALm2wPKTCy-jdJNv_UWaQ');
    ```
    
    __Example: Add link to current row__
    
    ``` python
    from seatable_api import Base, context
    # Do not hesitate to store the tables' and columns' names at the beginning of your script,
    # it will make it really easier to update if names change
    TABLE1_NAME = "Table1";
    TABLE1_LINK_COLUMN_NAME = "Table2 link";
    TABLE2_NAME = "Table2";

    base = Base(context.api_token, context.server_url)
    base.auth()
    lin_id = base.get_column_link_id(TABLE1_NAME,TABLE1_LINK_COLUMN_NAME); # (1)!
    current_row_id = context.current_row['_id'];
    base.add_link(lin_id, TABLE1_NAME, TABLE2_NAME, current_row_id, 'J5St2clyTMu_OFf9WD8PbA')
    ```

    1. Remember you can use `base.get_column_link_id` to get the link id of a specific link-type column.

## Update link(s)

!!! abstract "update_link"

    Update the content of the link-type column whose link id is `link_id` for the row with id `row_id` in the table `table_name`. It will remove all existing row links and add new links to records of table `other_table_name` with ids in the `other_rows_ids` list.

    ``` python
    base.update_link(link_id, table_name, other_table_name, row_id, other_rows_ids)
    ```

    __Output__ Dict containing a single `success` key with the result of the operation (throws an error if no column with ink id `link_id` exists in the *source* table, if no table named `table_name` or `other_table_name` exists or if no row with id `row_id` exists in the *source* table)

    __Example__
    
    ``` python
    from seatable_api import Base, context

    base = Base(context.api_token, context.server_url)
    base.auth()
    base.update_link(
        link_id='r4IJ',
        table_name='Table1',
        other_table_name='Table2',
        row_id='BXhEm9ucTNu3FjupIk7Xug',
        other_rows_ids=[
          'exkb56fAT66j8R0w6wD9Qg',
          'DjHjwmlRRB6WgU9uPnrWeA'
        ]
    )
    ```

!!! abstract "batch_update_links"

    Same than above,except that it allows you to batch update infos of link-type columns for several rows at once. Learn more about `other_rows_ids_map` in the [SeaTable API Reference](https://api.seatable.com/reference/createrowlink). This function can't operate more than 1000 rows at once. If you need to deal with more than 1000 rows at once, please refer to the [common questions](../common_questions.md#dealing-with-more-than-1000-rows-at-once-with-batch-operations).

    ``` python
    base.batch_update_links(link_id, table_name, other_table_name, row_id_list, other_rows_ids_map) # (1)!
    ```

    1. `row_id_list` is a list containing the ids of all the rows of the source table (whose id is `table_id`) you want to update

        `other_rows_ids_map` is an object with the following syntax, the keys `id_1`,`id_2`,...,`id_n` being **all** the ids of `row_id_list`:

        ``` python
        {
            'id_1': [record1['_id'], record2['_id']],
            'id_2': [record5['_id']],
            ...
            'id_n': [record1['_id'], recordn['_id']]
        }
        ```

    __Output__ Dict containing a single `success` key with the result of the operation (throws an error if no column with ink id `link_id` exists in the *source* table, if no table named `table_name` or `other_table_name` exists or if no row with one of the id `row_id_list` exists in the *source* table)
    
    __Example__
    
    ``` python
    from seatable_api import Base, context

    base = Base(context.api_token, context.server_url)
    base.auth()
    link_id = "WaW5"
    table_name = "Table1"
    other_table_name ="Table2"
    row_id_list = ["fRLglslWQYSGmkU7o6KyHw","FseN8ygVTzq1CHDqI4NjjQ"]
    other_rows_ids_map = {
        "FseN8ygVTzq1CHDqI4NjjQ":["OcCE8aX8T7a4dvJr-qNh3g","JckTyhN0TeS8yvH8D3EN7g"],
        "fRLglslWQYSGmkU7o6KyHw":["MdfUQiWcTL--uMlrGtqqgw","E7Sh3FboSPmfBlDsrj_Fhg","UcZ7w9wDT-uVq4Ohtwgy9w"]
    }
    base.batch_update_links(link_id, table_name, other_table_name, row_id_list, other_rows_ids_map)
    ```

## Remove link

!!! abstract "remove_link"

    Delete the link to the record from table `other_table_name` whose id is `other_row_id` in the row from table `table_name` whose id is `row_id`.

    ``` python
    base.remove_link(link_id, table_name, other_table_name, row_id, other_row_id)
    ```

    __Output__ Dict containing a `success` key with the result of the operation and a `deleted_links_count` with the number of actually deleted links (throws an error if no column with ink id `link_id` exists in the *source* table, if no table named `table_name` or `other_table_name` exists or if no row with id `row_id` or `other_row_id` exists in their respective tables)
    
    __Example__
    
    ``` python
    from seatable_api import Base, context

    base = Base(context.api_token, context.server_url)
    base.auth()
    base.remove_link('5WeC', 'Table1', 'Table2', 'CGtoJB1oQM60RiKT-c5J-g', 'PALm2wPKTCy-jdJNv_UWaQ')
    ```
