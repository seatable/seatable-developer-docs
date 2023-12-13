# Rows

Interact with the rows of a SeaTable base.

## Get rows

!!! question "getRows"

    Get all the rows of the view and return an array.

    ``` js
    base.getRows(table: Object/String, view: Object/String);
    ```

    __Examples__

    ``` js
    const table = base.getTableByName('Table1');
    const view = base.getViewByName(table, 'view1');
    const rows = base.getRows(table, view);
    ```

    ``` js
    const rows = base.getRows('Table1', 'view1');
    ```

!!! question "query"

    Use sql to query a base. SQL-Query is the most powerful function to the data from a base. Most SQL-syntax is support.

    ``` js
    await base.query(sql)
    ```

    __Example: Get everything with a wildcard__

    ``` js
    const data = await base.query('select * from Bill')
    output.text(data) // (1)!
    ```

    1.  Returns for example the following:
        ```
        [
            {"name":"Bob","price":"300","year":"2021"},
            {"name":"Bob","price":"300","year":"2019"},
            {"name":"Tom","price":"100","year":"2019"},
            {"name":"Tom","price":"100","year":"2020"},
            {"name":"Tom","price":"200","year":"2021"},
            {"name":"Jane","price":"200","year":"2020"},
            {"name":"Jane","price":"200","year":"2021"}
        ]
        ```

    __Example: WHERE__

    ``` js
    const data = await base.query('select name, price from Bill where year = 2021')
    output.text(data) // (1)!

    const data = await base.query('select name, price from Bill where name = "Bob"')
    output.text(data) // (2)!
    ```

    1.  Returns for example the following:
        ```
        [
            {"name":"Bob","price":"300"},
            {"name":"Tom","price":"200"},
            {"name":"Jane","price":"200"}
        ]
        ```
    2.  Returns for example the following:
        ```
        [
            {"name":"Bob","price":"300","year":"2021"},
            {"name":"Bob","price":"300","year":"2019"}
        ]
        ```


    __Example: GROUP BY__

    ``` js
    const data = await base.query('select name, sum(price) from Bill group by name')
    output.text(data) // (1)!
    ```

    1.  Returns for example the following:
        ```
        [
            {'SUM(price)': 600, 'name': 'Bob'},
            {'SUM(price)': 400, 'name': 'Tom'},
            {'SUM(price)': 400, 'name': 'Jane'}
        ]
        ```

    __Example: DISTINCT__

    ``` js
    const data = await base.query('select distinct name from Bill')
    output.text(data) // (1)!
    ```

    1.  Returns for example the following:
        ```
        [
            {'SUM(price)': 600, 'name': 'Bob'},
            {'SUM(price)': 400, 'name': 'Tom'},
            {'SUM(price)': 400, 'name': 'Jane'}
        ]
        ```

!!! question "getGroupedRows"

    Get rows in the grouped view.

    ``` js
    base.getGroupedRows(table: Object/String, view: Object/String);
    ```

    __Example__

    ``` js
    const table = base.getTableByName('Table1');
    const view = base.getViewByName(table, 'GroupedView');
    const groupViewRows = base.getGroupedRows(table, view);
    ```

    ``` js
    const groupViewRows = base.getGroupedRows('Table1', 'GroupedView');
    ```

!!! question "getRowById"

    Get a `row` via its `id` and return a row object.

    ``` js
    base.getRowById(table: Object/String, rowId: String);
    ```

    __Examples__

    ``` js
    const table = base.getTableByName('Table1');
    const row = base.getRowById(table, "M_lSEOYYTeuKTaHCEOL7nw");
    ```

    ``` js
    const row = base.getRowById('Table1', "M_lSEOYYTeuKTaHCEOL7nw");
    ```

## Delete row

!!! question "deleteRowById"

    Delete a `row` in a table by its `id`.

    ``` js
    base.deleteRowById(table: Object/String, rowId: String);
    ```

    __Examples__

    ``` js
    const table = base.getTableByName('Table1');
    base.deleteRowById(table, 'M_lSEOYYTeuKTaHCEOL7nw');
    ```

    ``` js
    base.deleteRowById('Table1', 'M_lSEOYYTeuKTaHCEOL7nw');
    ```

