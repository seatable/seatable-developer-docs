# Tables

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

### 