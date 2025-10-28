# Rows

You'll find below all the available methods to interact with the rows of a SeaTable table. In this section, you'll have to deal with the **id** of the rows. You can find few tips on how to get it in [the user manual](https://seatable.com/help/was-ist-die-zeilen-id/).

{%
    include-markdown "includes.md"
    start="<!--rowstructure-start-->"
    end="<!--rowstructure-end-->"
%}

## Get row(s)

!!! abstract "get_row"

    Get a row from table `table_name` via its `row_id`.

    ``` python
    base.get_row(table_name, row_id)
    ```

    __Output__ Single row dict (throws an error if no table named `table_name` exists or if no row with the id `row_id` exists)
    
    __Example__
    
    ``` python
    from seatable_api import Base, context

    base = Base(context.api_token, context.server_url)
    base.auth()
    row = base.get_row('Table1', 'U_eTV7mDSmSd-K2P535Wzw')
    ```

!!! abstract "list_rows"

    Lists multiple rows of the table `table_name`. If `view_name` is provided, only the rows displayed in this specific view will be returned. The default `limit` is 1000 which is also the maximum number of rows this method returns. The query method (see below) offers more filter options and can return more rows.

    ``` python
    base.list_rows(table_name, view_name=None, start=None, limit=None) # (1)!
    ```

    1. `view_name` (optional): the name of the view you want to get the rows from. If there is no view named `view_name`, all the rows from table `table_name` will be eventually returned (depending on `start` and `limit`)

        `start` (optional): the index of the first rows you want to get (default is `0`)

        `limit` (optional): the maximum number of rows that should be returned (default is 1000, couldn't be higher)

    !!! warning "Mind the indexes!"
        In the SeaTable web interface, the row numbers, on the left, start at 1, whereas the `start` argument for the `base.list_rows` method starts at 0! This means that to get as first row the row numbered 10 in the web interface, you'll have to enter `start=9`.

    __Output__ List of row dicts (eventually empty if `start` is higher than the number of rows or if the view `view_name` is empty, throws an error if no table named `table_name` exists or if no view named `view_name` exists)
    
    __Example__
    
    ``` python
    from seatable_api import Base, context

    base = Base(context.api_token, context.server_url)
    base.auth()
    rows = base.list_rows('Table1')
    rows = base.list_rows('Table1', view_name='Default View', start=5, limit=20)
    ```

!!! abstract "query"

    Use SQL to query a base. SQL queries are the most powerful way access data stored in a base. If your not familiar with SQL syntax, we recommend using first the [SQL query plugin](https://seatable.com/help/anleitung-zum-sql-abfrage-plugin/). Most SQL syntax is supported, you can check the [SQL Reference](../../sql/reference.md) section of this manual for more information.

    ``` python
    base.query(sql_statement)
    ```

    Unless the SQL statement specifies a higher limit, the method returns a maximum of 100 rows. The maximum number of rows returned is 10000 no matter the limit specified in the SQL statement.

    !!! info "Backticks for table or column names containing or special characters or using reserved words"
    For SQL queries, you can use numbers, special characters or spaces in the names of your tables and columns. However, you'll **have to** escape these names with backticks in order for your query to be correctly interpreted, for example `` SELECT * FROM `My Table` ``. 

    Similarly, if some of your of table or column names are the same as [SQL function](./functions.md) names (for example a date-type column named `date`), you'll also **have to** escape them in order for the query interpreter to understand that it's not a function call missing parameters, but rather a table or column name.

    Similarly, if some of your of table or column names are the same as SQL function names (for example a date-type column named `date`), you'll also **have to** escape them in order for the query interpreter to understand that it's not a function call missing parameters, but rather a table or column name.

    __Output__ List of row dicts (eventually empty if no row match the request's conditions)

    All the examples below are related to a table **Bill** with the following structure/data:

    | name  | price | year  |
    | ----- | ----- | ----- |
    | Bob   | 300   | 2021  |
    | Bob   | 300   | 2019  |
    | Tom   | 100   | 2019  |
    | Tom   | 100   | 2020  |
    | Tom   | 200   | 2021  |
    | Jane  | 200   | 2020  |
    | Jane  | 200   | 2021  |


    __Example with a wildcard__

    === "Function call"

        ``` python
        import json
        from seatable_api import Base, context

        base = Base(context.api_token, context.server_url)
        base.auth()
        json_data = base.query('select * from Bill') # (1)!
        print(json.dumps(json_data, indent=' '))
        ```

        1. `*` means that you want to get the whole rows data (columns's values and specific row data such as id, etc.)

    === "Output"

        ``` json
        [
            {
                "name": "Bob",
                "price": 300,
                "year": 2021,
                "_locked": null,
                "_locked_by": null,
                "_archived": false,
                "_creator": "bd26d2b...82ca3fe1178073@auth.local",
                "_ctime": "2025-09-15T10:57:19.106+02:00",
                "_last_modifier": "bd26d2b...82ca3fe1178073@auth.local",
                "_mtime": "2025-09-18T09:52:00+02:00",
                "_id": "W77uzH1cSXu2v2UtqA3xSw"
            },
            {
                "name": "Bob",
                "price": 300,
                "year": 2019,
                "_locked": null,
                "_locked_by": null,
                "_archived": false,
                "_creator": "bd26d2b...82ca3fe1178073@auth.local",
                "_ctime": "2025-09-15T10:57:22.112+02:00",
                "_last_modifier": "bd26d2b...82ca3fe1178073@auth.local",
                "_mtime": "2025-09-18T09:52:00+02:00",
                "_id": "IxONgyDFQxmcDKpZWlQ9XA"
            },
            {
                "name": "Tom",
                "price": 100,
                "year": 2019,
                "_locked": null,
                "_locked_by": null,
                "_archived": false,
                "_creator": "bd26d2b...82ca3fe1178073@auth.local",
                "_ctime": "2025-09-15T10:57:23.4+02:00",
                "_last_modifier": "bd26d2b...82ca3fe1178073@auth.local",
                "_mtime": "2025-09-18T09:52:00+02:00",
                "_id": "K4LBuQ7aSjK9JwN14ITqvA"
            },
            {
                "name": "Tom",
                "price": 100,
                "year": 2020,
                "_locked": null,
                "_locked_by": null,
                "_archived": false,
                "_creator": "bd26d2b...82ca3fe1178073@auth.local",
                "_ctime": "2025-09-18T09:52:00+02:00",
                "_last_modifier": "bd26d2b...82ca3fe1178073@auth.local",
                "_mtime": "2025-09-18T09:52:00+02:00",
                "_id": "EHcQEaxiRzm3Zvq8B33bwQ"
            },
            {
                "name": "Tom",
                "price": 200,
                "year": 2021,
                "_locked": null,
                "_locked_by": null,
                "_archived": false,
                "_creator": "bd26d2b...82ca3fe1178073@auth.local",
                "_ctime": "2025-09-18T09:52:00+02:00",
                "_last_modifier": "bd26d2b...82ca3fe1178073@auth.local",
                "_mtime": "2025-09-18T09:52:00+02:00",
                "_id": "CjaCdBlNRXKkYkm231shqg"
            },
            {
                "name": "Jane",
                "price": 200,
                "year": 2020,
                "_locked": null,
                "_locked_by": null,
                "_archived": false,
                "_creator": "bd26d2b...82ca3fe1178073@auth.local",
                "_ctime": "2025-09-18T09:52:00+02:00",
                "_last_modifier": "bd26d2b...82ca3fe1178073@auth.local",
                "_mtime": "2025-09-18T09:52:00+02:00",
                "_id": "YzmUexIAR7iDWmhKGHgpMw"
            },
            {
                "name": "Jane",
                "price": 200,
                "year": 2021,
                "_locked": null,
                "_locked_by": null,
                "_archived": false,
                "_creator": "bd26d2b...82ca3fe1178073@auth.local",
                "_ctime": "2025-09-18T09:52:00+02:00",
                "_last_modifier": "bd26d2b...82ca3fe1178073@auth.local",
                "_mtime": "2025-09-18T09:52:00+02:00",
                "_id": "HJi7wbUMQIOuIlPaoO9Fbg"
            }
        ]
        ```

    __Example with WHERE__

    === "Function call 1 (filter by year)"

        ```python
        import json
        from seatable_api import Base, context

        base = Base(context.api_token, context.server_url)
        base.auth()
        json_data = base.query('select name, price from Bill where year = 2021')
        print(json.dumps(json_data, indent=' '))
        ```

    === "Output #1"

        ```json
        [
            {"name":"Bob","price":"300"},
            {"name":"Tom","price":"200"},
            {"name":"Jane","price":"200"}
        ]
        ```

    === "Function call 2 (filter by name)"

        ```python
        import json
        from seatable_api import Base, context

        base = Base(context.api_token, context.server_url)
        base.auth()
        json_data = base.query('select name, price, year from Bill where name = "Bob"')
        print(json.dumps(json_data, indent=' '))
        ```

    === "Output #2"

        ```json
        [
            {"name":"Bob","price":"300","year":"2021"},
            {"name":"Bob","price":"300","year":"2019"}
        ]
        ```


    __Example with GROUP BY__

    === "Function call"

        ```python
        import json
        from seatable_api import Base, context

        base = Base(context.api_token, context.server_url)
        base.auth()
        json_data = base.query('select name, sum(price) from Bill group by name')
        print(json.dumps(json_data, indent=' '))
        ```

    === "Output"

        ```json
        [
            {'name': 'Bob', 'SUM(price)': 600},
            {'name': 'Tom', 'SUM(price)': 400},
            {'name': 'Jane', 'SUM(price)': 400}
        ]
        ```

    __Example with DISTINCT__

    === "Function call"

        ```python
        import json
        from seatable_api import Base, context

        base = Base(context.api_token, context.server_url)
        base.auth()
        json_data = base.query('select distinct name from Bill')
        print(json.dumps(json_data, indent=' '))
        ```

    === "Output"

        ```json
        [
            {'name': 'Bob'},
            {'name': 'Tom'},
            {'name': 'Jane'}
        ]
        ```

## Add row(s)

!!! info "Dealing with default values"

    By default, the default values specified for the table columns in the web interface do **not** apply when adding/appending rows via Python scripts. In order to apply the default values, add `apply_default=True`as a function parameter. If set to `True`, the default values can be overwritten by specifying alternative values in `row_data`.

!!! abstract "append_row"

    Add a row to the table `table_name`. This row contains the data specified in the dict `row_data`. No row will be added if `row_data` is an empty dict (`{}`).empty or if it contains only keys that don't exist in the table.


    ``` python
    base.append_row(table_name, row_data, apply_default=False) # (1)!
    ```

    1. `row_data`: dict (pairs of `key`:`value`, each `key` being the name of a column), for example:

        ```
        {
            'First Name': 'John',
            'Last Name': 'Doe',
            'Invoice amount': 100,
            'Products': ['Office Supplies', 'Computer']
        }
        ```

        `apply_default` (optional): wether to use default values or not (default is `False`)

    !!! info "Creating an empty row"
        To create an empty row, specify a `row_data` dict containing at least one existing column of the table with an empty string as value, for example: `{'Name': ''}`

    __Output__ Single row dict (`None` if no row were added, throws an error if no table named `table_name` exists)

    __Example__
    
    ``` python
    from seatable_api import Base, context

    base = Base(context.api_token, context.server_url)
    base.auth()
    row_data = {
        "Name": "Ron"
    }

    row = base.append_row('Table1', row_data, apply_default=True)
    print(row)
    ```

!!! abstract "batch_append_rows"

    Append multiple rows to the table `table_name` at once. This function can't operate more than 1000 rows at once. If you need to deal with more than 1000 rows at once, please refer to the [common questions](../common_questions.md#dealing-with-more-than-1000-rows-at-once-with-batch-operations).

    ``` python
    base.batch_append_rows(table_name, rows_data, apply_default=False) # (1)!
    ```

    1. `rows_data`: list of `row_data` dict (see `base.append_row` above)

        `apply_default` (optional): wether to use default values or not (default is `False`)

    __Output__ Single dict object containing the number of new rows, the list of the ids of the created rows and the first row (see example output below); throws an error if no table named `table_name` exists
    
    __Example__
    
    === "Function call"

        ``` python
        from seatable_api import Base, context

        base = Base(context.api_token, context.server_url)
        base.auth()
        rows_data = [{
            'Name': 'Ron',
            'Birthday': '1975-01-01'
        }, {
            'Name': 'Richard',
            'Birthday': '1978-10-08'
        }]

        rows = base.batch_append_rows('Table1', rows_data)
        print(rows)
        ```

    === "Output"

        ```json
        {
           "inserted_row_count": 2, /* (1)! */
           "row_ids": [  /* (2)! */
              {
                "_id": "bglW5pKfQxG9D70hc693Wg"
              },
              {
                "_id": "Q3E3IJWrTQCjOOxjipM8jA"
              }
           ],
           "first_row": {  /* (3)! */
              "0000": "Ron",
              "1JGG": "1975-01-01",
              "_creator": "cc7a1d0fcec84bf9b36df5dcf5b65b99@auth.local",
              "_last_modifier": "cc7a1d0fcec84bf9b36df5dcf5b65b99@auth.local",
              "_id": "bglW5pKfQxG9D70hc693Wg",
              "_ctime": "2025-09-24T14:52:55.651+00:00",
              "_mtime": "2025-09-24T14:52:55.651+00:00"
           }
        }
        ```

        1. `inserted_row_count`: number of new rows

        2. `row_ids`: list of dicts, each containing a single `_id` key and the id of the corresponding created row as value

        3. `first_row`: the row dict of the first created row

!!! abstract "insert_row"

    Insert one row to the table `table_name` under an *anchor* row whose id is `anchor_row_id`. If no row with id `anchor_row_id` exists, the row is added to the end of the table (similar to `base.append_row` in ths case).

    ``` python
    base.insert_row(table_name, row_data, anchor_row_id, apply_default=False)
    ```

    __Output__ Single row dict (`None` if no row were added, throws an error if no table named `table_name` exists)

    __Example__
    
    ``` python
    from seatable_api import Base, context

    base = Base(context.api_token, context.server_url)
    base.auth()
    row_data = {
        "Name": "Ron"
    }
    row = base.insert_row('Table1', row_data, 'U_eTV7mDSmSd-K2P535Wzw')
    print(row)
    ```


## Update row(s)

!!! abstract "update_row"

    Update the row whose id is `row_id` in the table `table_name`. The `row_data` dict (pairs of `key`:`value`, each `key` being the name of a column) need to contain only the data you want to update. To reset a value, specify the `key`:`value` pair with an empty string `''`.

    ``` python
    base.update_row(table_name, row_id, row_data)
    ```

    __Output__ Dict containing a single `success` key with the result of the operation  (throws an error if no table named `table_name` exists or if no row with the id `row_id` exists)

    __Example__
    
    ``` python
    from seatable_api import Base, context

    base = Base(context.api_token, context.server_url)
    base.auth()
    row_data = {
        "Name": "Ron"
    }
    row_update = base.update_row('Table1', 'U_eTV7mDSmSd-K2P535Wzw', row_data)
    print(row_update)
    ```

!!! abstract "batch_update_rows"

    Updates multiple rows in the table `table_name` at once. This function can't operate more than 1000 rows at once. If you need to deal with more than 1000 rows at once, please refer to the [common questions](../common_questions.md#dealing-with-more-than-1000-rows-at-once-with-batch-operations).

    ``` python
    base.batch_update_rows(table_name, rows_data) # (1)!
    ```

    1. `rows_data`: list of dicts containing two `key`:`value` pairs:
     
        - `row_id`: the id of the row to update
        - `row`: the dict containing the row data to update (see `base.append_row` above)

    __Output__ Dict containing a single `success` key with the result of the operation  (throws an error if no table named `table_name` exists, if no row with the id `row_id` exists or if `rows_data` is wrong, for example with non-existing `row_id` value)
    
    __Example__
    
    ``` python
    from seatable_api import Base, context

    base = Base(context.api_token, context.server_url)
    base.auth()
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
            "Height" : "173"
            }
    }]
    row_update = base.batch_update_rows('Table1', rows_data)
    print(row_update)
    ```
    

## Delete row(s)

!!! abstract "delete_row"

    Delete a single row (whose id is `row_id`) from the table `table_name`.

    ``` python
    base.delete_row(table_name, row_id)
    ```

     __Output__ Dict containing a single `deleted_rows` key with the number of deleted rows (`0` if no row with id `row_id` exists, throws an error if no table named `table_name` exists)

    __Example__
    
    ``` python
    from seatable_api import Base, context

    base = Base(context.api_token, context.server_url)
    base.auth()
    base.delete_row('Table1', 'U_eTV7mDSmSd-K2P535Wzw')
    ```

!!! abstract "batch_delete_rows"

    Delete multiple rows from the table `table_name` at once. This function can't operate more than 1000 rows at once. If you need to deal with more than 1000 rows at once, please refer to the [common questions](../common_questions.md#dealing-with-more-than-1000-rows-at-once-with-batch-operations).

    ``` python
    base.batch_delete_rows(table_name, row_ids) # (1)!
    ```

    1. `row_ids`: list of the ids of the rows to delete

    __Output__ Dict containing a single `deleted_rows` key with the number of deleted rows (`0` if `row_ids` is an empty list, throws an error if no table named `table_name` exists)

    __Example__
    
    ``` python
    from seatable_api import Base, context

    base = Base(context.api_token, context.server_url)
    base.auth()
    # Retrieving the rows of table 'Table1'
    rows = base.list_rows('Table1')
    #Getting only the three first rows
    del_rows = rows[:3]
    # Creating a list of the ids from these three rows
    row_ids = [row['_id'] for row in del_rows]
    deletion_result = base.batch_delete_rows('Table1', row_ids)
    print(deletion_result)
    ```
