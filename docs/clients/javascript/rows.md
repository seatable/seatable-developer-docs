# Rows

## Get Rows

!!! question "listRows"

    ``` js
    base.listRows(table_name, view_name=None, order_by='', desc='', start='', limit='')
    ```

    __Example__
    ``` js
    const rows1 = await base.listRows('Table1')
    const rows2 = await base.listRows('Table1', view_name='default', order_by='年龄', desc=true, start=5, limit=20)
    ```

!!! question "getRow"

    ``` js
    base.getRow(table_name, row_id)
    ```

    __Example__
    ``` js
    const row = await base.getRow('Table1', 'U_eTV7mDSmSd-K2P535Wzw')
    ```

## Add Row(s)

!!! question "appendRow"

    ``` js
    base.appendRow(table_name, row_data)
    ```

    __Example__
    ``` js
    row_data = {
        "Name": "I am new Row"
    }

    await base.appendRow('Table1', row_data)
    ```

!!! question "insertRow"

    ``` js
    base.insertRow(table_name, row_data, anchor_row_id)
    ```

    __Example__
    ``` js
    const row_data = {
        "Name": "I am new Row"
    }

    await base.insertRow('Table1', row_data, 'U_eTV7mDSmSd-K2P535Wzw')
    ```

!!! question "batchAppendRows"

    ``` js
    base.batchAppendRows(table_name, rows_data)
    ```

    __Example__
    ``` js
    const rows_data = [{
                    'Name': 'test batch',
                    'content': 'Yes'
                }, {
                    'Name': 'test batch',
                    'content': 'Yes'
                }, {
                    'Name': 'test batch',
                    'content': 'Yes'
                }]
    await base.batchAppendRows('Table6', rows_data)
    ```

## Update Row

!!! question "updateRow"

    ``` js
    base.updateRow(table_name, row_id, row_data)
    ```

    __Example__
    ``` js
    row_data = {
        "Number": "123"
    }
    await base.updateRow('Table1', 'U_eTV7mDSmSd-K2P535Wzw', row_data)
    ```

!!! question "batchUpdateRows"

    ``` js
    base.batchUpdateRows(table_name, rows_data)
    ```

    __Example__
    ``` js
    const updates_data = [
            {
                "row_id": "fMmCFyoxT4GN5Y2Powbl0Q",
                "row": {
                    "Name": "Ranjiwei",
                    "age": "36"
                }
            },
            {
                "row_id": "cF5JTE99Tae-VVx0BGT-3A",
                "row": {
                    "Name": "Huitailang",
                    "age": "33"
                }
            },
            {
                "row_id": "WP-8rb5PSUaM-tZRmTOCPA",
                "row": {
                    "Name": "Yufeng",
                    "age": "22"
                }
            }
        ]
    await base.batchUpdateRows('Table1', rows_data=updates_data)
    ```

## Delete Row(s)

!!! question "deleteRow"

    ``` js
    base.deleteRow(table_name, row_id)
    ```

    __Example__
    ``` js
    await base.deleteRow('Table1', 'U_eTV7mDSmSd-K2P535Wzw')
    ```

!!! question "batchDeleteRows"

    ``` js
    base.batchDeleteRows(table_name, row_ids)
    ```

    __Example__
    ``` js
    const del_rows = rows.slice(0, 3);
    const row_ids = del_rows.map(row => row._id);
    await base.batchDeleteRows('Table1', row_ids)
    ```
