# Predefined objects in SeaTable (Javascript)

## Base object

Base object provide a way to read, manipulate and output data in/from your base. The following methods are available.

### Table

??? question "getActiveTable"

    Get the currently selected table and return a table object.

    ``` js
    base.getActiveTable();
    ```

    __Example__
    ``` js
    const table = base.getActiveTable();
    output.text(`The name of the active table is: ${table.name}`);
    ```

??? question "getTables"

    Get all tables of this base as `json` object with all rows and metadata.

    ```
    base.getTables();
    ```

    __Example__
    ``` js
    const tables = base.getTables();
    output.text(tables);
    ```

??? question "getTableByName"

    Get a table object by its name. The object contains all rows and metadata.
    ``` js
    base.getTableByName(tableName: String);
    ```

    __Example__
    ``` js
    const table = base.getTableByName('Table1');
    output.text(`The id of the table is: ${table._id}`);
    ```

??? question "addTable"

    Add a new table to this base. The table should not exist already in your base.

    ``` js
    base.addTable(tableName: String);
    ```

    __Example__
    ``` js
    base.addTable('New table');
    output.text("Wow, I just added a new table to this base.")
    ```

??? question "renameTable"

    Rename an existing table.

    ``` js
    base.renameTable(oldName: String, newName: String);
    ```

    __Example__
    ``` js
    const old_name = "Table1";
    const new_name = "Projects 2023";
    base.renameTable(old_name, new_name);
    output.text(`This base ${old_name} got a new name: ${new_name}`);
    ```

