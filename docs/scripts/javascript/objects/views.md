# Views

Functions to interact with the views of a table.

## Get Views

!!! question "getActiveView"

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

!!! question "getViews"

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

!!! question "getViewByName"

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

## Add View

!!! question "addView"

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

## Rename View

!!! question "renameView"

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

## Delete View

!!! question "deleteView"

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
