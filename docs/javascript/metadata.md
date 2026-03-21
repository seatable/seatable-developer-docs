# Metadata

!!! abstract "getMetadata"

    Get the complete structure of a base -- tables, views, and columns. Does not include row data.

    ``` js
    base.getMetadata();
    ```json

    __Example output__
    ```json
    {
        "tables": [{
            "_id": "4krH",
            "name": "Contact",
            "is_header_locked": false,
            "columns": [{
                "key": "0000",
                "type": "text",
                "name": "Name",
                "editable": true,
                "width": 200
            }],
            "views": [{
                "_id": "0000",
                "name": "Default view",
                "type": "table",
                "is_locked": false,
                "filters": [],
                "sorts": [],
                "groupbys": [],
                "hidden_columns": []
            }]
        }]
    }
    ```
