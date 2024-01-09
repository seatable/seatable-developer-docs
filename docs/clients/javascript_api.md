# JavaScript API

JavaScript API encapsulates SeaTable Server Restful API. You can call it in your front-end page or Node.js program.

!!! Danger "JavaScript API cannot be used for scripts in SeaTable bases. For script programming with Javascript, there is a [separate chapter](/scripts/) in this documentation."

## Installation

```shell
npm install seatable-api
```

## Reference

To use SeaTable APIs, you should first initialize a base object and call `base.auth()`. `base.auth()` is an async function, which needs to be executed in async functions. Other APIs all return a promise object. There are two ways to use them

The first way:

```
base.listViews(tableName).then(views => {
  // Use views to complete the requirements
}).catch(error => {
  // Exception handling
})
```

The second way:

```
try {
  const views = await base.listViews(tableName);
  // Use views to complete the requirements
} catch (error) {
  // Exception handling
}
```

SeaTable API Errors

- 400 Params invalid
- 403 Permission denied
- 413 exceed limit
- 500 Internal Server Error



## Base API

Base represents a table. You can use the api token of the form to obtain the authorization to read and write the base. This token can be generated directly on the web side.


### Get authorization

Use the API Token of the base to get access authorization.

##### Example

```javascript
import { Base } from 'seatable-api';

const config = {
  server: 'https://cloud.seatable.cn',
  APIToken: 'c3c75dca2c369849455a39f4436147639cf02b2d'
};

const base = new Base(config);
await base.auth()
```

### Metadata

!!! question "getMetadata"

    Get the complete metadata of a table. The metadata will not contain the concrete rows of the table.
    
    ``` js
    base.getMetadata();
    ```
    
    Example result of this call.
    
    ```
    {
        'tables': [{
            '_id': '4krH',
            'name': 'Contact',
            'is_header_locked': False,
            'columns': [{
                'key': '0000',
                'type': 'text',
                'name': 'Name',
                'editable': True,
                'width': 200,
                'resizable': True,
                'draggable': True,
                'data': None,
                'permission_type': '',
                'permitted_users': []
            }, {
                'key': 'M31F',
                'type': 'text',
                'name': 'Email',
                'editable': True,
                'width': 200,
                'resizable': True,
                'draggable': True,
                'data': None,
                'permission_type': '',
                'permitted_users': []
            }],
            'views': [{
                '_id': '0000',
                'name': 'Default view',
                'type': 'table',
                'is_locked': False,
                'filter_conjunction': 'And',
                'filters': [],
                'sorts': [],
                'groupbys': [],
                'group_rows': [],
                'groups': [],
                'colorbys': {},
                'hidden_columns': [],
                'rows': [],
                'formula_rows': {},
                'link_rows': {},
                'summaries': {},
                'colors': {}
            }]
        }]
    }
    ```

### Table

!!! question "getTables"    

    ``` js
    base.getTables()
    ```
    
    __Example__
    ``` js
    const tables = await base.getTables();
    ```

!!! question "getTableByName"

````
``` js
base.getTableByName(table_name);
```

__Example__
``` js
const table = await base.getTableByName('Table1')
```
````

!!! question "addTable"

````
``` js
base.addTable(table_name, lang='en', columns=[])
```

__Example__
``` js
await base.addTable('Investigation', lang='en')
```
````

!!! question "renameTable

````
``` js
base.renameTable(old_name, new_name)
```

__Example__
``` js
await base.renameTable('Table_Add1', 'New_Table_Add1');
```
````

!!! question "deleteTable"

````
``` js
base.deleteTable(table_name)
```

__Example__
``` js
await base.deleteTable('Table1')
```
````

### Views

!!! question "listViews"

````
``` js
base.listViews(table_name)
```

__Example__
``` js
const views = await base.listViews('Table1')
```
````

!!! question "getViewByName"

````
``` js
base.getViewByName(table_name, view_name);
```

__Example__
``` js
const view = await base.getViewByName('Table1', 'MyView');
```
````

!!! question "addView"

````
``` js
base.addView(table_name, new_view_name);
```

__Example__
``` js
await base.addView('Table1', 'new_view');
```
````

!!! question "renameView"

````
``` js
base.renameView(table_name, view_name, new_view_name);
```

__Example__
``` js
await base.renameView('Table1', 'myView', 'myView-01');
```
````

!!! question "deleteView"

````
``` js
base.deleteView(table_name, view_name);
```

