# SQL in SeaTable

SQL queries are the most powerful way to access data stored in a base. SeaTable supports `SELECT`, `INSERT`, `UPDATE`, and `DELETE` statements.

If you're not familiar with SQL syntax, try the [SQL query plugin](https://seatable.com/help/anleitung-zum-sql-abfrage-plugin/) in SeaTable first.

!!! info "Backticks for special names"
    Escape table or column names that contain spaces, special characters, or match [SQL function](./functions.md) names with backticks: `` SELECT * FROM `My Table` ``.

## How to use SQL

SQL queries can be executed via the Python or JavaScript API:

=== "Python"

    ```python
    results = base.query("SELECT * FROM Table1 LIMIT 100")
    ```

=== "JavaScript"

    ```js
    const results = await base.query("SELECT * FROM Table1 LIMIT 100");
    ```

SQL syntax is case insensitive. We use upper-cased keywords for readability.

## Sections

- [SELECT](select.md): Retrieve rows with filtering, sorting, grouping, and aggregation
- [INSERT, UPDATE, DELETE](insert-update-delete.md): Modify data
- [Clauses](clauses.md): WHERE, GROUP BY, HAVING, ORDER BY, LIKE, BETWEEN
- [Data Types](data-types.md): Column type mapping, list types, NULL handling
- [Extended Syntax](extended-syntax.md): Formulas in SQL, list operators, big data indexes
- [Functions](functions.md): Complete function reference