## Add row

!!! question "addRow"

    Add a row to a table.

    ``` js
    base.addRow(table: Object/String, rowData: Object, viewName?: String)
    ```

    __Examples__

    ``` js
    const table = base.getTableByName('Table1');
    base.addRow(table, {'Name': 'Alex', 'Age': '18'});
    base.addRow(table, {'Name': 'Alex', 'Age': '18'}, 'Default View');
    ```

    ``` js
    base.addRow('Table1', {'Name': 'Alex', 'Age': '18'});
    base.addRow('Table1', {'Name': 'Alex', 'Age': '18'}, 'Default View');
    ```

## Update row(s)

!!! question "modifyRow"

    Modify a row in the table.

    ``` js
    base.modifyRow(table: Object/String, row: Object, updateRowData: Object);
    ```

    __Examples__

    ``` js
    const table = base.getTableByName('Table1');
    const row = base.getRowById(table, "M_lSEOYYTeuKTaHCEOL7nw");
    base.modifyRow(table, row, {'Name': 'new name', 'number': 100});
    ```

    ``` js
    const row = base.getRowById('Table1', "M_lSEOYYTeuKTaHCEOL7nw");
    base.modifyRow('Table1', row, {'Name': 'new name', 'number': 100});
    ```

!!! question "modifyRows"

    Modify multiple rows in the table at once.

    ``` js
    base.modifyRow(table: Object/String, rows: Array, updatedRows: Array);
    ```

    __Example__

    ``` js
    const table = base.getTableByName('Table1');
    const rows = base.getRows('Table1', 'Default view');
    const selectedColumnName = 'Name';
    const selectedRows = [], updatedRows = [];

    rows.forEach((row) => {
    if (row[columnName] === 'name') {
        selectedRows.push(row);
        updatedRows.push({columnName: 'name1'});
    }
    });
    base.modifyRow(table, selectedRows, updatedRows);
    ```

## Filter

`base.filter` allows to pass a conditional statement. It filters the rows that meet the conditions in the table, and returns a querySet object.

!!! question "filter"

    ``` js
    base.filter(tableName, viewName, filterExpression)
    ```

    __Example__

    ``` js
    // Filter out rows whose number column is equal to 5, and return a querySet object
    const querySet = base.filter('Table1', 'Default', 'number = 5');
    ```

### Filter Expressions