__Example__
``` js
await base.deleteView('Table1', 'MyView');
```
````



### Rows

!!! question "listRows"

````
``` js
base.listRows(table_name, view_name=None, order_by='', desc='', start='', limit='')
```

__Example__
``` js
const rows1 = await base.listRows('Table1')
const rows2 = await base.listRows('Table1', view_name='default', order_by='年龄', desc=true, start=5, limit=20)
```
````

!!! question "getRow"

````
``` js
base.getRow(table_name, row_id)
```

__Example__
``` js
const row = await base.getRow('Table1', 'U_eTV7mDSmSd-K2P535Wzw')
```
````

!!! question "appendRow"

````
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
````

!!! question "insertRow"

````
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
````

!!! question "batchAppendRows"

````
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
````

!!! question "updateRow"

````
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
````

!!! question "batchUpdateRows"

````
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
````

!!! question "deleteRow"

````
``` js
base.deleteRow(table_name, row_id)
```

__Example__
``` js
await base.deleteRow('Table1', 'U_eTV7mDSmSd-K2P535Wzw')
```
````

!!! question "batchDeleteRows"

````
``` js
base.batchDeleteRows(table_name, row_ids)
```

__Example__
``` js
const del_rows = rows.slice(0, 3);
const row_ids = del_rows.map(row => row._id);
await base.batchDeleteRows('Table1', row_ids)
```
````



### Column

!!! question "listColumns"

````
``` js
base.listColumns(table_name, view_name='')
```

__Example__
``` js
const columns1 = await base.listColumns('Table1')
const columns2 = await base.listColumns('Table1', view_name='default')
```
````

!!! question "getColumnByName"

````
``` js
base.getColumnByName(table_name, column_name);
```

__Example__
``` js
const col = await base.getColumnsByName('Table1', 'Name');
```
````

!!! question "getColumnsByType"

````
``` js
base.getColumnsByType(table_name, col_type);
```

__Example__
``` js
const cols = await base.getColumnsByType('Table1', 'number')
```
````

!!! question "insertColumn"

````
``` js
base.insertColumn(table_name, column_name, column_type, column_key='', column_data='')
```

__Example__
``` js
import { ColumnTypes } from 'seatable-api';
await base.insertColumn('Table1', 'seatable-api', ColumnTypes.TEXT)
await base.insertColumn('Table1', 'seatable-api', ColumnTypes.TEXT, '0000')
await base.insertColumn('Table1', 'Link1', ColumnTypes.LINK, column_data={
        'table':'Table1',
        'other_table':'Test_User'
    })
```
````

!!! question "renameColumn"

````
``` js
base.renameColumn(table_name, column_key, new_column_name)
```

__Example__
``` js
await base.renameColumn('Table1', 'kSiR', 'new-seatable-api')
```
````

!!! question "resizeColumn"

````
``` js
base.resizeColumn(table_name, column_key, new_column_width)
```

__Example__
``` js
await base.resizeColumn('Table1', 'asFV', 500)
```
````

!!! question "freezeColumn"

````
``` js
base.freezeColumn(table_name, column_key, frozen)
```

__Example__
``` js
await base.freezeColumn('Table1', '0000', true)
```
````

!!! question "moveColumn"

````
``` js
base.moveColumn(table_name, column_key, target_column_key)
```

__Example__
In this example, the 'loPx' column will be moved to the right of the '0000' column
``` js
await base.moveColumn('Table1', 'loPx', '0000')
```
````

!!! question "modifyColumnType"

````
``` js
base.modifyColumnType(table_name, column_key, new_column_type)
```

__Example__
``` js
import { ColumnTypes } from 'seatable-api';
await base.modifyColumnType('Table1', 'nePI', ColumnTypes.NUMBER)
```
````

!!! question "addColumnOptions"

````
Used by single-select or multiple-select type columns
``` js
base.addColumnOptions(table_name, column, options)
```

__Example__
``` js
await base.addColumnOptions('Table1', 'My choices', [
        {"name": "ddd", "color": "#aaa", "textColor": "#000000"},
        {"name": "eee", "color": "#aaa", "textColor": "#000000"},
        {"name": "fff", "color": "#aaa", "textColor": "#000000"},
])
```
````

!!! question "addColumnCascadeSettings"

````
Used by single-select column, to add a limitation of child column options according to the option of parent column
``` js
base.addColumnCascadeSettings(table_name, child_column, parent_column, cascade_settings)
```

