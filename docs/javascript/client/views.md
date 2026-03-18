# Views

## Get Views

!!! question "listViews"

    ``` js
    base.listViews(table_name)
    ```

    __Example__
    ``` js
    const views = await base.listViews('Table1')
    ```

!!! question "getViewByName"

    ``` js
    base.getViewByName(table_name, view_name);
    ```

    __Example__
    ``` js
    const view = await base.getViewByName('Table1', 'MyView');
    ```

## Add View

!!! question "addView"

    ``` js
    base.addView(table_name, new_view_name);
    ```

    __Example__
    ``` js
    await base.addView('Table1', 'new_view');
    ```

## Rename View

!!! question "renameView"

    ``` js
    base.renameView(table_name, view_name, new_view_name);
    ```

    __Example__
    ``` js
    await base.renameView('Table1', 'myView', 'myView-01');
    ```

## Delete View

!!! question "deleteView"

    ``` js
    base.deleteView(table_name, view_name);
    ```

    __Example__
    ``` js
    await base.deleteView('Table1', 'MyView');
    ```