!!! question "filter expressions"

    The table query will become simpler and more efficiency by using the sql-like statements as a paramter in `base.filter()` function. In different column types, there are a little differences in the query method and the format of input statement. These are the available __query methods__:

    * **greater-less query:**  >， >， =， \<， \<=
    * **equal-unequal query:**  =,  \<>
    * **computation:** +, -, *, /, ^, %

    Here is an example based on the code `queryset = base.filter("Table1", "age>18")`

    * age: column name
    * \>: operator
    * 18: parameter

    | Data structure | Column type                               | Format of greater-less query                                | Format of equal-unequal query                       | computation |
    | -------------- | ----------------------------------------- | ----------------------------------------------------------- | --------------------------------------------------- | :---------- |
    | String         | Text, Long Text, URL,Email, Single Select | Unsupported                                                 | String                                              | Unsupported |
    | List           | Multiple Select                           | Unsupported                                                 | String                                              | Unsupported |
    | Number         | Number                                    | int, float                                                  | int, float, and empty string ""                     | Supported   |
    | Date           | Date, Created time,  Last modified time   | Patterns: YYYY-MM-DD, YYYY-MM-DD hh:mm, YYYY-MM-DD hh\:mm:ss | Same patterns as greater-less query                 | Unsupported |
    | Boolean        | Checkbox                                  | Unsupported                                                 | true, false and empty string "", (case-insensitive) | Unsupported |

    ---

    Here are more examples of the different filter expressions pending of the column type.

    __String-based Column__

    Column types include **Text, Long Text, URL, Email, Checkbox**.

    ```python
    # 1. equal-unequal query
    base.filter('Table1', 'view_name', "column_name=hello world")
    base.filter('Table1', 'view_name', "column_name!=''")

    ```

    __List-based Column__

    Column types include **Multiple Select**

    ```python
    # equal-unequal query
    base.filter('Table1','view_name', "column_name=A and column_name=B") # Find the rows which contains both 'A' and 'B'

    ```

    __Number-based Column__

    1. Column types include **Number**

    ```javascript
    # 1. greater-less query
    base.filter('Table1', 'view_name', "column_name>18")
    base.filter('Table1', 'view_name', "column_name>-10 and column_name<=0")

    # 2. equal-unequal query
    base.filter('Table1', 'view_name',"column_name<>20")
    base.filter('Table1', 'view_name', "column_name=0")
    base.filter('Table1', 'view_name',"column_name=''")

    ```

    2. Computation

    ```javascript
    base.filter('Table1', 'view_name', "column_name+3>18")
    base.filter('Table1', 'view_name', "column_name*2=18")
    base.filter('Table1', 'view_name', "column_name-2=18")
    base.filter('Table1', 'view_name', "column_name/2=18")
    base.filter('Table1', 'view_name', "column_name^2=18")
    base.filter('Table1', 'view_name', "column_name%2=1")
    ```

    __Date-based Column__

    Column types include **Date, Created time, Last modified time**

    ```javascript
    # 1. greater-less query
    base.filter('Table1', 'view_name', "column_name>'2020-1-30'")
    base.filter('Table1', 'view_name', "column_name>='2019-1-1 5:30' and column_name<='2019-5-1 6:00'")

    # 2. equal-unequal query
    base.filter('Table1', 'view_name', "column_name='2020-1-1 10:59:59'")
    base.filter('Table1', 'view_name', "column_name!=''")

    ```

    !!! note "Note that please use the quotes "" when making the date-time query"

    __Boolean-based Column__

    Column types include **Checkbox**

    ```javascript
    # equal-unequal query
    base.filter('Table1', 'view_name','column_name=False') # Same as base.filter('Table1', "column_name=''")
    base.filter('Table1', 'view_name', "column_name=True")

    ```

### Filter Queries

The return value of the `base.filter` function, this object provides some methods to simplify the operation of the filtered data

!!! question "filter"

    Pass a conditional statement, filter out the rows that meet the conditions in the table, and return a querySet object.

    ``` js
    base.filter(table: Object/String, ??, condition: ??)
    ```

    __Example__

    ``` js
    // Filter out rows whose number column is equal to 5, and return a querySet object
    const querySet = base.filter('Table1', 'Default', 'number = 5');
    ```

!!! tip "all"

    Returns all filtered data in the form of a list

    ``` js
    querySet.all(linkId, tableName, linkedTableName, rowId, updatedlinkedRowIds)
    ```

    __Example__

    ``` js
    const list = querySet.all();
    ```

!!! tip "count"

    Returns the number of filtered rows

    __Example__

    ```js
    const count = querySet.count();
    ```

!!! tip "last"

    Return the last filtered data

    __Example__

    ```js
    const row = querySet.last();
    ```

!!! tip "first"

    Return the first filtered data

    __Example__

    ```js
    const row = querySet.first();
    ```

!!! tip "delete"

    Delete all filtered rows and return the number of successfully deleted

    __Example__

    ```js
    const count = querySet.delete();
    ```

!!! tip "update"

    Modify the row data and return the updated data

    __Example__

    ```js
    // Modify the contents of the Name column of all filtered rows to xxxx
    const rows = querySet.update({Name: 'xxxx'});
    ```

!!! tip "filter"

    Further filtering, return a querySet object

    __Example__

    ```js
    // Filter out the rows with the value of Tom in the Name column of the querySe
    const querySet1 = querySet.filter('Name = "Tom"');
    ```

!!! tip "get"

    Get a piece of data in the querySet that meets the conditions, and return a row

    __Example__

    ```js
    // Get the first data of Tom in the Name column of the querySet
    const row = querySet.get('Name = "Tom"');
    ```
