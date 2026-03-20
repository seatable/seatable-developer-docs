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

## Quick reference

### Supported

| Feature | Notes |
|:---|:---|
| `SELECT`, `INSERT`, `UPDATE`, `DELETE` | [INSERT requires Big Data storage](insert-update-delete.md) |
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

## Big Data storage indexes

SeaTable automatically creates indexes for rows in big data storage to improve query performance. Indexed column types: text, number, date, single select, multiple select, collaborators, creator, create date, modifier, modification date.

Indexes are updated when:

1. The table is archived the next time
2. A user triggers index management from the "Big data management" menu in the base
