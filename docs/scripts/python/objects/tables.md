# Table

!!! question "add_table"

    Add a table into a base.

    ``` python
    base.add_table(table_name, lang='en', columns=[]);
    ```

    __Example__
    ``` js
    const new_table = base.add_table('New Tasks', lang='en', [{'name': 'Name', 'type': 'text'},{'name': 'Address', 'type': 'text'}]);
    output.text(`New table added: ${table.name}`);
    ```

!!! question "getActiveTable"

    Get the active table.

    ``` python
    base.getActiveTable();
    ```

    __Example__
    ``` js
    const table = base.getActiveTable();
    output.text(`The name of the active table is: ${table.name}`);
    ```
