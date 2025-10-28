# Big data storage

## Insert rows into big data storage

!!! abstract "big_data_insert_rows"

    Batch insert rows into big data storage.

    ``` python
    base.big_data_insert_rows(table_name, rows_data)
    ```

    __Output__ Dict containing a single `inserted_row_count` key with the number of rows actually inserted in the big data storage.

    __Example__

    ``` python
    rows = [
            {'Name': "A"},
            {'Name': "B"}
        ]
    base.big_data_insert_rows('Table1', rows_data=rows)
    ```
