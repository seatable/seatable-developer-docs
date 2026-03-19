# SELECT

The `SELECT` statement retrieves an optionally filtered, sorted, and grouped list of rows from a table. Each returned row is a JSON object.

## Syntax

```
SELECT [Column List] FROM tableName [WHERE ...] [GROUP BY ...] [HAVING ...] [ORDER BY ...] [LIMIT ... OFFSET ...]
```

`[Column List]` is a comma-separated list of columns. Use `*` to retrieve all columns.

See [Clauses](clauses.md) for details on WHERE, GROUP BY, HAVING, and ORDER BY.

## Limits

Unless you specify a higher limit, the method returns a maximum of **100 rows**. The absolute maximum is **10,000 rows**.

__Example__

```
SELECT * FROM Table1 LIMIT 10000
```

Returns the first 10,000 rows.

```
SELECT * FROM Table1 LIMIT 10000 OFFSET 10000
```

Returns the next 10,000 rows.

## Column keys vs. column names

By default, returned rows use column **names** as keys (when using `base.query` in Python or JavaScript). The raw API returns column **keys**. This can be controlled with the `convert_keys` parameter.

## JOIN

Since version 4.3, basic implicit join queries are supported:

```
SELECT ... FROM Table1, Table2 WHERE Table1.column1 = Table2.column2 AND ...
```

Restrictions:

- Do **not** use the `JOIN` keyword explicitly
- Only inner join is supported (no left, right, or full join)
- Tables in the `FROM` clause must be unique
- Each table must have at least one join condition
- Join conditions use equality only: `Table1.column1 = Table2.column2`
- Join conditions must be placed in the `WHERE` clause, connected with `AND`
- Columns in join conditions must be indexed (unless the table is not archived)

## Field aliases

Field aliases with `AS` are supported:

```
SELECT table.amount AS a, COUNT(*) FROM Invoices AS i GROUP BY a HAVING a > 100
```

- Aliases **can** be used in `GROUP BY`, `HAVING`, and `ORDER BY`
- Aliases **cannot** be used in `WHERE`

## Aggregation functions

When using `GROUP BY`, these aggregation functions are available:

| Function | Description | Example |
|---|---|---|
| `COUNT(*)` | Number of rows | `COUNT(*)` |
| `SUM(col)` | Sum of values | `SUM(Amount)` |
| `MAX(col)` | Maximum value | `MAX(Amount)` |
| `MIN(col)` | Minimum value | `MIN(Amount)` |
| `AVG(col)` | Average of non-empty values | `AVG(Amount)` |

__Example__

```
SELECT Customer, SUM(Amount) FROM Invoices GROUP BY Customer
```
