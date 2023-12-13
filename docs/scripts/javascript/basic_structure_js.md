# Basic structure

The JavaScript script runs directly in the current browser and is suitable for simple data processing. JavaScript does not require any authentication.
The source code of the used JavaScript API is available at [Github](https://github.com/seatable/seatable-api-js).

## Interact with your base

JavaScript provide pre-defined objects, corresponding methods of this objects and utilities. On top, normal JavaScript operations like `console.log` or calculations are working as usual.

- [base](/scripts/javascript/objects/base/)
- [output](/scripts/javascript/objects/output/)
- [context](/scripts/javascript/objects/context/)
- [base utilities](/scripts/javascript/objects/utilities/)

## Let's beginn

Let's make this concrete and let us look at some basic examples.

1. Jump to your seatable webinterface
2. Create a new Script of the type `Javascript`
3. Copy the following code
4. Run the script

You will learn from these examples, that it is quite easy to read, output and even manipulate the data of a base inside SeaTable with the predefined objects and the corresponding methods.

=== "Get number of tables"

    ``` js
    const tables = base.getTables(); // (1)!
    output.text(tables.length); // (2)!
    ```

    1.  1. `base` is the predefined-object provided by SeaTable containing all bases of a base.
        1. `getTables()` is the function to get all bases from the object `base`.

    2.  1. `output` is also a predefined-object provided by SeaTable.
        1. `length` is just a normal operation in JavaScript.

    As you can see, the script will output the number of tables in your base. Read the comments behind the two lines to get more information about the difference between a predefined object, a method of this object and an ordinary JavaScript function.

=== "Get column names"

    ``` js
    const table = base.getTableByName('Table1'); // (1)!
    const view = base.getViewByName(table, 'Default View'); // (2)!
    const rows = base.getRows(table, view); // (3)!

    for (var i=0; i<rows.length; i++) { // (4)!
    const row = rows[i];
    output.text(row['Name']);
    }
    ```

    1.  get the content of the table `Table1`.
    2.  get the content of the view `Default View`.
    3.  get the row of this view `Default View` in this table `Table1`.
    4.  iterate over all rows and print them

    This time, we will get the `Name` of all columns in the table `Table1` and the view `Default View`.

=== "Write new row"

    ``` js
    comming soon.
    ```

=== "Update one specific cell"

    ``` js
    comming soon.
    ```
