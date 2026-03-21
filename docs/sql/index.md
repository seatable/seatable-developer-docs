# SQL

SeaTable provides an SQL interface for querying and modifying data. It supports `SELECT`, `INSERT`, `UPDATE`, and `DELETE` statements. SQL can be used from any programming language — through the [Python](../python/) and [JavaScript](../javascript/) client libraries via `base.query()`, or directly through the [REST API](https://api.seatable.com/reference/query-with-sql).

=== "Python"

    ```python
    results = base.query("SELECT * FROM Table1 LIMIT 100")
    ```

=== "JavaScript"

    ```js
    const results = await base.query("SELECT * FROM Table1 LIMIT 100");
    ```

=== "API"

    ```bash
    curl -X POST \
      'https://cloud.seatable.io/api-gateway/api/v2/dtables/{base_uuid}/sql/' \
      -H 'Authorization: Bearer {base_token}' \
      -H 'Content-Type: application/json' \
      -d '{"sql": "SELECT * FROM Table1 LIMIT 100", "convert_keys": true}'
    ```

All three methods use the same SQL engine and return identical results. SQL syntax is case insensitive — keywords, function names, and identifiers can be written in any case. We use upper-case for SQL keywords (`SELECT`, `WHERE`, ...) and lower-case for function names (`now()`, `round()`, ...) for readability.

!!! tip "New to SQL?"

    Try the [SQL query plugin](https://seatable.com/help/anleitung-zum-sql-abfrage-plugin/) in SeaTable to experiment with queries interactively.

## Quick reference

### Supported

| Feature | Notes |
|:---|:---|
| `SELECT`, `UPDATE`, `DELETE` | |
| `INSERT` | [Requires Big Data storage](insert.md) |
| `WHERE` with `=`, `!=`, `<>`, `>`, `<`, `>=`, `<=` | |
| `LIKE`, `ILIKE`, `IN`, `NOT IN`, `BETWEEN`, `IS [NOT] NULL` | |
| `AND`, `OR`, `NOT` | |
| `GROUP BY`, `HAVING`, `ORDER BY`, `LIMIT`, `OFFSET` | |
| `DISTINCT`, `AS` aliases | |
| `COUNT`, `SUM`, `MIN`, `MAX`, `AVG` | Standard SQL aggregates |
| Implicit joins: `FROM T1, T2 WHERE T1.col = T2.col` | Inner join only |
| Arithmetic operators `+`, `-`, `*`, `/` in `SELECT` | |
| [SeaTable functions](functions.md) in `SELECT`, `WHERE`, `GROUP BY`, `HAVING`, `ORDER BY` | |
| [Extended list operators](select.md#extended-list-operators): `HAS ANY OF`, `HAS ALL OF`, etc. | For multi-select and collaborator columns |

### Not supported

| Feature | Alternative |
|:---|:---|
| `JOIN` keyword (`INNER JOIN`, `LEFT JOIN`, etc.) | Use implicit joins |
| Subqueries | Split into multiple queries |
| `UNION` / `UNION ALL` | Split into multiple queries |
| `CASE WHEN ... THEN ... END` | Use SeaTable `if()` or `ifs()` function |
| MySQL functions (`SUBSTR`, `CONCAT`, `LENGTH`, etc.) | Use [SeaTable equivalents](functions.md): `mid()`, `concatenate()`, `len()` |
| Functions or expressions in `UPDATE SET` | Read with `SELECT`, compute, write with API |
| Functions in `INSERT VALUES` | Use API `appendRow` instead |

## Formulas in SQL queries

You can use SeaTable formula syntax directly in SQL queries. A few differences from SeaTable's built-in formulas:

- Link formulas (e.g. `{link.age}`) are **not** supported
- Column references are **not** enclosed in curly brackets: use `abs(column)`, not `abs({column})`
- Use backticks for column names with spaces or hyphens: `` abs(`column-a`) ``
- Column aliases cannot be used in formulas: `abs(t.column)` is invalid

For the complete list of available functions, see the [function reference](./functions.md).
