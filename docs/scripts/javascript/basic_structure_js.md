# Basic structure

The JavaScript scripts run directly in the current browser and are suitable for simple data processing. JavaScript does not require any authentication.

{%
    include-markdown "includes.md"
    start="<!--datamodel-start-->"
    end="<!--datamodel-end-->"
%}

This manual list all available objects and methods (also called functions) that are available within JavaScript scripts in SeaTable to interact with this data structure. On top, normal JavaScript operations like `console.log` or calculations are working as usual. By running directly in SeaTable, JavaScript scripts have the ability to access the [base context](/scripts/javascript/objects/context/). [Base utilities](/scripts/javascript/objects/utilities/) and specific [output methods](/scripts/javascript/objects/output/) are also available.

!!! warning "Two JavaScript APIs in SeaTable"

    SeaTable offers two different ways to use JavaScript with SeaTable. You can executing a JavaScript script directly in SeaTable and there is a JavaScript Client API. The functions are similar but not identical.
    If you want to use a JavaScript script in SeaTable, stay at this section, otherwise switch to the [Client APIs](clients/javascript/javascript_api/).

!!! info "Need specific function?"

    The JavaScript class does not yet cover all available functions of the SeaTable API. If you are missing a special function, please contact us at [support@seatable.io](mailto:support@seatable.io) and we will try to add the missing functions.

For details about the different objects (tables, view, rows & columns and links) you can look at the global structure presented in each object page in the [Scripting section](./scripts/index.md) or at the [SeaTable API Reference](https://api.seatable.com/reference/models) for even more information.

## Getting started

Let's have a look at some basic examples. You will learn that it is quite easy to read, output and even manipulate the data of a base inside SeaTable with the predefined objects and the corresponding methods. Here is how to run these examples in your environment:

1. Jump to your SeaTable web interface
2. Create a new Script of the type `JavaScript`
3. Copy the following code (you might have to change tables' or columns' names)
4. Run the script

=== "Get number of tables"

    ``` js
    const tables = base.getTables(); // (1)!
    output.text(tables.length); // (2)!
    ```

    1.  1. `base` is the predefined-object provided by SeaTable containing all tables of a base.
        1. `getTables()` is the function to get all bases from the object `base`.

    2.  1. `output` is also a predefined-object provided by SeaTable.
        1. `length` is just a pure JavaScript property.

    As you can see, the script will output the number of tables in your base. Read the comments at the end of both lines to get more information about the difference between a predefined object, a function of this object and a pure JavaScript property.

=== "Get column names"

    ```js
    const table = base.getTableByName('Table1'); // (1)!
    const columns = base.getColumns(table); // (2)!

    for (var i=0; i<columns.length; i++) {  // (3)!
        output.text(columns[i].name + " (" + columns[i].type + ")")
    }
    ```

    1.  get the content of the table `Table1` (replace `Table1` with your actual table name).
    2.  get the columns of the table `Table1` in an array.
    3.  iterate over all columns of the array `columns`.

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

    1.  get the content of the table `Table1` (replace `Table1` with your actual table name).
    2.  get the content of the view `Default View`.
    3.  get the rows displayed in the view `Default View` of the table `Table1`.
    4.  iterate over all rows and print them

    This time, we will get content of the `Name` column for each row displayed in the view `Default View` of the table `Table1`.

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

    1.  get the content of the table `Table1` (replace `Table1` with your actual table name).
    2.  create an object containing column names `Name` and `Age` and the values you would like to set.

=== "Update one specific row"

    ``` js
    // Get the table
    const table = base.getTableByName('Table1');

    // Specify the row_id you want to update
    const rowId = 'KDW9PZMkTOuwtx71pmAMxA'; // (1)!

    // Define the updates you want to make
    // Replace 'Name' with the actual column name you want to update
    // and 'NewValue' with the new value you want to set
    // You can define more key:value pairs if you want to update
    // several values of the row at the same time
    const updates = {
        'Name': 'NewValue'
    };

    base.updateRow(table, rowId, updates); // (2)!
    ```

    1. define the id of the row you want to modify. You can also use `base.context.currentRow;` to access the current (selected) row.
    2. update each values contained in the object `updates` of the row whose id is `rowId` in the table `Table1`.

    Do not hesitate to write comments in your code. It will help you (or others) to understand it more easily afterwards.


