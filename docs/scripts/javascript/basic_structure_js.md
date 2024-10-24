# Basic structure

The JavaScript script runs directly in the current browser and is suitable for simple data processing. JavaScript does not require any authentication.

!!! warning "Two JavaScript APIs in SeaTable"

    SeaTable offers two different ways to use JavaScript with SeaTable. You can executing a JS-Script directly in SeaTable and there is a JavaScript Client API. The functions are similar but not identical.
    If you want to use a JavaScript in SeaTable, stay at this section, otherwise switch to the [Client APIs](clients/javascript/javascript_api/).

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

    ```js
    const table = base.getTableByName('Table1');
    const columns = base.getColumns(table);

    for (var i=0; i<columns.length; i++) {
        output.text(columns[i].name + " (" + columns[i].type + ")")
    }
    ```

    This will return all column names and the column types.

=== "Get row content"

    ```js
    const table = base.getTableByName('Table1'); // (1)!
    const view = base.getViewByName(table, 'Default View'); // (2)!
    const rows = base.getRows(table, view); // (3)!

    for (var i=0; i<rows.length; i++) { // (4)!
    const row = rows[i];
    output.text('>>> new row <<<')
    output.text(row);
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
    const table = base.getTableByName('Table1'); // (1)!

    const newRow = { // (2)!
    'Name': 'Hugo',
    'Age': 3,
    };

    try {
        const row = base.addRow(table, newRow);
        output.text(`New row added with _id: ${row._id}`);
    } catch (error) {
        output.text(`Error adding row: ${error}`);
    }
    ```

    1.  Replace `Table1` with your actual table name
    2.  Update column names `Name` and `Age` and the values you would like to add.

=== "Update one specific cell"

    ``` js
    // Get the table
    const table = base.getTableByName('Table1');

    // Specify the row_id you want to update
    const rowId = 'KDW9PZMkTOuwtx71pmAMxA';

    // Define the updates you want to make
    // Replace 'Name' with the actual column name you want to update
    // and 'NewValue' with the new value you want to set
    const updates = {
        'Name': 'NewValue'
    };

    base.updateRow(table, rowId, updates);
    ```
