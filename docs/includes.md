<!--datamodel-start-->
As a developer you typically interact with a single base. In SeaTable, a base can contain multiple tables, each one containing multiple rows and columns (or fields) and eventually multiple views used to filter, sort and/or group these rows and columns. The logic is like this:

```sh
SeaTable Base
├─ Table 1 (Column A | Column B | Column C)
│  └─ View A (Column A | Column B | Column C)
|     └─ Row 1
|     └─ Row 2
|     └─ Row 3
|     └─ ...
│  └─ View B (Column A | Column C)
|     └─ Row 3
|     └─ Row 4
└─ Table 2
|  └─ ...
```

Every objects and methods will help you interact with this architecture. For details about the different objects (tables, view, rows & columns and links) you can look at the global structure presented in each object page or at the [SeaTable API Reference](https://api.seatable.com/reference/models) for even more information.
<!--datamodel-end-->

<!--tablestructure-start-->
## Global structure

Here is the global structure of a table object:
```js
{
    "_id": "IfcB",
    "name": "New table",
    "is_header_locked": false,
    "summary_configs": {},
    "columns": [ // (1)!
        {
        "key": "0000",
        "type": "number",
        "name": "First column",
        "editable": true,
        "width": 200,
        "resizable": true,
        "draggable": true,
        "data": null,
        "permission_type": "",
        "permitted_users": []
        },
        {
        "key": "2w6F",
        "type": "text",
        "name": "second column",
        "editable": true,
        "width": 200,
        "resizable": true,
        "draggable": true,
        "data": null,
        "permission_type": "",
        "permitted_users": []
        },
        {
        "key": "3aAf",
        "type": "date",
        "name": "third column",
        "editable": true,
        "width": 200,
        "resizable": true,
        "draggable": true,
        "data": null,
        "permission_type": "",
        "permitted_users": []
        }
    ],
    "rows": [], // (2)!
    "views": [ // (3)!
        {
        "_id": "0000",
        "name": "Default View",
        "type": "table",
        "is_locked": false,
        "filter_conjunction": "And",
        "filters": [],
        "sorts": [],
        "groupbys": [],
        "group_rows": [],
        "groups": [],
        "colorbys": {},
        "hidden_columns": [],
        "rows": [],
        "formula_rows": {},
        "link_rows": {},
        "summaries": {},
        "colors": {}
        }
    ],
    "id_row_map": {}
}
```

1.  Array of existing [columns](./columns.md#global-structure)
    ```js
    {
      "key": "g4s1",
      "type": "number",
      "name": "api3",
      "editable": true,
      "width": 200,
      "resizable": true,
      "draggable": true,
      "data": null,
      "permission_type": "",
      "permitted_users": []
    }
    ```

2.  Array of existing [rows](./rows.md#global-structure)
    ```js
    {
    "_id": "Qtf7xPmoRaiFyQPO1aENTjb",
    "_mtime": "2021-03-10T16:19:31.761+00:00",
    "Name": "NewName",
    "Date": "2020-08-01",
    "Content": "111",
    "link": [
                {
                "display_value": "1",
                "row_id": "XzdZfL2oS-aILnhfagTWEg"
                }
            ]
    }
    ```

3.  Array of existing [views](views.md#global-structure)
    ```js
    {
      "_id": "0000",
      "name": "Default View",
      "type": "table",
      "is_locked": false,
      "rows": [],
      "formula_rows": {},
      "summaries": [],
      "filter_conjunction": "And",
      "sorts": [],
      "filters": [],
      "hidden_columns": [],
      "groupbys": [],
      "group_rows": [],
      "groups": []
    }
    ```
Please refer to the [SeaTable API Reference](https://api.seatable.com/reference/models#table) for a more detailed presentation.

You can have a look at the specific [view](./views.md#global-structure), [column](./columns.md#global-structure) or [row](./rows.md#global-structure) structure on the corresponding pages.

<!--tablestructure-end-->

<!--viewstructure-start-->
## Global structure

Here is the global structure of a view object:

```js
{
    "_id": "0000",
    "name": "Default View",
    "type": "table",
    "is_locked": false,
    "rows": [],
    "formula_rows": {},
    "summaries": [],
    "filter_conjunction": "And",
    "sorts": [],
    "filters": [],
    "hidden_columns": [],
    "groupbys": [],
    "group_rows": [],
    "groups": []
}
```

Please refer to the [SeaTable API Reference](https://api.seatable.com/reference/models#view) for a more detailed presentation.
<!--viewstructure-end-->

<!--columnstructure-start-->
## Global structure

Here is the global structure of a column object:

```js
{
    "key":"bjcM",
    "type":"number",
    "name":"Val",
    "editable":true,
    "width":200,
    "resizable":true,
    "draggable":true,
    "data": // (1)!
        {
            "format":"number",
            "precision":2,
            "enable_precision":false,
            "enable_fill_default_value":false,
            "enable_check_format":false,
            "decimal":"comma",
            "thousands":"no",
            "format_min_value":0,
            "format_max_value":1000
        },
    "permission_type":"",
    "permitted_users":[],
    "permitted_group":[],
    "edit_metadata_permission_type":"",
    "edit_metadata_permitted_users":[],
    "edit_metadata_permitted_group":[],
    "description":null,
    "colorbys":{},
    "editor":
        {
            "key":null,
            "ref":null,
            "props":{},
            "_owner":null
        },
    "formatter":
        {
            "key":null,
            "ref":null,
            "props":{},
            "_owner":null
        }
}
```

1. See below for a presentation of `data` object keys depending on the column `type`

!!! warning "Columns particularities"

    - Unless other elements, columns don't have an `_id`, but a `key`
    - Link-type columns also have a link id that should not be mistaken with the column `key`. This value is present in the `data` object (see below)

### Column data

The `data` object keys will depend on the column `type` and will allow you to define the specific column parameters. Here is a list of the different `data` keys depending on the column `type`:

!!! note "`text`, `email`, `long-text`, `image`, `file`, `url`, `creator`, `ctime`, `last-modifier`, `mtime`"

    empty

??? note "`link`"

    ```
    {
        "display_column_key":"qqXZ",
        "table_id":"0000",
        "other_table_id":"XE5U",
        "is_internal_link":true,
        "is_multiple":true,
        "only_adding_new_record":false,
        "is_row_from_view":false,
        "other_view_id":"",
        "link_id":"OSD1",
        "array_type":"text",
        "array_data":null,
        "result_type":"array"
    }
    ```

??? note "`number`"

    ```
    {
        "format":"custom_currency",
        "precision":2,
        "enable_precision":true,
        "enable_fill_default_value":false,
        "decimal":"comma",
        "thousands":"no",
        "currency_symbol_position":"after",
        "currency_symbol":"p"
    }
    ```

??? note "`date`"

    ```
    {
        "format":"M/D/YYYY HH:mm"
    }
    ```

??? note "`duration`"

    ```
    {
        "format":"duration",
        "duration_format":"h:mm"
    }
    ```

??? note "`single select, multiple select`"

    ```
    {
        "options":
            [
                {
                    "name":"Male",
                    "id":"783482",
                    "color":"#46A1FD",
                    "textColor":"#FFFFFF",
                    "borderColor":"#3C8FE4"
                },
                {
                    "name":"Female",
                    "id":"330935",
                    "color":"#DC82D2",
                    "textColor":"#FFFFFF",
                    "borderColor":"#D166C5"
                },
                {
                    "name":"Non-binary",
                    "id":"147140",
                    "color":"#ADDF84",
                    "textColor":"#FFFFFF",
                    "borderColor":"#9CCF72"
                }
            ],
            "cascade_column_key":"Qvkt",
            "cascade_settings":
                {
                    "147140":["783482"],
                    "330935":["330935"],
                    "783482":["783482"]
                }
    }
    ```

??? note "`checkbox`"

    ```
    {
        "default_value":false,
        "enable_fill_default_value":false
    }
    ```

??? note "`rate`"

    ```
    {
        "rate_max_number":5,
        "rate_style_color":"#FF8000",
        "default_value":"",
        "enable_fill_default_value":false
    }
    ```

??? note "`formula`"

    ```
    {
        "formula":"left({Email},search(\"@\",{Email},1)-1)",
        "operated_columns":["JfP2"],
        "result_type":"string",
        "enable_precision":true,
        "precision":1,
        "thousands":"no"
    }
    ```

??? note "`link-formula`"

    ```
    {
        "formula":"findmax",
        "result_type":"array",
        "operated_columns":["TaXD"],
        "conditions":[],
        "link_column_key":"TaXD",
        "include_condition":false,
        "condition_conjunction":"And",
        "column_key_in_linked_record":"0000",
        "column_key_for_comparison":"RSjx",
        "level2_linked_table_column_key":null,
        "array_type":"auto-number",
        "array_data":null
    }
    ```

??? note "`geolocation`"

    ```
    {
        "geo_format":"lng_lat"
    }
    ```

??? note "`auto-number`"

    ```
    {
        "format":"YYYYMMDD-00",
        "max_used_auto_number":33,
        "digits":2,
        "prefix_type":"date",
        "prefix":"20250909"
    }
    ```

??? note "`button`"

    ```
    {
        "button_type":"copy_row_to_another_table",
        "button_name":"Copy to Table2",
        "button_color":"#FFFCB5",
        "table_id":"0000"
    }
    ```

!!! info "Accessing a particular data object value"

    This rather long list is not exhaustive, however. If you need to access a specific `data` value, consult the [SeaTable API Reference](https://api.seatable.com/reference/models#row--column) or create the corresponding column to display the content of its `data` object.

<!--columnstructure-end-->

<!--rowstructure-start-->
## Global structure

Here is the global structure of a row object:
```js
{
  "_id": "Qtf7xPmoRaiFyQPO1aENTjb",
  "_mtime": "2021-03-10T16:19:31.761+00:00",
  "Name": "NewName",
  "Date": "2020-08-01",
  "Content": "111",
  "link": [
            {
              "display_value": "1",
              "row_id": "XzdZfL2oS-aILnhfagTWEg"
            }
          ]
}
```

Please note the specific format for link-type columns (structure of the array objects for key `link`):

- `display_value`: Value displayed in the cell

- `row_id`: id of the linked row in the other table

<!--rowstructure-end-->

<!--add-row-example-start-->
# Add rows

This script adds two expenses rows in a ledger. Before adding them, it checks if they have already been added for the current month.

Here is the structure of the table named `Daily expenses` you need so that this script could run:

| Column name | Name | Date | Type | Type (single select) | Fee |
| ----------- |: ------ :|: ------ :|: ------ :|: ---------------------- :|: ----- :|
| **Column type**  |  text   |   date  |  text  |   single select    |     number           |
<!--add-row-example-end-->

<!--accumulated-value-example-start-->
# Calculate accumulated value

This script accumulates the values of the current row and the previous rows, and records the result to the current row. It does the same than the *Calculate accumulated value* operation from the data processing menu. If there's a grouping rule active on the view, accumulated values will be calculated for each group.Otherwise, values are accumulated for all rows. Please not that this script only supports **grouping by a single column**.

 Here is the structure of the table named `Accumulated value` you need so that this script could run:

| Column name | Value to add | Incremental total | Grouping column |
| ----------- |: ------ :|: ------ :|: ------ :|
| **Column type**  |  number   |   number  |  single select  |
<!--accumulated-value-example-end-->

<!--attendance-statistics-example-start-->
# Compute attendance statistics

This script computes, from a list of clocking times, daily clock in (earliest clocking) and clock out (latest clocking) times for each day and staff member.

Here is the structure of the table named `Clocking table` that contains the input data:

| Column name | Name | Department | Date | Clocking time |
| ----------- |: ------ :|: ------ :|: ------ :|: ------ :|
| **Column type**  |  text   |   single select  |  date  | duration |

And the structure of the table `Attendance statistics` where the daily summarized values will be stored:

| Column name | Name | Department | Date | Clock-in | Clock-out |
| ----------- |: ------ :|: ------ :|: ------ :|: ------ :|: ------ :|
| **Column type**  |  text   |   single select  |  date  | duration | duration |
<!--attendance-statistics-example-end-->