# Big data storage

!!! question "Insert rows into big data storage"

    Batch insert rows into big data storage.

    ``` python
    base.big_data_insert_rows(table_name, rows_data)
    ```

    __Example__

    ``` python
    rows = [
            {'Name': "A"},
            {'Name': "B"}
        ]
    base.big_data_insert_rows('Table1', rows_data=rows)
    ```
