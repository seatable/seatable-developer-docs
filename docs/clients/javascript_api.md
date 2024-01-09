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

#### Get metadata

Get base metadata information

```javascript
base.getMetadata();
```

##### Example

```javascript
const metadata = await base.getMetadata();
```

Return

```javascript
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

####  Get tables

List table infos in a base

```javascript
base.getTables()
```

##### Example

```javascript
const tables = await base.getTables();
```

####  Get table by name

```javascript
base.getTableByName(table_name);
```

##### Example

```javascript
const table = await base.getTableByName('Table1')
```

#### Add table

Add a table to a base

```javascript
base.addTable(table_name, lang='en')
```

* lang：language，default by English ('en') , and Chinese is also supported ('zh-cn')

##### Example

```javascript
await base.addTable('项目调查表', lang='zh-cn')
```

####  Rename table

```javascript
base.renameTable(old_name, new_name)
```

##### Example

```javascript
await base.renameTable('Table_Add1', 'New_Table_Add1');
```

####  Delete table

```javascript
base.deleteTable(table_name)
```

##### Example

```javascript
await base.deleteTable('Table1')
```



### Views

#### List views

```javascript
base.listViews(table_name)
```

##### Example

```javascript
const views = await base.listViews('Table1')
```

#### Get a view by name

Example

```javascript
base.getViewByName(table_name, view_name);
```

##### Example

```javascript
const view = await base.getViewByName('Table1', 'MyView');
```

#### Add view

```javascript
base.addView(table_name, new_view_name);
```


##### Example

```javascript
await base.addView('Table1', 'new_view');
```

#### Raname view

```javascript
base.renameView(table_name, view_name, new_view_name);
```

##### Example

```javascript
await base.renameView('Table1', 'myView', 'myView-01');
```

#### Delete view

```javascript
base.deleteView(table_name, view_name);
```

##### Example

```javascript
await base.deleteView('Table1', 'MyView');
```



### Rows

#### List rows

Get all rows of the table

```javascript
base.listRows(table_name, view_name=None, order_by='', desc='', start='', limit='')
```

* order_by:  column name based on which ordering the data
* start: start position of rows
* limit:  number of rows returned

##### Example

```javascript
const rows1 = await base.listRows('Table1')
const rows2 = await base.listRows('Table1', view_name='default', order_by='年龄', desc=true, start=5, limit=20)
```

#### Get row

Get a row of the table by row ID.

```javascript
base.getRow(table_name, row_id)
```

##### Example

```javascript
const row = await base.getRow('Table1', 'U_eTV7mDSmSd-K2P535Wzw')
```

#### Append row

Append a row

```javascript
base.appendRow(table_name, row_data)
```

##### Example

```javascript
row_data = {
    "Name": "I am new Row"
}

await base.appendRow('Table1', row_data)
```

#### Insert row

Insert a row

```javascript
base.insertRow(table_name, row_data, anchor_row_id)
```

* anchor_row_id: the row under which the new row will be inserted

##### Example

```javascript
row_data = {
    "Name": "I am new Row"
}

