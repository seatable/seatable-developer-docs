# Views

{%
    include-markdown "includes.md"
    start="<!--viewstructure-start-->"
    end="<!--viewstructure-end-->"
%}

## Get View(s)

!!! abstract "getActiveView :material-tag-outline:{ title='Scripting only' }"

    Get the current view of the active table. Only available in SeaTable scripts.

    ``` js
    base.getActiveView();
    ```js

    __Output__ Single view object

    __Example__
    ``` js
    const view = base.getActiveView();
    output.text(view.name);
    ```

!!! abstract "getViewByName"

    Get a view of a table, specified by its name.

    ``` js
    base.getViewByName(table, viewName);
    ```js

    __Output__ Single view object (`undefined` if no view with that name exists)

    __Example__
    ``` js
    const view = base.getViewByName('Table1', 'Default View');
    ```

!!! abstract "listViews"

    Get all the views of a table.

    ``` js
    base.listViews(table);
    ```js

    __Output__ Array of view objects

    __Example__
    ``` js
    const views = base.listViews('Table1');
    ```

## Add View

!!! abstract "addView"

    Add a new view to a table.

    ``` js
    base.addView(table, viewName);
    ```js

    __Example__
    ``` js
    base.addView('Table1', 'My View');
    ```

## Rename View

!!! abstract "renameView"

    Rename an existing view.

    ``` js
    base.renameView(table, currentViewName, newViewName);
    ```js

    __Example__
    ``` js
    base.renameView('Table1', 'Default View', 'Main View');
    ```

## Delete View

!!! abstract "deleteView"

    Delete a view. Deleting the last view is not possible.

    ``` js
    base.deleteView(table, viewName);
    ```js

    __Example__
    ``` js
    base.deleteView('Table1', 'Old View');
    ```
