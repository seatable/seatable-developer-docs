### Links

## Get link id

!!! question "Get link id"

    Get the link id by column name

    ``` python
    base.get_column_link_id(table_name, column_name)
    ```

    __Example__

    ``` python
    base.get_column_link_id('Table1', 'Record')
    ```

## Get linked records

!!! question "Get linked records"

    List the linked records of rows. You can get the linked records of multiple rows.

    ``` python
    base.get_linked_records(table_id, link_column_key, rows)
    ```

    __Example__

    ``` python
    # rows: a list, each item of the which contains a row info including row_id, offset (defualt by 0) and limit (default by 10) of link table.
    base.get_linked_records('0000', '89o4', rows=[
        {'row_id': 'FzNqJxVUT8KrRjewBkPp8Q', 'limit': 2, 'offset': 0},
        {'row_id': 'Jmnrkn6TQdyRg1KmOM4zZg', 'limit': 20}
    ])
    # a key-value data structure returned as below
    # key: row_id of link table
    # value: a list which includes the row info of linked table
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

## Add link

!!! question "Add link"

    Add links, link other table records. A link column must already exist.

    ``` python
    base.add_link(link_id, table_name, other_table_name, row_id, other_row_id)
    ```

    __Example__

    ``` python
    base.add_link('5WeC', 'Table1', 'Table2', 'CGtoJB1oQM60RiKT-c5J-g', 'PALm2wPKTCy-jdJNv_UWaQ')
    ```

## Update link

!!! question "Update link"

    Modify the info of link-type column.

    ``` python
    update_link(self, link_id, table_name, other_table_name, row_id, other_rows_ids)
    ```

    __Example__

    ``` python
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

## Batch update links

!!! question "Batch update links"

    Batch update infos of link-type columns.

    ``` python
    base.batch_update_links(link_id, table_name, other_table_name, row_id_list, other_rows_ids_map)
    ```

    __Example__

    ``` python
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

!!! question "Remove link"

    Delete the link row.

    ``` python
    base.remove_link(link_id, table_name, other_table_name, row_id, other_row_id)
    ```

    __Example__

    ``` python
    base.remove_link('5WeC', 'Table1', 'Table2', 'CGtoJB1oQM60RiKT-c5J-g', 'PALm2wPKTCy-jdJNv_UWaQ')
    ```