__Example__
``` js
await base.addColumnCascadeSettings("Table1", "single-op-col-c", "single-op-col", {
  "aaa": ["aaa-1", "aaa-2"], # If “aaa” is selected by parent column, the available options of child column are "aaa-1 and aaa-2"
  "bbb": ["bbb-1", "bbb-2"],
  "ccc": ["ccc-1", "ccc-2"]
})
```
````

!!! question "deleteColumn"

````
``` js
base.deleteColumn(table_name, column_key)
```

__Example__
``` js
await base.deleteColumn('Table1', 'bsKL')
```
````

### Links

!!! question "getLinkedRecords"

````
List the linked records of rows. You can get the linked records of multiple rows.
``` js
base.getLinkedRecords(table_id, link_column_key, rows)
```

__Example__
``` js
await base.getLinkedRecords('0000', '89o4', [
  {'row_id': 'FzNqJxVUT8KrRjewBkPp8Q', 'limit': 2, 'offset': 0},
  {'row_id': 'Jmnrkn6TQdyRg1KmOM4zZg', 'limit': 20}
])

// a key-value data structure returned as below
// key: row_id of link table
// value: a list which includes the row info of linked table
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
````

!!! question "addLink"

````
Add links, link other table records
``` js
base.addLink(link_id, table_name, other_table_name, row_id, other_row_id)
```

__Example__
``` js
await base.addLink('5WeC', 'real-img-files', 'contact', 'CGtoJB1oQM60RiKT-c5J-g', 'PALm2wPKTCy-jdJNv_UWaQ')
```
````

!!! question "updateLink"

````
Modify the info of link-type column
``` js
base.updateLink(link_id, table_id, other_table_id, row_id, other_rows_ids)
```

__Example__
``` js
await base.updateLink(
        link_id='r4IJ',
        table_id='0000',
        other_table_id='kFoO',
        row_id='BXhEm9ucTNu3FjupIk7Xug',
        other_rows_ids=[
          'exkb56fAT66j8R0w6wD9Qg',
          'DjHjwmlRRB6WgU9uPnrWeA'
        ]
    )
```
````

!!! question "batchUpdateLinks"

````
Batch update infos of link-type columns
``` js
base.batchUpdateLinks(link_id, table_id, other_table_id, row_id_list, other_rows_ids_map)
```

__Example__
``` js
link_id = "WaW5"
table_id ="0000"
other_table_id = "jtsf"
row_id_list = ["fRLglslWQYSGmkU7o6KyHw","eSQe9OpPQxih8A9zPXdMVA","FseN8ygVTzq1CHDqI4NjjQ"]
other_rows_ids_map = {
    	"FseN8ygVTzq1CHDqI4NjjQ":["OcCE8aX8T7a4dvJr-qNh3g","JckTyhN0TeS8yvH8D3EN7g"],
    	"eSQe9OpPQxih8A9zPXdMVA":["cWHbzQiTR8uHHzH_gVSKIg","X56gE7BrRF-i61YlE4oTcw"],
    	"fRLglslWQYSGmkU7o6KyHw":["MdfUQiWcTL--uMlrGtqqgw","E7Sh3FboSPmfBlDsrj_Fhg","UcZ7w9wDT-uVq4Ohtwgy9w"]
}

