# Utility functions

Utility functions help you to work with data in SeaTable.

## Date and Time

!!! abstract "formatDate"

    Format `date` to 'YYYY-MM-DD' to be used in a date-type column.

    ``` js
    base.utils.formatDate(date: Date Object)
    ```

    __Output__ String
    
    __Example__
    ``` js
    let date = new Date();
    let formatDate = base.utils.formatDate(date);
    output.text(formatDate);
    ```

!!! abstract "formatDateWithMinutes"

    Format `date` to 'YYYY-MM-DD HH:mm' to be used in a date-type column.

    ``` js
    base.utils.formatDateWithMinutes(date: date object)
    ```

     __Output__ String

    __Example__
    ``` js
    let date = new Date();
    let formatDate = base.utils.formatDateWithMinutes(date);
    output.text(formatDate);
    ```

## Lookup and Query

!!! abstract "lookupAndCopy"

    Similar to the Microsoft Excel VLOOKUP function. Find a matching row in the *source* table for each row of the *target* table, and then copy the data of the specified cell of the matching row to the specified cell of the *target* row. Every arguments are `String`.

    ``` js
    base.utils.lookupAndCopy(targetTable, targetColumn, targetColumnToCompare, sourceTableName, 
                             sourceColumnName, sourceColumnToCompare = null /* (1)! */);
    ```

    1. `targetTable`: the name of the *target* table - i.e. the table you want to copy data **into**

        `targetColumn`: the column of `targetTable` you want to copy data into

        `targetColumnToCompare`: the column of `targetTable` you want to compare to a column of table `sourceTableName`

        `sourceTableName`: the *source* table - i.e. the table you want to copy data **from**

        `sourceColumnName`: the column of `sourceTableName` you want to copy data from

        `sourceColumnToCompare`: If specified, the column of `sourceTableName` you want to compare with `targetColumnToCompare` to find matching rows. If not specified, the system will look for a column with the name `targetColumn` in the table `sourceTableName`
    
     __Output__ Nothing (throws an error if some tables or columns do not exist)
    
    __Principle example__

    Here are two tables, the *source* table containing both names and emails for few Avengers whereas the *target* table only has the user names.

    **Source table**

    | Name | SourceEmail |
    | ---  | --- |
    | Hulk | greenbigboy@stark-industries.movie |
    | Tony | ironman|stark-industries.movie |

    **Target table**

    | Name | TargetEmail |
    | ---  | --- |
    | Hulk | |
    | Tony | |

    To copy the email addresses from the *source* table to the *target* table, this function can be used with the following syntax:

    ```
    base.utils.lookupAndCopy('Target table', 'TargetEmail', 'Name', 'Source table', 'SourceEmail');
    ```

    __Example__

    ``` js
    // Match the rows with the same content in the Name column of Table1 and Table2, 
    // copy the contents of the Email column of the row in Table1 to the Email column 
    // of the corresponding row in Table2
    base.utils.lookupAndCopy('Table2', 'Email', 'Name', 'Table1', 'Email');

    // Match the rows with the same content in the Name column in Table1 and the Name1 column
    //  in Table2, and copy the contents of the Email column of the row in Table1 to the 
    // Email1 column of the corresponding row in Table2
    base.utils.lookupAndCopy('Table2', 'Email1', 'Name1', 'Table1', 'Email', 'Name');

    ```

!!! abstract "query"

    Filter and summarize the table `tableName` data of the view `viewName` by SQL like `query` statements.

    ``` js
    base.utils.query(tableName: String, viewName: String, query: String);
    ```

    __Example__

    ``` js
    // Filter out the rows where the sum of the three columns 'number', 'number1', 
    // and 'number2' is greater than 5 then sum the number and number2 columns in these rows, 
    // return {number: 12, number2: 23}
    base.utils.query('Table1', 'Default View', 'select sum(number), sum(number2) where number + number1 + number2 > 5');
    ```
