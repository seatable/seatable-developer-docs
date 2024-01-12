# Tables

## Get Table(s)

!!! question "getTables"

    ``` js
    base.getTables()
    ```

    __Example__
    ``` js
    const tables = await base.getTables();
    ```

!!! question "getTableByName"

    ``` js
    base.getTableByName(tableName);
    ```

    __Example__
    ``` js
    const table = await base.getTableByName('Table1')
    ```

## Add Table

!!! question "addTable"

    ``` js
    base.addTable(tableName: String, lang='en', columns=[])
    ```

    __Example__
    ``` js
    await base.addTable('Investigation', lang='en')
    ```

## Rename Table

!!! question "renameTable"

    ``` js
    base.renameTable(oldNname: String, newName: String)
    ```

    __Example__
    ``` js
    await base.renameTable('Table1', 'Projects 2023');
    ```

## Delete Table

!!! question "deleteTable"

    ``` js
    base.deleteTable(tableName)
    ```

    __Example__
    ``` js
    await base.deleteTable('Table1')
    ```