??? question "deleteTable"

    Delete a table from the base. By the way, the table can be [restored from the logs](https://seatable.io/docs/arbeiten-in-tabellen/eine-geloeschte-tabelle-wiederherstellen/?lang=auto).

    ``` js
    base.deleteTable(tableName: String);
    ```

    __Example__
    ``` js
    base.deleteTable('Old table');
    ```

### View

??? question "getActiveView"

    Get the current view, the method return a view object.

    ``` js
    base.getActiveView();
    ```

    __Example__
    ``` js
    const view  = base.getActiveView();
    output.text(view._id);
    output.text(view);
    ```

??? question "getViews"

    Get all the views of the current table, and return all the views in an array

    ``` js
    base.getViews(table: Object/String);
    ```

    __Example__
    ``` js
    const table  = base.getTableByName('Table1');
    const views = base.getViews(table);
    output.text(views.length);
    ```

??? question "getViewByName"

    Get a view object via its name, and return a view object.

    ``` js
    base.getViewByName(table: Object/String, viewName: String);
    ```

    __Examples__
    ``` js
    const table  = base.getTableByName('Table1');
    const view = base.getViewByName(table, 'view 1');
    output.text(view.name);
    ```

    ``` js
    const view = base.getViewByName('Table1', 'view 1');
    output.text(view.name);
    ```

??? question "addView"

    Add a view to a table.

    ``` js
    base.addView(table: Object/String, viewName: String);
    ```

    __Examples__
    ``` js
    const table  = base.getTableByName('Table1');
    base.addView(table, 'view 2');
    ```

    ``` js
    base.addView('Table1', 'view 2');
    ```

??? question "renameView"

    Rename a view in the table.

    ``` js
    base.renameView(table: Object/String, currentViewName: String, nextViewName: String);
    ```

    __Examples__
    ``` js
    const table  = base.getTableByName('Table1');
    base.renameView(table, 'view1', 'view2');
    ```

    ``` js
    base.renameView('Table1', 'view1', 'view2');
    ```

??? question "deleteView"

    Delete a view.

    ``` js
    base.deleteView(table: Object/String, viewName: String);
    ```

    __Examples__
    ``` js
    const table  = base.getTableByName('Table1');
    base.deleteView(table, 'view2');
    ```

    ``` js
    base.deleteView('Table1', 'view2');
    ```

### Column

??? question "getColumns"

    Get all the columns in the table, and return all the column objects in an array.

    ``` js
    base.getColumns(table: Object/String);
    ```

    __Examples__
    ``` js
    const table  = base.getTableByName('Table1');
    const columns = base.getColumns(table);

    column.forEach((column) => {
        output.text(column.name);
    })
    ```

    ``` js
    const columns = base.getColumns('Table1');
    ```

??? question "getShownColumns"

    Get all the displayed columns in a view, excluding the hidden columns in the view, and return an array.

    ``` js
    base.getShownColumns(table: Object/String, view: Object/String);
    ```

    __Examples__
    ``` js
    const table  = base.getTableByName('Table1');
    const view = base.getViewByName(table, 'view 1');
    const columns = base.getShownColumns(table, view);
    column.forEach((column) => {
        output.text(column.name);
    })
    ```

    ``` js
    const columns = base.getShownColumns('Table1', 'view 1');
    ```

??? question "getColumnByName"

    Get the column object via its name.

    ``` js
    base.getColumnByName(table: Object/String, name: String);
    ```

    __Examples__
    ``` js
    const column = base.getColumnByName(table, 'Column name');
    output.text(column.name);
    ```

    ``` js
    const column = base.getColumnByName('Table1', 'Column name');
    ```

??? question "getColumnsByType"

    Get all specific types of columns in the table.

    ``` js
    const columns = base.getColumnsByType(table: Object/String, type: String);
    ```

    __Examples__
    ``` js
    const table  = base.getTableByName('Table1');
    const columns = base.getColumnsByType(table, 'text');
    output.text(column.length);
    ```

    ``` js
    const columns = base.getColumnsByType('Table1', 'text');
    output.text(column.length);
    ```

### Row

??? question "getRows"

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

??? question "query"

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

??? question "getGroupedRows"

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

??? question "getRowById"

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

??? question "deleteRowById"

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

??? question "addRow"

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

??? question "modifyRow"

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

??? question "modifyRows"

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

??? question "filter"

    Pass a conditional statement, filter out the rows that meet the conditions in the table, and return a querySet object.

    ``` js
    base.filter(table: Object/String, ??, condition: ??)
    ```

    __Example__

    ``` js
    // Filter out rows whose number column is equal to 5, and return a querySet object
    const querySet = base.filter('Table1', 'Default', 'number = 5');
    ```

### Links

??? question "addLink"

    Add link, link other table records. Get more information about linking columns from the [SeaTable API Reference](https://api.seatable.io/reference/create-row-link).

    ``` js
    base.addLink(linkId, tableName, linkedTableName, rowId, linkedRowId)
    ```

    __Example__

    ``` js
    base.addLink('5WeC', 'Table1', 'Table2', 'CGtoJB1oQM60RiKT-c5J-g', 'PALm2wPKTCy-jdJNv_UWaQ')
    ```

??? question "removeLink"

    Delete the link row.

    ``` js
    base.removeLink(linkId, tableName, linkedTableName, rowId, linkedRowId)
    ```

    __Example__

    ``` js
    base.removeLink('5WeC', 'Table1', 'Table2', 'CGtoJB1oQM60RiKT-c5J-g', 'PALm2wPKTCy-jdJNv_UWaQ')
    ```

??? question "getColumnLinkId"

    Get the link id by column name.

    ``` js
    base.getColumnLinkId(tableName, columnName)
    ```

    __Example__

    ``` js
    base.getColumnLinkId('Table1', 'Record')
    ```

??? question "updateLinks"

    Remove all existing row links and add new links.

    ``` js
    base.updateLinks(linkId, tableName, linkedTableName, rowId, updatedlinkedRowIds)
    ```

    __Example__

    ``` js
    const rows = base.getRows('contact', 'Default_view');
    // Update row links to [rows[0]._id, rows[1]._id, rows[2]._id, rows[3]._id]
    base.updateLinks('5WeC', 'Table1', 'Table2', 'CGtoJB1oQM60RiKT-c5J-g', [rows[0]._id, rows[1]._id, rows[2]._id, rows[3]._id])
    ```

### Filter

`base.filter` allows to pass a conditional statement. It filters the rows that meet the conditions in the table, and returns a querySet object.

??? question "filter"

    ``` js
    base.filter(tableName, viewName, filterExpression)
    ```

    __Example__

    ``` js
    // Filter out rows whose number column is equal to 5, and return a querySet object
    const querySet = base.filter('Table1', 'Default', 'number = 5');
    ```

??? question "filter expressions"

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

## Queryset

The return value of the `base.filter` function, this object provides some methods to simplify the operation of the filterd data

??? tip "all"

    Returns all filtered data in the form of a list

    ``` js
    querySet.all(linkId, tableName, linkedTableName, rowId, updatedlinkedRowIds)
    ```

    __Example__

    ``` js
    const list = querySet.all();
    ```

??? tip "count"

    Returns the number of filtered rows

    __Example__

    ```js
    const count = querySet.count();
    ```

??? tip "last"

    Return the last filtered data

    __Example__

    ```js
    const row = querySet.last();
    ```

??? tip "first"

    Return the first filtered data

    __Example__

    ```js
    const row = querySet.first();
    ```

??? tip "delete"

    Delete all filtered rows and return the number of successfully deleted

    __Example__

    ```js
    const count = querySet.delete();
    ```

??? tip "update"

    Modify the row data and return the updated data

    __Example__

    ```js
    // Modify the contents of the Name column of all filtered rows to xxxx
    const rows = querySet.update({Name: 'xxxx'});
    ```

??? tip "filter"

    Further filtering, return a querySet object

    __Example__

    ```js
    // Filter out the rows with the value of Tom in the Name column of the querySe
    const querySet1 = querySet.filter('Name = "Tom"');
    ```

??? tip "get"

    Get a piece of data in the querySet that meets the conditions, and return a row

    __Example__

    ```js
    // Get the first data of Tom in the Name column of the querySet
    const row = querySet.get('Name = "Tom"');
    ```

---

## Base Utility functions

Utility functions help you to work with data in SeaTable.

### Date and Time

??? success "formatDate"

    Format date to 'YYYY-MM-DD' to be used in a date column.

    ``` js
    base.utils.formatDate(date: date object)
    ```

    __Example__
    ``` js
    let date = new Date();
    let formatDate = base.utils.formatDate(date);
    output.text(formatDate);
    ```

??? success "formatDateWithMinutes"

    Format date to 'YYYY-MM-DD HH:mm' to be used in a date column..

    ``` js
    base.utils.formatDateWithMinutes(date: date object)
    ```

    __Example__
    ``` js
    let date = new Date();
    let formatDate = base.utils.formatDateWithMinutes(date);
    output.text(formatDate);
    ```

### Lookup and Query

??? success "lookupAndCopy"

    Similar to the vlookup function in Excel. Find a matching row in the source table for each row of the target table, and then copy the data of the specified cell of the matching row to the specified cell of the target row.

    | Name | Email |
    | ---  | --- |
    | Hulk | greenbigboy@stark-industries.movie |
    | Tony | ironman|stark-industries.movie |

    The target table only has the user names but we want to copy the email address from the source table to the target table, then this function can be used.

    | Name | Email |
    | ---  | --- |
    | Hulk | |
    | Tony | |

    ``` js
    base.utils.lookupAndCopy(targetTable, targetColumn, targetColumnToCompare, sourceTableName, sourceColumnName, sourceColumnToCompare = null);
    ```

    __Example__

    ``` js
    // Match the rows with the same content in the Name column of Table1 and Table2, copy the contents of the Email column of the row in Table1 to the Email column of the corresponding row in Table2
    base.utils.lookupAndCopy('Table2', 'Email', 'Name', 'Table1', 'Name');

    // Match the rows with the same content in the Name column in Table1 and the Name1 column in Table2, and copy the contents of the Email column of the row in Table1 to the Email1 column of the corresponding row in Table2
    base.utils.lookupAndCopy('Table2', 'Email1', 'Name1', 'Table1', 'Email', 'Name');

    ```

??? success "query"

    Filter and summary the table data by SQL like statements.

    ``` js
    base.utils.query(tableName: String, viewName: String, query: String);
    ```

    __Example__

    ``` js
    // Filter out the rows where the sum of the three columns 'number', 'number1', and 'number2' is greater than 5 then sum the number and number2 columns in these rows, return {number: 12, number2: 23}
    base.utils.query('Table1', 'View_name', 'select sum(number), sum(number2) where number + number1 + number2 > 5');
    ```

---

## Output

Output object supports output strings in text or Markdown format.

??? quote "text"

    Prints the content of the passed variable as normal text. Code Syntax is ignored and just printed.

    ``` js
    output.text(anything: String/Object/Array)
    ```

    __Example__

    ``` js
    const table = base.getActiveTable();
    output.text(table.name);
    ```

??? quote "markdown"

    Prints the content of the passed variable. Markdown formating is used to style the output.

    ``` js
    output.markdown(anything: String/Object/Array)
    ```

    __Example__

    ``` js
    const table = base.getActiveTable();
    output.markdown(`# This is a headline and prints the name of the table: ${table.name}`);
    ```

---

## Context

When the script runs, the context object provides the context. The usage is as follows.

??? info "currentTable"

    Returns the name of the currently selected table.

    ``` js
    base.context.currentTable
    ```

    __Example__

    ``` js
    const name = base.context.currentTable
    output.text(`The name of the current table is: ${name}`)
    ```

??? info "currentRow"

    Returns the currently selected row and returns the complete row object including `_id`, `_mtime`, `_ctime`. If no row is selected, this function returns `undefined`.

    ``` js
    base.context.currentRow
    ```

    __Example__

    ``` js
    const row = base.context.currentRow
    output.text(row)
    ```
