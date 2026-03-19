# SQL Queries

Use SQL to query a base. This is the most powerful way to access data. For the full SQL syntax reference, see the [SQL Reference](/sql/index.md).

!!! abstract "query"

    ``` js
    await base.query(sql);
    ```

    !!! info "Backticks for special names"
        Escape table or column names that contain spaces, special characters, or are [SQL function names](/sql/functions.md) with backticks: `` SELECT * FROM `My Table` ``

    __Output__ Array of row objects

__Example: SELECT all__
``` js
const data = await base.query('SELECT * FROM Bill');
```

__Example: WHERE__
``` js
const data = await base.query('SELECT name, price FROM Bill WHERE year = 2021');
```

__Example: ORDER BY__
``` js
const data = await base.query('SELECT name, price, year FROM Bill ORDER BY year');
```

__Example: GROUP BY__
``` js
const data = await base.query('SELECT name, SUM(price) FROM Bill GROUP BY name');
// Returns: [{'SUM(price)': 600, 'name': 'Bob'}, ...]
```

__Example: DISTINCT__
``` js
const data = await base.query('SELECT DISTINCT name FROM Bill');
```
