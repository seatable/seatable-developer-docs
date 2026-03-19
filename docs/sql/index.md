# SQL

SQL queries are the most powerful way to access data stored in a base. SeaTable supports `SELECT`, `INSERT`, `UPDATE`, and `DELETE` statements. SQL is not a standalone interface but is used through the [Python](../python/) or [JavaScript](../javascript/) API via `base.query()`:

=== "Python"

    ```python
    results = base.query("SELECT * FROM Table1 LIMIT 100")
    ```

=== "JavaScript"

    ```js
    const results = await base.query("SELECT * FROM Table1 LIMIT 100");
    ```

SQL syntax is case insensitive. We use upper-cased keywords for readability.

!!! tip "New to SQL?"

    Try the [SQL query plugin](https://seatable.com/help/anleitung-zum-sql-abfrage-plugin/) in SeaTable to experiment with queries interactively.
