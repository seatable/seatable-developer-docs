# Rows

You'll find below all the available methods to interact with the rows of a SeaTable table. In this section, you'll have to deal with the id of the rows. You can find few tips on how to get it in [the user manual](https://seatable.com/help/was-ist-die-zeilen-id/).

{%
    include-markdown "includes.md"
    start="<!--rowstructure-start-->"
    end="<!--rowstructure-end-->"
%}

## Get row(s)

!!! abstract "getRow / <del>getRowById</del> (deprecated)"

    Get a `table`'s row via its id `rowId`.

    ``` js
    base.getRow(table: Object/String /* (1)! */, rowId: String);
    ```

    1. `table`: either a table object or the table name

    __Output__ Single row object (throws an error if `table` doesn't exist or if no row with the specified id `rowId` exists)

    __Example__

    ``` js
    const table = base.getTableByName('Table1');
    const row = base.getRow(table, "M_lSEOYYTeuKTaHCEOL7nw");
    ```

    ``` js
    const row = base.getRow('Table1', "M_lSEOYYTeuKTaHCEOL7nw");
    ```

!!! abstract "getRows"

    Get all the rows displayed in the `view` of a `table`.

    ``` js
    base.getRows(table: Object/String, view: Object/String /* (1)! */);
    ```

    1. `table`: either a table object or the table name
    
        `view` (required): either a view object or the view name

    __Output__ Array of row objects (throws an error if `table` or `view` doesn't exist)

    __Example__

    ``` js
    const table = base.getTableByName('Table1');
    const view = base.getViewByName(table, 'Default View');
    const rows = base.getRows(table, view);

    rows.forEach((row) => {
        output.text(row._id);
    })
    ```

    ``` js
    const rows = base.getRows('Table1', 'Default View');
    ```

!!! abstract "query"

    Use SQL to query a base. SQL queries are the most powerful way access data stored in a base. If your not familiar with SQL syntax, we recommend using first the [SQL query plugin](https://seatable.com/help/anleitung-zum-sql-abfrage-plugin/). Most SQL syntax is supported, you can check the [SQL Reference](/scripts/sql/introduction.md) section of this manual for more information.

    ``` js
    await/* (1)! */ base.query(sqlStatement: String);
    ```

    1. `await` is used for asynchronous functions. This is **required** to ensure that the following operations (or the variable where you store the results) wait for the query's response to arrive before continuing to execute the script

    !!! info "Backticks for table or column names containing or special characters or using reserved words"
    For SQL queries, you can use numbers, special characters or spaces in the names of your tables and columns. However, you'll **have to** escape these names with backticks in order for your query to be correctly interpreted, for example `` SELECT * FROM `My Table` ``. 

    Similarly, if some of your of table or column names are the same as [SQL function](/scripts/sql/functions.md) names (for example a date-type column named `date`), you'll also **have to** escape them in order for the query interpreter to understand that it's not a function call missing parameters, but rather a table or column name.

    __Output__ Array of row objects (single empty object if no row match the request's conditions)

    All the examples below are related to a table **Bill** with the following structure/data:

    | name  | price | year  |
    | ----- | ----- | ----- |
    | Bob   | 300   | 2021  |
    | Bob   | 300   | 2019  |
    | Tom   | 100   | 2019  |
    | Tom   | 100   | 2020  |
    | Tom   | 200   | 2021  |
    | Jane  | 200   | 2020  |
    | Jane  | 200   | 2021  |


    __Example: Get everything with a wildcard__

    === "Function call"

        ``` js
        const data = await base.query('select *  from Bill');/* (1)! */
        output.text(data);
        ```

        1. `*` means that you want to get the whole rows data (columns's values and specific row data such as id, etc.)

    === "Output"

        ```json
        [
            {
                "name": "Bob",
                "price": 300,
                "year": 2021,
                "_locked": null,
                "_locked_by": null,
                "_archived": false,
                "_creator": "bd26d2b...82ca3fe1178073@auth.local",
                "_ctime": "2025-09-15T10:57:19.106+02:00",
                "_last_modifier": "bd26d2b...82ca3fe1178073@auth.local",
                "_mtime": "2025-09-18T09:52:00+02:00",
                "_id": "W77uzH1cSXu2v2UtqA3xSw"
            },
            {
                "name": "Bob",
                "price": 300,
                "year": 2019,
                "_locked": null,
                "_locked_by": null,
                "_archived": false,
                "_creator": "bd26d2b...82ca3fe1178073@auth.local",
                "_ctime": "2025-09-15T10:57:22.112+02:00",
                "_last_modifier": "bd26d2b...82ca3fe1178073@auth.local",
                "_mtime": "2025-09-18T09:52:00+02:00",
                "_id": "IxONgyDFQxmcDKpZWlQ9XA"
            },
            {
                "name": "Tom",
                "price": 100,
                "year": 2019,
                "_locked": null,
                "_locked_by": null,
                "_archived": false,
                "_creator": "bd26d2b...82ca3fe1178073@auth.local",
                "_ctime": "2025-09-15T10:57:23.4+02:00",
                "_last_modifier": "bd26d2b...82ca3fe1178073@auth.local",
                "_mtime": "2025-09-18T09:52:00+02:00",
                "_id": "K4LBuQ7aSjK9JwN14ITqvA"
            },
            {
                "name": "Tom",
                "price": 100,
                "year": 2020,
                "_locked": null,
                "_locked_by": null,
                "_archived": false,
                "_creator": "bd26d2b...82ca3fe1178073@auth.local",
                "_ctime": "2025-09-18T09:52:00+02:00",
                "_last_modifier": "bd26d2b...82ca3fe1178073@auth.local",
                "_mtime": "2025-09-18T09:52:00+02:00",
                "_id": "EHcQEaxiRzm3Zvq8B33bwQ"
            },
            {
                "name": "Tom",
                "price": 200,
                "year": 2021,
                "_locked": null,
                "_locked_by": null,
                "_archived": false,
                "_creator": "bd26d2b...82ca3fe1178073@auth.local",
                "_ctime": "2025-09-18T09:52:00+02:00",
                "_last_modifier": "bd26d2b...82ca3fe1178073@auth.local",
                "_mtime": "2025-09-18T09:52:00+02:00",
                "_id": "CjaCdBlNRXKkYkm231shqg"
            },
            {
                "name": "Jane",
                "price": 200,
                "year": 2020,
                "_locked": null,
                "_locked_by": null,
                "_archived": false,
                "_creator": "bd26d2b...82ca3fe1178073@auth.local",
                "_ctime": "2025-09-18T09:52:00+02:00",
                "_last_modifier": "bd26d2b...82ca3fe1178073@auth.local",
                "_mtime": "2025-09-18T09:52:00+02:00",
                "_id": "YzmUexIAR7iDWmhKGHgpMw"
            },
            {
                "name": "Jane",
                "price": 200,
                "year": 2021,
                "_locked": null,
                "_locked_by": null,
                "_archived": false,
                "_creator": "bd26d2b...82ca3fe1178073@auth.local",
                "_ctime": "2025-09-18T09:52:00+02:00",
                "_last_modifier": "bd26d2b...82ca3fe1178073@auth.local",
                "_mtime": "2025-09-18T09:52:00+02:00",
                "_id": "HJi7wbUMQIOuIlPaoO9Fbg"
            }
        ]
        ```

    __Example with WHERE__

    === "Function call 1 (filter by year)"

        ``` js
        const data = await base.query('select name, price from Bill where year = 2021');
        output.text(data);
        ```

    === "Output #1"

        ```json
        [
            {"name":"Bob","price":"300"},
            {"name":"Tom","price":"200"},
            {"name":"Jane","price":"200"}
        ]
        ```

    === "Function call 2 (filter by name)"

        ```js
        const data = await base.query('select name, price, year from Bill where name = "Bob"');
        output.text(data);
        ```

    === "Output #2"

        ```json
        [
            {"name":"Bob","price":"300","year":"2021"},
            {"name":"Bob","price":"300","year":"2019"}
        ]
        ```


    __Example with GROUP BY__

    === "Function call"

        ``` js
        const data = await base.query('select name, sum(price) from Bill group by name');
        output.text(data);
        ```

    === "Output"

        ```json
        [
            {'name': 'Bob', 'SUM(price)': 600},
            {'name': 'Tom', 'SUM(price)': 400},
            {'name': 'Jane', 'SUM(price)': 400}
        ]
        ```

    __Example with DISTINCT__

    === "Function call"

        ``` js
        const data = await base.query('select distinct name from Bill');
        output.text(data);
        ```

    === "Output"

        ```json
        [
            {'name': 'Bob'},
            {'name': 'Tom'},
            {'name': 'Jane'}
        ]
        ```

!!! abstract "getGroupedRows"

    Get rows in the grouped `view` of a `table`.

    ``` js
    base.getGroupedRows(table: Object/String, view: Object/String /* (1)! */);
    ```

    1. `table`: either a table object or the table name
    
        `view` (required): either a view object or the view name

    __Output__ Array of grouped rows object (see Output example below)

    __Example__

    === "Function call"

        ``` js
        const table = base.getTableByName('Table1');
        const view = base.getViewByName(table, 'GroupedView');
        const groupViewRows = base.getGroupedRows(table, view);
        ```
    
    === "Output example"

        ```json
        [
            { /* (1)! */
                "column_name": "date",
                "column_key": "tc2B",
                "cell_value": "2025-09",
                "rows": [], /* (2)! */
                "subgroups": [
                {
                    "column_name": "Val2",
                    "column_key": "7Q0G",
                    "cell_value": 462,
                    "rows": [
                    {
                        "bjcM": 12,
                        "0000": "John",
                        "7Q0G": 462,
                        "tc2B": "2025-09-11",
                        "Tm99": "520035",
                        "_creator": "aa",
                        "_last_modifier": "cc7a1d0fce...b65b99@auth.local",
                        "_id": "AGO_2SiiTY61uMr-tTVGvQ",
                        "_ctime": "2025-09-11T07:38:23.082+00:00",
                        "_mtime": "2025-09-11T09:28:32.204+00:00",
                        "mpxK": 0
                    },
                    {
                        "bjcM": 12,
                        "0000": "John",
                        "7Q0G": 462,
                        "tc2B": "2025-09-11",
                        "Tm99": "520035",
                        "_creator": "aa",
                        "_last_modifier": "cc7a1d0fce...b65b99@auth.local",
                        "_id": "WTu6o6lxS-ChnamkU1wjuA",
                        "_ctime": "2025-09-11T07:39:10.297+00:00",
                        "_mtime": "2025-09-11T09:28:32.204+00:00",
                        "mpxK": 0
                    }
                    ],
                    "subgroups": [] /* (3)! */
                }
                ]
            },
            {
                "column_name": "date",
                "column_key": "tc2B",
                "cell_value": null,
                "rows": [],
                "subgroups": [
                {
                    "column_name": "Val2",
                    "column_key": "7Q0G",
                    "cell_value": 4,
                    "rows": [
                    {
                        "_id": "GIgxrz8VSzm-aHSbJ6_i4w",
                        "_participants": [],
                        "_creator": "cc7a1d0fce...b65b99@auth.local",
                        "_ctime": "2025-09-03T07:03:57.838+00:00",
                        "_last_modifier": "cc7a1d0fce...b65b99@auth.local",
                        "_mtime": "2025-09-17T15:31:04.150+00:00",
                        "bjcM": 1,
                        "0000": "name",
                        "7Q0G": 4,
                        "plxx": 5676,
                        "Tm99": "207110",
                        "mpxK": ""
                    },
                    {
                        "_id": "PSfpr9dzRPaKUeIn-3va0w",
                        "_participants": [],
                        "_creator": "cc7a1d0fce...b65b99@auth.local",
                        "_ctime": "2025-09-03T07:03:57.838+00:00",
                        "_last_modifier": "cc7a1d0fce...b65b99@auth.local",
                        "_mtime": "2025-09-11T09:28:32.204+00:00",
                        "bjcM": 0,
                        "0000": "zu",
                        "7Q0G": 4,
                        "plxx": 3872,
                        "Tm99": "375528",
                        "mpxK": 0
                    }
                    ],
                    "subgroups": []
                },
                {
                    "column_name": "Val2",
                    "column_key": "7Q0G",
                    "cell_value": 9,
                    "rows": [
                    {
                        "_id": "H3djeRnkQdWhKBhEG2cGUw",
                        "_participants": [],
                        "_creator": "cc7a1d0fce...b65b99@auth.local",
                        "_ctime": "2025-09-03T07:03:57.838+00:00",
                        "_last_modifier": "cc7a1d0fce...b65b99@auth.local",
                        "_mtime": "2025-09-11T09:28:32.204+00:00",
                        "bjcM": 3,
                        "0000": "a",
                        "7Q0G": 9,
                        "plxx": 1668,
                        "Tm99": "520035",
                        "mpxK": 0
                    },
                    {
                        "_id": "ARedNyn8R7CZFmRushZmvQ",
                        "_participants": [],
                        "_creator": "cc7a1d0fce...b65b99@auth.local",
                        "_ctime": "2025-09-03T08:23:03.776+00:00",
                        "_last_modifier": "cc7a1d0fce...b65b99@auth.local",
                        "_mtime": "2025-09-17T15:31:09.842+00:00",
                        "0000": "b",
                        "bjcM": "",
                        "7Q0G": 9,
                        "plxx": 610,
                        "Tm99": "211464",
                        "mpxK": 0
                    },
                    {
                        "_id": "L4IWGz4hT3qb1_u9bBbvFg",
                        "_participants": [],
                        "_creator": "cc7a1d0fce...b65b99@auth.local",
                        "_ctime": "2025-09-03T14:03:51.524+00:00",
                        "_last_modifier": "cc7a1d0fce...b65b99@auth.local",
                        "_mtime": "2025-09-17T15:31:08.429+00:00",
                        "0000": "name",
                        "bjcM": 15,
                        "7Q0G": 9,
                        "plxx": 565,
                        "Tm99": "745764",
                        "mpxK": 0
                    }
                    ],
                    "subgroups": []
                }
                ]
            }
        ]
        ```

        1. Grouped rows object containing either `rows` or `subgroups` (array of grouped rows objects) in the case of multiple grouping rules

        2. No `rows`: this grouped rows object only contains `subgroups` (member of the first grouping rule)

        3. No `subgroups`: this grouped rows object only contains `rows` (member of the last grouping rule)

    ``` js
    const groupViewRows = base.getGroupedRows('Table1', 'GroupedView');
    ```

## Add row

!!! abstract "appendRow / <del>addRow</del> (deprecated)"

    Add a row to a `table`. This row contains the data specified in the object `rowData`. The row will be empty if `rowData` is empty or if it contains only keys that don't exist in the `table`.

    ``` js
    base.appendRow(table: Object/String, rowData: Object, viewName: String /* (1)! */)
    ```

    1. `table`: either a table object or the table name

        `rowData`: object (pairs of `key`:`value`, each `key` being the name of a column), for example:

        ```
        {
            'First Name': 'John',
            'Last Name': 'Doe',
            'Invoice amount': 100,
            'Products': ['Office Supplies', 'Computer']
        }
        ```

    __Output__ Single row object (throws an error if `table` doesn't exist)

    __Example__

    ``` js
    const table = base.getTableByName('Table1');
    base.appendRow(table, {'Name': 'Alex', 'Age': '18'});
    base.appendRow(table, {'Name': 'Alex', 'Age': '18'}, 'Default View');
    ```

## Update row(s)

!!! abstract "updateRow / <del>modifyRow</del>(deprecated)"

    Modify a `row` in the `table`. The `updateRowData` object (pairs of `key`:`value`, each `key` being the name of a column) need to contain only the data you want to update. To reset a value, specify the `key`:`value` pair with an empty string `''`.

    ``` js
    base.updateRow(table: Object/String, row: Object/String, updateRowData: Object /* (1)! */);
    ```

    1. `table`: either a table object or the table name

        `row`: either a row object or the row id

    __Output__ Nothing (throws an error if `table` doesn't exist or if no row with the specified id exists)

    __Example__

    ``` js
    const table = base.getTableByName('Table1');
    const row = base.getRow(table, "M_lSEOYYTeuKTaHCEOL7nw");
    base.updateRow(table, row, {'Name': 'new name', 'number': 100});
    ```

    ``` js
    base.updateRow('Table1', 'U_eTV7mDSmSd-K2P535Wzw', {'Name': 'new name', 'number': 100})
    ```

!!! abstract "modifyRows"

    Modify multiple `rows` in the `table` at once. `updatedRows` is an array of `updateRowData` objects (see above). Please note that `rows` only accepts an array of row objects (and not of ids).

    ``` js
    base.modifyRows(table: Object/String, rows: Array of Object, updatedRows: Array of Object /* (1)! */);
    ```

    1. `table`: either a table object or the table name

        `rows`: array of row objects **only** (not row ids)

    __Output__ Nothing (throws an error if `table` doesn't exist or if one row in `rows` doesn't exists)

    __Example__

    ``` js
    const table = base.getTableByName('Table1');
    const rows = base.getRows(table, 'Default View');
    const selectedColumnName = 'Name';
    const selectedRows = [], updatedRows = [];

    rows.forEach((row) => {
    if (row[selectedColumnName] === 'name') {
        selectedRows.push(row);
        updatedRows.push({[selectedColumnName]: 'name1'});
    }
    });
    base.modifyRows(table, selectedRows, updatedRows);
    ```

    ``` js
    base.modifyRows('Table1', [base.getRow('Table1','GIgxrz8VSzm-aHSbJ6_i4w'),base.getRow('Table1','PSfpr9dzRPaKUeIn-3va0w')], [{'Name': 'name'},{'Name': 'name'}]);
    ```
    
## Delete row

!!! abstract "deleteRow / <del>deleteRowById</del> (deprecated)"

    Delete a row in a `table` by its id `rowId`.

    ``` js
    base.deleteRow(table: Object/String, rowId: String /* (1)! */);
    ```

    1. `table`: either a table object or the table name

        `rowId`: the id of the row to delete


    __Output__ Nothing (no error if no row with id `rowId` exists)

    __Example__

    ``` js
    const table = base.getTableByName('Table1');
    base.deleteRow(table, 'M_lSEOYYTeuKTaHCEOL7nw');
    ```

    ``` js
    base.deleteRow('Table1', 'M_lSEOYYTeuKTaHCEOL7nw');
    ```



## Filter

!!! abstract "filter"

    Filters the rows displayed in the view `viewName` of the `table` that meet the conditions of the `filterExpression` (conditional statement), and returns a querySet object. See the `filterExpression` reference below for more details.

    ``` js
    base.filter(tableName: String, viewName: String, filterExpression: String);
    ```

    __Output__ Single querySet object (see below), the `rows` array being empty if no row meet the `filterExpression` conditions

    __Example__

    === "Function call"

        ``` js
        // Filter out rows whose number column is equal to 5, and return a querySet object
        const querySet = base.filter('Table1', 'Default View', 'number = 5');
        ```
    
    === "Output structure"

        ```json
        {
            "rows": [ /* (1)! */
                ...
            ],
            "table": { /* (2)! */
                ...
            },
            "parser": {
                ...
            }
        }
        ```

        1. `rows`: array of the rows in the view `viewName` meeting the `filterExpression` conditions

        2. `table`: the whole `table` object
    

    ```js
    const querySet = base.filter("Table1", "Default View", "age>18"/* (1)! */)
    ```

    1. `age`: column name

        `>`: operator

        `18`: parameter

### filterExpression reference

!!! abstract "filterExpression"

    The most common operators are available to define the conditional statement of the `filterExpression`:

    | Type of operators  | Available operators |
    | ------------------ | ------------------- |
    | Greater-Less comparisons | >=， >， <， <= |
    | Equal-Not equal comparisons | =,  <> (not equal to) |
    | Arithmetic operators | +, -, *, /, ^ (power), % (modulo) |
    | Logical operators | and, or |   
    
    Depending on the data type, there are slight differences in the query method and the format of input statement. Here is a list of the possible operations for each type:


    | Data structure | Column type                               | Format for Greater-Less comparisons                 | Format for Equal-Not equal comparisons             | Arithmetic operators |
    | -------------- | ----------------------------------------- | ----------------------------------------------------------- | --------------------------------------------------- | :---------- |
    | String         | Text, Long Text, URL, Email, Single Select | Unsupported                                                 | String                                              | Unsupported |
    | List           | Multiple Select                           | Unsupported                                                 | String                                              | Unsupported |
    | Number         | Number                                    | Number                                                  | Number and empty String `""`""                     | Supported   |
    | Date           | Date, Created time,  Last modified time   | Patterns: YYYY-MM-DD, YYYY-MM-DD hh:mm, YYYY-MM-DD hh\:mm:ss | Same patterns as greater-less query                 | Unsupported |
    | Boolean        | Checkbox                                  | Unsupported                                                 | true, false and empty String `""`, (case-insensitive) | Unsupported |


    !!! info "Mind the quotes!"
        For queries involving string-based or date-based columns, you'll have to use double quotes `" "` to define the `filterExpression` as you'll need simple quotes `' '` for the strings/dates... Or the opposite: use either `"column_name='hello world'"` or `'column_name="hello world"'`

    Here are more examples of the different filter expressions pending of the column type.

    __String-based Column__ (**Text, Long Text, URL, Email, Single Select** columns)


    ```js
    // Equal-unequal query
    base.filter('Table1', 'Default View', "column_name='hello world'")
    base.filter('Table1', 'Default View', "column_name!=''")

    ```

    <br>
    __List-based Column__ (**Multiple Select** columns)


    ```js
    // Equal-unequal query
    base.filter('Table1','Default View', "column_name='A' and column_name='B'") /* (1)! */
    ```

    1. Find the rows which contains both 'A' and 'B'

    <br>
    __Number-based Column__ (**Number** columns)

    === "Greater-less query"

        ```js
        base.filter('Table1', 'Default View', "column_name>18")
        base.filter('Table1', 'Default View', "column_name>-10 and column_name<=0")
        ```

    === "Equal-unequal query"

        ```js
        base.filter('Table1', 'Default View',"column_name<>20")
        base.filter('Table1', 'Default View', "column_name=0")
        base.filter('Table1', 'Default View',"column_name=''")
        ```

    === "Arithmetic query"

        ```js
        base.filter('Table1', 'Default View', "column_name+3>18")
        base.filter('Table1', 'Default View', "column_name*2=18")
        base.filter('Table1', 'Default View', "column_name-2=18")
        base.filter('Table1', 'Default View', "column_name/2=18")
        base.filter('Table1', 'Default View', "column_name^2=18")
        base.filter('Table1', 'Default View', "column_name%2=1")
        ```

    <br>
    __Date-based Column__ (**Date, Created time, Last modified time** columns)

    === "Greater-less query"

        ```js
        base.filter('Table1', 'Default View', "column_name>'2020-1-30'")
        base.filter('Table1', 'Default View', "column_name>='2019-1-1 5:30' and column_name<='2019-5-1 6:00'")
        ```

    === "Equal-unequal query"

        ```js
        base.filter('Table1', 'Default View', "column_name='2020-1-1 10:59:59'")
        base.filter('Table1', 'Default View', "column_name!=''")
        ```

    <br>
    __Boolean-based Column__ (**Checkbox** columns)

    === "Equal-unequal query"

        ```js
        base.filter('Table1', 'Default View','column_name=False')/* (1)! */
        base.filter('Table1', 'Default View', "column_name=True")
        ```

        1. same as `base.filter('Table1', "column_name=''")`

### querySet handling

The output of the `base.filter` function is a `querySet` object. Here are the methods of this object provided to simplify the operations on the filtered data.

!!! abstract "all"

    Returns all filtered rows of the `querySet` in the form of a list.

    ``` js
    querySet.all();
    ```

    __Output__ Array of row objects

    __Example__

    ``` js
    const querySet = base.filter('Table1', 'Default View', 'number = 5');
    const list = querySet.all();
    output.text(list);
    ```

!!! abstract "count"

    Returns the number of filtered rows of the `querySet`.

    ``` js
    querySet.count();
    ```

    __Output__ Number

    __Example__

    ```js
    const querySet = base.filter('Table1', 'Default View', 'number = 5');
    const count = querySet.count();
    output.text(`The querySet contains ${count} rows`);
    ```

!!! abstract "first"

    Return the first filtered row of the `querySet`.

    ``` js
    querySet.first();
    ```

    __Output__ Single row object (`undefined` if the `querySet` contains no row)

    __Example__

    ```js
    const querySet = base.filter('Table1', 'Default View', 'number = 5');
    const row = querySet.first();
    ```

!!! abstract "last"

    Return the last filtered row of the `querySet`.

    ``` js
    querySet.last();
    ```

    __Output__ Single row object (`undefined` if the `querySet` contains no row)

    __Example__

    ```js
    const querySet = base.filter('Table1', 'Default View', 'number = 5');
    const row = querySet.last();
    ```

!!! abstract "delete"

    Delete all filtered rows of the `querySet` and return the number of rows successfully deleted.

    ``` js
    querySet.delete();
    ```

    __Output__ Number

    __Example__

    ```js
    const querySet = base.filter('Table1', 'Default View', 'number = 5');
    const count = querySet.delete();
    output.text(`${count} rows successfully deleted!`);
    ```

!!! abstract "update"

    Modify the row data according to the`rowData` Object and return the updated rows.

    ``` js
    querySet.update(rowData: Object/* (1)! */);
    ```

    1. `rowData`: object (pairs of `key`:`value`, each `key` being the name of a column)

    __Output__ Array of row objects (empty Array if no filtered row)

    __Example__

    ```js
    // Modify the content of the Name column of all filtered rows to xxxx
    const querySet = base.filter('Table1', 'Default View', 'number = 5');
    const rows = querySet.update({Name: 'xxxx'});
    ```

!!! abstract "filter"

    Further filtering using the `filterExpression` conditional statement.

    ```js
    querySet.filter(filterExpression: String);
    ```

    __Output__ Single querySet object

    __Example__

    ```js
    // Filter out the rows with the value of Tom in the Name column of querySet1
    const querySet1 = base.filter('Table1', 'Default View', 'number = 5');
    const querySet2 = querySet1.filter("Name = 'Tom'");
    ```

!!! abstract "get"

    Return the first row of the querySet that meets the conditions of the new `filterExpression`. This is equivalent to `querySet.filter(filterExpression).first()`

    ```js
    querySet.get(filterExpression: String);
    ```

    __Output__ Single row object (`undefined` if no row meets the conditions of the `filterExpression`, `#ERROR!` if the `filterExpression` is wrong)

    __Example__

    ```js
    // Get the first data of Tom in the Name column of the querySet
    const querySet = base.filter('Table1', 'Default View', 'number = 5');
    const row = querySet.get("Name = 'Tom'");
    ```