await base.batchUpdateLinks(link_id, table_id, other_table_id, row_id_list, other_rows_ids_map)
```
````

!!! question "removeLink"

````
``` js
base.removeLink(link_id, table_name, other_table_name, row_id, other_row_id)
```

__Example__
``` js
await base.removeLink('5WeC', 'real-img-files', 'contact', 'CGtoJB1oQM60RiKT-c5J-g', 'PALm2wPKTCy-jdJNv_UWaQ')
```
````

!!! question "removeLink"

````
``` js
base.getColumnLinkId(columns, column_name)
```

__Example__
``` js
const columns = await base.listColumns('Table1'); // return table's columns
const linkId = await base.getColumnLinkId(columns, 'Record') // return the link id such as 'aHL2'
```
````

### Query with SQL

!!! question "query"

````
Use sql to query a base
``` js
base.query(sql)
```

__Example: BASIC__
``` js
await base.query('select name, price, year from Bill')
```
Returns for example the following:
[
    {'_id': 'PzBiZklNTGiGJS-4c0_VLw', 'name': 'Bob', 'price': 300, 'year': 2019},
    {'_id': 'Ep7odyv1QC2vDQR2raMvSA', 'name': 'Bob', 'price': 300, 'year': 2021},
    {'_id': 'f1x3X_8uTtSDUe9D60VlYQ', 'name': 'Tom', 'price': 100, 'year': 2019},
    {'_id': 'NxeaB5pDRFKOItUs_Ugxug', 'name': 'Tom', 'price': 100, 'year': 2020},
    {'_id': 'W0BrjGQpSES9nfSytvXgMA', 'name': 'Tom', 'price': 200, 'year': 2021},
    {'_id': 'EvwCWtX3RmKYKHQO9w2kLg', 'name': 'Jane', 'price': 200, 'year': 2020},
    {'_id': 'BTiIGSTgR06UhPLhejFctA', 'name': 'Jane', 'price': 200, 'year': 2021}
]

__Example: WHERE__

``` js
await base.query('select name, price from Bill where year = 2021 ')
```
Returns for example the following:
[
    {'_id': 'Ep7odyv1QC2vDQR2raMvSA', 'name': 'Bob', 'price': 300},
    {'_id': 'W0BrjGQpSES9nfSytvXgMA', 'name': 'Tom', 'price': 200},
    {'_id': 'BTiIGSTgR06UhPLhejFctA', 'name': 'Jane', 'price': 200}
]

__Example: ORDER BY__

``` js
await base.query('select name, price, year from Bill order by year')
```
Returns for example the following:
[
    {'_id': 'PzBiZklNTGiGJS-4c0_VLw', 'name': 'Bob', 'price': 300, 'year': 2019},
    {'_id': 'f1x3X_8uTtSDUe9D60VlYQ', 'name': 'Tom', 'price': 100, 'year': 2019},
    {'_id': 'NxeaB5pDRFKOItUs_Ugxug', 'name': 'Tom', 'price': 100, 'year': 2020},
    {'_id': 'EvwCWtX3RmKYKHQO9w2kLg', 'name': 'Jane', 'price': 200, 'year': 2020},
    {'_id': 'Ep7odyv1QC2vDQR2raMvSA', 'name': 'Bob', 'price': 300, 'year': 2021},
    {'_id': 'W0BrjGQpSES9nfSytvXgMA', 'name': 'Tom', 'price': 200, 'year': 2021},
    {'_id': 'BTiIGSTgR06UhPLhejFctA', 'name': 'Jane', 'price': 200, 'year': 2021}
]


__Example: GROUP BY__

``` js
await base.query('select name, sum(price) from Bill group by name')
```
Returns for example the following:
[
    {'SUM(price)': 600, 'name': 'Bob'},
    {'SUM(price)': 400, 'name': 'Tom'},
    {'SUM(price)': 400, 'name': 'Jane'}
]

__Example: DISTINCT__

``` js
await base.query('select distinct name from Bill')
```
Returns for example the following:
[
    {'_id': 'PzBiZklNTGiGJS-4c0_VLw', 'name': 'Bob'},
    {'_id': 'f1x3X_8uTtSDUe9D60VlYQ', 'name': 'Tom'},
    {'_id': 'EvwCWtX3RmKYKHQO9w2kLg', 'name': 'Jane'}
]
````

### Constants

In the script there may be some constants we need to know

!!! question "ColumnTypes"

````
Column type, when insert/add columns, change column types, etc. need to be used
``` js
import { ColumnTypes } from 'seatable-api';

ColumnTypes.NUMBER              // number
ColumnTypes.TEXT                // text
ColumnTypes.LONG_TEXT           // long text
ColumnTypes.CHECKBOX            // checkbox
ColumnTypes.DATE                // date & time
ColumnTypes.SINGLE_SELECT       // single select
ColumnTypes.MULTIPLE_SELECT     // multiple 
ColumnTypes.IMAGE               // image
ColumnTypes.FILE                // file
ColumnTypes.COLLABORATOR        // collaborator
ColumnTypes.LINK                // link to 
ColumnTypes.FORMULA             // formula
ColumnTypes.CREATOR             // creator
ColumnTypes.CTIME               // create time
ColumnTypes.LAST_MODIFIER       // last modifier
ColumnTypes.MTIME               // modify time
ColumnTypes.GEOLOCATION         // geolocation
ColumnTypes.AUTO_NUMBER         // auto munber
ColumnTypes.URL                 // URL
```
````