await base.insertRow('Table1', row_data, 'U_eTV7mDSmSd-K2P535Wzw')
```

#### Batch append rows

Batch append rows

```javascript
base.batchAppendRows(table_name, rows_data)
```

##### Example

```javascript
rows_data = [{
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

#### Update row

Update a row

```javascript
base.updateRow(table_name, row_id, row_data)
```

##### Example

```javascript
row_data = {
    "dcXS": "123"
}
await base.updateRow('Table1', 'U_eTV7mDSmSd-K2P535Wzw', row_data)
```

#### Batch update rows

Batch update rows

```javascript
base.batchUpdateRows(table_name, rows_data)
```

##### Example

```javascript
updates_data = [
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

#### Delete row

Delete a row

```javascript
base.deleteRow(table_name, row_id)
```

##### Example

```javascript
await base.deleteRow('Table1', 'U_eTV7mDSmSd-K2P535Wzw')
```

#### Batch delete rows

Batch delete rows

```javascript
base.batchDeleteRows(table_name, row_ids)
```

##### Example

```javascript
const del_rows = rows.slice(0, 3);
const row_ids = del_rows.map(row => row._id);
await base.batchDeleteRows('Table1', row_ids)
```



### Column

#### List columns

List all rows of the table/view

```javascript
base.listColumns(table_name, view_name='')
```

##### Example

```javascript
const columns1 = await base.listColumns('Table1')
const columns2 = await base.listColumns('Table1', view_name='default')
```

#### Get columns by name

```javascript
base.getColumnByName(table_name, column_name);
```

##### Example

```javascript
const col = await base.getColumnsByName('Table1', 'Name');
```

#### Get columns by type

```javascript
base.getColumnsByType(table_name, col_type);
```

##### Example

```javascript
const cols = await base.getColumnsByType('Table1', 'number')
```

#### Insert column

Insert/Append column

```javascript
base.insertColumn(table_name, column_name, column_type, column_key='', column_data='')
```

* column_key: the key of column after which the new column will be inserted, it will be appended to the last column by default
* column_data: config info of column, required for link-type column, optional for other type columns

##### Example

```javascript
import { ColumnTypes } from 'seatable-api';
await base.insertColumn('Table1', 'seatable-api', ColumnTypes.TEXT)
await base.insertColumn('Table1', 'seatable-api', ColumnTypes.TEXT, '0000')
await base.insertColumn('Table1', 'Link1', ColumnTypes.LINK, column_data={
        'table':'Table1',
        'other_table':'Test_User'
    })
```

#### Rename column

Rename a column

```javascript
base.renameColumn(table_name, column_key, new_column_name)
```

##### Example

```javascript
await base.renameColumn('Table1', 'kSiR', 'new-seatable-api')
```

#### Resize column

Set a column width

```javascript
base.resizeColumn(table_name, column_key, new_column_width)
```

##### Example

The default width of a column is 200, if you need to adjust the column width, such as 500

```javascript
await base.resizeColumn('Table1', 'asFV', 500)
```

#### Freeze column

Freeze a column

```javascript
base.freezeColumn(table_name, column_key, frozen)
```

frozen: true/false

##### Example

```javascript
await base.freezeColumn('Table1', '0000', true)
```

#### Move column

```javascript
base.moveColumn(table_name, column_key, target_column_key)
```

* column_key:  the key of the column you want to move

* target_column_key:  is the key of the anchor column, the moved column will be moved to the right of the column

##### Example

```javascript
await base.moveColumn('Table1', 'loPx', '0000')
```

In this example, the 'loPx' column will be moved to the right of the '0000' column

#### Modify column type

Transform a column type

```javascript
base.modifyColumnType(table_name, column_key, new_column_type)
```

##### Example

```javascript
import { ColumnTypes } from 'seatable-api';

await base.modifyColumnType('Table1', 'nePI', ColumnTypes.NUMBER)
```

#### Add column options

Used by single-select or multiple-select type columns

```javascript
base.addColumnOptions(table_name, column, options)
```

##### Example

```javascript
await base.addColumnOptions('Table1', 'My choices', [
        {"name": "ddd", "color": "#aaa", "textColor": "#000000"},
        {"name": "eee", "color": "#aaa", "textColor": "#000000"},
        {"name": "fff", "color": "#aaa", "textColor": "#000000"},
])
```

#### Add column cascade settings

Used by single-select column, to add a limitation of child column options according to the option of parent column

```javascript
base.addColumnCascadeSettings(table_name, child_column, parent_column, cascade_settings)
```

* child_column: name of child column
* parent_column: name of parent column

##### Example

```javascript
await base.addColumnCascadeSettings("Table1", "single-op-col-c", "single-op-col", {
  "aaa": ["aaa-1", "aaa-2"], # If “aaa” is selected by parent column, the available options of child column are "aaa-1 and aaa-2"
  "bbb": ["bbb-1", "bbb-2"],
  "ccc": ["ccc-1", "ccc-2"]
})
```

#### Delete column

Delete a column

```javascript
base.deleteColumn(table_name, column_key)
```

##### Example

```javascript
await base.deleteColumn('Table1', 'bsKL')
```



### Links

#### Get linked records

List the linked records of rows. You can get the linked records of multiple rows.

```javascript
base.getLinkedRecords(table_id, link_column_key, rows)
```

* table_id: the id of link table
* link_column_key: the column key of the link column of link table ( not link_id )
* rows: a list, each item of the which contains a row info including row_id, offset (defualt by 0) and limit (default by 10) of link table

##### Example

```javascript
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

#### Add link

Add links, link other table records

```javascript
base.addLink(link_id, table_name, other_table_name, row_id, other_row_id)
```

* link_id:  link_id in the data attribute of the link column
* table_name: the name of the link table
* other_table_name: the name of the linked table
* row_id: id of link row
* other_row_id: id of the linked row 

##### Example

```javascript
await base.addLink('5WeC', 'real-img-files', 'contact', 'CGtoJB1oQM60RiKT-c5J-g', 'PALm2wPKTCy-jdJNv_UWaQ')
```

#### Update link

Modify the info of link-type column

```
base.updateLink(link_id, table_id, other_table_id, row_id, other_rows_ids)
```

* link_id:  link_id in the data attribute of the link column
* table_id: the id of the link table
* other_table_id:  the id of the linked table
* row_id:   id of link row
* other_rows_ids: ids of the linked row 


##### Example

```javascript
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

#### Batch update links

Batch update infos of link-type columns

```javascript
base.batchUpdateLinks(link_id, table_id, other_table_id, row_id_list, other_rows_ids_map)
```

##### Example

```javascript
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

#### Remove link

Delete the link row

```javascript
base.removeLink(link_id, table_name, other_table_name, row_id, other_row_id)
```

##### Example

```javascript
await base.removeLink('5WeC', 'real-img-files', 'contact', 'CGtoJB1oQM60RiKT-c5J-g', 'PALm2wPKTCy-jdJNv_UWaQ')
```

#### Get link id

Get the link id by column name

```javascript
base.getColumnLinkId(columns, column_name)
```

##### Example

```javascript
const columns = await base.listColumns('Table1'); // return table's columns
const linkId = await base.getColumnLinkId(columns, 'Record') // return the link id such as 'aHL2'
```



### Query with SQL

#### Query

Use sql to query a base

```javascript
base.query(sql)
```

* sql: sql statement

**Note: Only 100 results will be returned by default. To get more results, add `limit` in SQL statement.**

Possible exceptions

* ValueError: sql can not be empty
* ConnectionError: network error
* Exception: no such table
* Exception: no such column
* Exception: columns in group by should match columns in select

#### Example

##### Basic

```javascript
await base.query('select name, price, year from Bill')
```

Result

```javascript
[
    {'_id': 'PzBiZklNTGiGJS-4c0_VLw', 'name': 'Bob', 'price': 300, 'year': 2019},
    {'_id': 'Ep7odyv1QC2vDQR2raMvSA', 'name': 'Bob', 'price': 300, 'year': 2021},
    {'_id': 'f1x3X_8uTtSDUe9D60VlYQ', 'name': 'Tom', 'price': 100, 'year': 2019},
    {'_id': 'NxeaB5pDRFKOItUs_Ugxug', 'name': 'Tom', 'price': 100, 'year': 2020},
    {'_id': 'W0BrjGQpSES9nfSytvXgMA', 'name': 'Tom', 'price': 200, 'year': 2021},
    {'_id': 'EvwCWtX3RmKYKHQO9w2kLg', 'name': 'Jane', 'price': 200, 'year': 2020},
    {'_id': 'BTiIGSTgR06UhPLhejFctA', 'name': 'Jane', 'price': 200, 'year': 2021}
]
```

##### WHERE

```javascript
await base.query('select name, price from Bill where year = 2021 ')
```

Result

```javascript
[
    {'_id': 'Ep7odyv1QC2vDQR2raMvSA', 'name': 'Bob', 'price': 300},
    {'_id': 'W0BrjGQpSES9nfSytvXgMA', 'name': 'Tom', 'price': 200},
    {'_id': 'BTiIGSTgR06UhPLhejFctA', 'name': 'Jane', 'price': 200}
]
```


##### ORDER BY

```javascript
await base.query('select name, price, year from Bill order by year')
```

结果

```javascript
[
    {'_id': 'PzBiZklNTGiGJS-4c0_VLw', 'name': 'Bob', 'price': 300, 'year': 2019},
    {'_id': 'f1x3X_8uTtSDUe9D60VlYQ', 'name': 'Tom', 'price': 100, 'year': 2019},
    {'_id': 'NxeaB5pDRFKOItUs_Ugxug', 'name': 'Tom', 'price': 100, 'year': 2020},
    {'_id': 'EvwCWtX3RmKYKHQO9w2kLg', 'name': 'Jane', 'price': 200, 'year': 2020},
    {'_id': 'Ep7odyv1QC2vDQR2raMvSA', 'name': 'Bob', 'price': 300, 'year': 2021},
    {'_id': 'W0BrjGQpSES9nfSytvXgMA', 'name': 'Tom', 'price': 200, 'year': 2021},
    {'_id': 'BTiIGSTgR06UhPLhejFctA', 'name': 'Jane', 'price': 200, 'year': 2021}
]
```

##### GROUP BY

```javascript
await base.query('select name, sum(price) from Bill group by name')
```

Result

```javascript
[
    {'SUM(price)': 600, 'name': 'Bob'},
    {'SUM(price)': 400, 'name': 'Tom'},
    {'SUM(price)': 400, 'name': 'Jane'}
]
```


##### DISTINCT

```javascript
await base.query('select distinct name from Bill')
```

Result

```javascript
[
    {'_id': 'PzBiZklNTGiGJS-4c0_VLw', 'name': 'Bob'},
    {'_id': 'f1x3X_8uTtSDUe9D60VlYQ', 'name': 'Tom'},
    {'_id': 'EvwCWtX3RmKYKHQO9w2kLg', 'name': 'Jane'}
]
```



### Constants

In the script there may be some constants we need to know

#### ColumnTypes

Column type, when insert/add columns, change column types, etc. need to be used

```javascript
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

