# Links

!!! question "getColumnLinkId"

````
Get the link id by column name.

```js
base.getColumnLinkId(tableName, columnName)
```

__Example__

```js
await base.getColumnLinkId('Table1', 'Record')
```
````

!!! question "getLinkedRecords"

````
List the linked records of rows. You can get the linked records of multiple rows.
``` js
base.getColumnLinkId(table_name, column_name)
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
base.updateLink(link_id, table_name, other_table_name, row_id, other_rows_ids)
```

__Example__
``` js
await base.updateLink(
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
````

!!! question "batchUpdateLinks"

````
Batch update infos of link-type columns
``` js
base.batchUpdateLinks(link_id, table_name, other_table_name, row_id_list, other_rows_ids_map)
```

__Example__
``` js
link_id = "WaW5"
table_name ="Table1"
other_table_name = "Table2"
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
base.getColumnLinkId(table_name, column_name)
```

__Example__
``` js
const linkId = await base.getColumnLinkId('LinkTable', 'Record') // return the link id such as 'aHL2'
```
````

### 