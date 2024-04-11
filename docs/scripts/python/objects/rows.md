# Rows

## Get row / rows

!!! question "Get row"

    Gets one row of a table by its row ID.

    ``` python
    base.get_row(table_name, row_id)
    ```

    __Example__

    ``` python
    row = base.get_row('Table1', 'U_eTV7mDSmSd-K2P535Wzw')
    ```

!!! question "List rows"

    Lists multiple rows of a table.

    ``` python
    base.list_rows(table_name, view_name=None, order_by=None, desc=False, start=None, limit=None)
    ```

    The default limit is 1000 which is also the maximum number of rows this method returns.

    The query method (see below) offers more filter options and can return more rows.

    __Examples__

    ``` python
    rows = base.list_rows('Table1')
    rows = base.list_rows('Table1', view_name='default', order_by='Age', desc=True, start=5, limit=20)
    ```

!!! question "Query"

    Queries a base using a SQL statement.

    ``` python
    base.query(sql-statement)
    ```

    Unless the SQL statement specifies a higher limit, the method returns a maximum of 100 rows. The maximum number of rows returned is 10000 no matter the limit specified in the SQL statement.

    __Example with a wildcard__

    ``` js
    json_data = base.query('select * from Users') // (1)!
    print(json.dumps(json_data, indent=2))
    ```

    1.  Returns for example the following:
        ``` json
        [
            {
                "Name": "Thomas",
                "_id": "VkyADGkFRiif0bEVHd-CtA",
                "_ctime": "2023-08-16T15:04:56.018Z",
                "_mtime": "2023-08-17T07:02:59.585Z",
                "_creator": "a5adebe279e04415a28b2c7e256e9e8d@auth.local",
                "_last_modifier": "a5adebe279e04415a28b2c7e256e9e8d@auth.local",
                "_locked": null,
                "_locked_by": null,
                "_archived": false
            },
            {
                "Name": "Steve",
                "_id": "UevpAVOjRrmbfqMmpsuTEg",
                "_ctime": "2023-08-17T07:03:00.292Z",
                "_mtime": "2023-08-17T07:03:00.801Z",
                "_creator": "a5adebe279e04415a28b2c7e256e9e8d@auth.local",
                "_last_modifier": "a5adebe279e04415a28b2c7e256e9e8d@auth.local",
                "_locked": null,
                "_locked_by": null,
                "_archived": false
            },
        ]
        ```

    __Example with WHERE__

    ``` python
    json_data = base.query('select name, price from Bill where year = 2021')
    print(json.dumps(json_data, indent=2))
    ```

    __Example with ORDER BY__

    ``` python
    json_data = base.query('select name, price, year from Bill order by year')
    print(json.dumps(json_data, indent=2))
    ```

    __Example with GROUP BY__

    ``` python
    json_data = base.query('select name, sum(price) from Bill group by name')
    print(json.dumps(json_data, indent=2))
    ```

    __Example with DISTINCT__

    ``` python
    json_data = base.query('select distinct name from Bill')
    print(json.dumps(json_data, indent=2))
    ```

## Add rows

By default, the default values specified for the table columns in the webinterface do **not** apply when adding/appending rows via API. In order to apply the default values, add `apply_default=True`as a function parameter. If set to True, the default values can be overwritten by specifying alternative values in `row_data`. 

!!! question "Append row"

    Appends one row to a table.

    ``` python
    base.append_row(table_name, row_data, apply_default=False)
    ```

    __Example__

    ``` python
    row_data = {
        "Name": "Ron"
    }

    base.append_row('Table1', row_data, apply_default=True)
    ```

!!! question "Batch append rows"

    Appends multiple rows to a table.

    ``` python
    base.batch_append_rows(table_name, rows_data, apply_default=False)
    ```

    __Example__

    ``` python
    rows_data = [{
        'Name': 'Ron',
        'Birthday': '1975-01-01'
    }, {
        'Name': 'Richard',
        'Birthday': '1978-10-08'
    }]

    base.batch_append_rows('Table6', rows_data)
    ```

!!! question "Insert row"

    Inserts one row to a table under a anchor row.

    ``` python
    base.insert_row(table_name, row_data, anchor_row_id, apply_default=False)
    ```

    __Example__

    ``` python
    row_data = {
        "Name": "Ron"
    }
    base.insert_row('Table1', row_data, 'U_eTV7mDSmSd-K2P535Wzw')
    ```


## Update row

!!! question "Update row"

    Updates one row in a table.

    ``` python
    base.update_row(table_name, row_id, row_data)
    ```

    __Example__

    ``` python
    row_data = {
        "Name": "Ron"
    }
    base.update_row('Table1', 'U_eTV7mDSmSd-K2P535Wzw', row_data)
    ```

!!! question "Batch update rows"

    Updates multiple rows in a table.

    ``` python
    base.batch_update_rows(table_name, rows_data)
    ```

    __Example__

    ``` python
    rows_data = [{
        "row_id" : "fMmCFyoxT4GN5Y2Powbl0Q",
        "row" : {
            "Name" : "Ron",
            "Height" : "183"
            }
    }, {
        "row_id" : "cF5JTE99Tae-VVx0BGT-3A",
        "row" : {
            "Name" : "Richard",
            "Height" : "184"
            }
    }, {
        "row_id" : "WP-8rb5PSUaM-tZRmTOCPA",
        "row" : {
            "Name" : "Regina",
            "Heigt" : "173"
            }
    }]
    base.batch_update_rows('Table1', rows_data)
    ```
    

## Delete rows

!!! question "Delete row"

    Deletes one row from a table.

    ``` python
    base.delete_row(table_name, row_id)
    ```

    __Example__

    ``` python
    base.delete_row('Table1', 'U_eTV7mDSmSd-K2P535Wzw')
    ```

!!! question "Batch delete rows"

    Deletes multiple rows from a table.

    ``` python
    base.batch_delete_rows(table_name, row_ids)
    ```

    __Example__

    ``` python
    del_rows = rows[:3]
    row_ids = [row['_id'] for row in del_rows]
    base.batch_delete_rows('Table1', row_ids)
    ```
