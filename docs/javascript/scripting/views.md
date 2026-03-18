# Views

You'll find below all the available methods to interact with the views of a SeaTable table.

{%
    include-markdown "includes.md"
    start="<!--viewstructure-start-->"
    end="<!--viewstructure-end-->"
%}

## Get View(s)

!!! abstract "getActiveView"

    Get the current view of the active table.

    ``` js
    base.getActiveView();
    ```

    __Output__ Single view object

    __Example__
    ``` js
    const view  = base.getActiveView();
    output.text(view._id);
    output.text(view);
    ```

!!! abstract "getViewByName"

    Get a view of a particular `table`, specified by its name `viewName`.

    ``` js
    base.getViewByName(table: Object/String/* (1)! */, viewName: String);
    ```

    1. `table`: either a table object or the table name
    
    __Output__ Single view object (`undefined` if no view called `viewName` exists, throws an error if `table` doesn't exist)

    __Example__
    ``` js
    const table  = base.getTableByName('Table1');
    const view = base.getViewByName(table, 'Default View');
    output.text(view.name);
    ```

    ``` js
    const view = base.getViewByName('Table1', 'Default View');
    output.text(view.name);
    ```

!!! abstract "listViews / <del>getViews</del> (deprecated)"

    Get all the views of the `table`.

    ``` js
    base.listViews(table: Object/String/* (1)! */);
    ```

    1. `table`: either a table object or the table name

    __Output__ Array of view objects (throws an error if `table` doesn't exist)

    __Example__
    ``` js
    const table  = base.getTableByName('Table1');
    const views = base.listViews(table);
    output.text(views.length);
    ```

## Add View

!!! abstract "addView"

    Add a view named `viewName` to a `table`.

    ``` js
    base.addView(table: Object/String/* (1)! */, viewName: String);
    ```

    1. `table`: either a table object or the table name

    __Output__ Nothing (throws an error if `table` doesn't exist)

    __Example__
    ``` js
    const table  = base.getTableByName('Table1');
    base.addView(table, 'view 2');
    ```

    ``` js
    base.addView('Table1', 'view 2');
    ```

## Rename View

!!! abstract "renameView"

    Rename a view in the `table` specified by its current name `currentViewName` and its new name `nextViewName`. Please ensure that you choose a `nextViewName` that doesn't already exists in your `table`.

    ``` js
    base.renameView(table: Object/String/* (1)! */, currentViewName: String, nextViewName: String);
    ```

    1. `table`: either a table object or the table name

    __Output__ Nothing (throws an error if `table` or `currentViewName` doesn't exist)

    __Example__
    ``` js
    const table  = base.getTableByName('Table1');
    base.renameView(table, 'Default View', 'view2');
    ```

    ``` js
    base.renameView('Table1', 'Default View', 'view2');
    ```

## Delete View

!!! abstract "deleteView"

    Delete a view in a particular `table`, specified by its name `viewName`. Deleting the last view is not possible.

    ``` js
    base.deleteView(table: Object/String/* (1)! */, viewName: String);
    ```

    1. `table`: either a table object or the table name

    __Output__ Nothing (throws an error if `table`  doesn't exist or no view called `viewName` exists)

    __Example__
    ``` js
    const table  = base.getTableByName('Table1');
    base.deleteView(table, 'view2');
    ```

    ``` js
    base.deleteView('Table1', 'view2');
    ```
