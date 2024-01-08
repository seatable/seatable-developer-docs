# Table

!!! question "List tables"

    Get the active table.
    
    ``` python
    base.list_tables()
    ```
    
    __Example__
    ``` js
    tables = base.list_tables()
    ```

!!! question "Get a table by name"

    Get the active table.
    
    ``` python
    base.get_table_by_name(table_name)
    ```
    
    __Example__
    ``` js
    base.get_table_by_name('Table1')
    ```

!!! question "Add table"

    Add a table into a base.
    
    ``` python
    base.add_table(table_name, lang='en', columns=[]);
    ```
    
    __Example__
    ``` js
    base.add_table('Investigation', lang='zh-cn')
    ```

!!! question "Rename table"

    Add a table into a base.
    
    ``` python
    base.rename_table(table_name, new_table_name)
    ```
    
    __Example__
    ``` js
    base.rename_table('Table1', 'Table11')
    ```

!!! question "Delete table"

    Add a table into a base.
    
    ``` python
    base.delete_table(table_name)
    ```
    
    __Example__
    ``` js
    base.delete_table('Table1')
    ```
