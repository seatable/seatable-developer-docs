# Query with SQL

!!! question "query"

    Use sql to query a base
    ``` js
    base.query(sql)
    ```

    __Example: BASIC__
    ``` js
    await base.query('select name, price, year from Bill')
    ```
    Returns for example the following:
    ``` js
    [
        {'_id': 'PzBiZklNTGiGJS-4c0_VLw', 'name': 'Bob', 'price': 300, 'year': 2019},
        {'_id': 'Ep7odyv1QC2vDQR2raMvSA', 'name': 'Bob', 'price': 300, 'year': 2021},
        {'_id': 'f1x3X_8uTtSDUe9D60VlYQ', 'name': 'Tom', 'price': 100, 'year': 2019},
        {'_id': 'NxeaB5pDRFKOItUs_Ugxug', 'name': 'Tom', 'price': 100, 'year': 2020},
        {'_id': 'W0BrjGQpSES9nfSytvXgMA', 'name': 'Tom', 'price': 200, 'year': 2021},
        {'_id': 'EvwCWtX3RmKYKHQO9w2kLg', 'name': 'Jane', 'price': 200, 'year': 2020},
        {'_id': 'BTiIGSTgR06UhPLhejFctA', 'name': 'Jane', 'price': 200, 'year': 2021}
    ]
    ```

    __Example: WHERE__

    ``` js
    await base.query('select name, price from Bill where year = 2021 ')
    ```
    Returns for example the following:
    ``` js
    [
        {'_id': 'Ep7odyv1QC2vDQR2raMvSA', 'name': 'Bob', 'price': 300},
        {'_id': 'W0BrjGQpSES9nfSytvXgMA', 'name': 'Tom', 'price': 200},
        {'_id': 'BTiIGSTgR06UhPLhejFctA', 'name': 'Jane', 'price': 200}
    ]
    ```

    __Example: ORDER BY__

    ``` js
    await base.query('select name, price, year from Bill order by year')
    ```
    Returns for example the following:

    ``` js
    [
        {'_id': 'PzBiZklNTGiGJS-4c0_VLw', 'name': 'Bob', 'price': 300, 'year': 2019},
        {'_id': 'f1x3X_8uTtSDUe9D60VlYQ', 'name': 'Tom', 'price': 100, 'year': 2019},
        {'_id': 'NxeaB5pDRFKOItUs_Ugxug', 'name': 'Tom', 'price': 100, 'year': 2020},
        {'_id': 'EvwCWtX3RmKYKHQO9w2kLg', 'name': 'Jane', 'price': 200, 'year': 2020},
        {'_id': 'Ep7odyv1QC2vDQR2raMvSA', 'name': 'Bob', 'price': 300, 'year': 2021},
        {'_id': 'W0BrjGQpSES9nfSytvXgMA', 'name': 'Tom', 'price': 200, 'year': 2021},
        {'_id': 'BTiIGSTgR06UhPLhejFctA', 'name': 'Jane', 'price': 200, 'year': 2021}
    ]
    ```

    __Example: GROUP BY__

    ``` js
    await base.query('select name, sum(price) from Bill group by name')
    ```
    Returns for example the following:
    ``` js
    [
        {'SUM(price)': 600, 'name': 'Bob'},
        {'SUM(price)': 400, 'name': 'Tom'},
        {'SUM(price)': 400, 'name': 'Jane'}
    ]
    ```

    __Example: DISTINCT__

    ``` js
    await base.query('select distinct name from Bill')
    ```
    Returns for example the following:

    ``` js
    [
        {'_id': 'PzBiZklNTGiGJS-4c0_VLw', 'name': 'Bob'},
        {'_id': 'f1x3X_8uTtSDUe9D60VlYQ', 'name': 'Tom'},
        {'_id': 'EvwCWtX3RmKYKHQO9w2kLg', 'name': 'Jane'}
    ]
    ```
