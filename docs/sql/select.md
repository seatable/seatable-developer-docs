# SELECT

The `SELECT` statement retrieves an optionally filtered, sorted, and grouped list of rows from a table. Each returned row is a JSON object. `SELECT` works the same way regardless of whether the table uses normal or Big Data storage.

## Syntax

```
SELECT [Column List]
  FROM tableName
  [WHERE ...]
  [GROUP BY ...]
  [HAVING ...]
  [ORDER BY ...]
  [LIMIT ... OFFSET ...]
```

`[Column List]` is a comma-separated list of columns. Use `*` to retrieve all columns.

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

## DISTINCT

Use `DISTINCT` to return only unique values:

```
SELECT DISTINCT city FROM Contacts
```

## Field aliases

Field aliases with `AS` are supported:

```
SELECT table.amount AS a, COUNT(*) FROM Invoices AS i GROUP BY a HAVING a > 100
```

- Aliases **can** be used in `GROUP BY`, `HAVING`, and `ORDER BY`
- Aliases **cannot** be used in `WHERE`

## WHERE

!!! info "Backticks for special names"
    Escape table or column names that contain spaces, special characters, or match [SQL function](./functions.md) names with backticks: `` SELECT * FROM `My Table` ``.

Most SQL syntax can be used in the `WHERE` clause: arithmetic expressions, comparison operators, `[NOT] LIKE`, `IN`, `BETWEEN ... AND ...`, `AND`, `OR`, `NOT`, `IS [NOT] TRUE`, `IS [NOT] NULL`.

- Arithmetic expressions only support numbers
- Time constants must be strings in ISO format (e.g. `"2020-09-08 00:11:23"`). Since version 2.8, RFC 3339 format is also supported (e.g. `"2020-12-31T23:59:60Z"`)

### LIKE

`LIKE` only supports strings. Use `ILIKE` for case-insensitive matching. The percent sign `%` represents zero, one, or multiple characters.

__Example__

```
SELECT `Full Name` FROM Contacts WHERE `Full Name` LIKE "% M%"
```

Returns every record with a last name starting with M.

### BETWEEN

`BETWEEN lowerLimit AND upperLimit` supports numbers and time. Both limits are included. They must be in the correct order.

__Example__

```
SELECT * FROM Contacts WHERE Age BETWEEN 18 AND 25
```

### Extended list operators

SeaTable supports special operators for list-type columns (multiple select, collaborator, etc.):

| Operator | Description |
|---|---|
| `HAS ANY OF` | Row contains at least one of the values |
| `HAS ALL OF` | Row contains all of the values |
| `HAS NONE OF` | Row contains none of the values |
| `IS EXACTLY` | Row contains exactly these values (order-independent) |

Values are enclosed in parentheses, like the `IN` operator.

__Example__

```
SELECT * FROM table WHERE city HAS ANY OF ("New York", "Paris")
```

## GROUP BY

`GROUP BY` uses strict syntax. Selected fields must appear in the GROUP BY list, except for aggregation functions (`COUNT`, `SUM`, `MAX`, `MIN`, `AVG`) and formulas.

## HAVING

`HAVING` filters rows resulting from `GROUP BY`. Only fields in the GROUP BY list or aggregation functions can be used. Other syntax is the same as WHERE.

## ORDER BY

Fields in the `ORDER BY` list can be columns, expressions, or functions.

__Example__

```
SELECT name, age FROM table ORDER BY age DESC
SELECT name, abs(score) FROM table ORDER BY abs(score)
```

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

## JOIN

Since version 4.3, basic implicit join queries are supported:

```
SELECT ...
  FROM Table1, Table2
  WHERE Table1.column1 = Table2.column2
    AND ...
```

Restrictions:

- Do **not** use the `JOIN` keyword explicitly
- Only inner join is supported (no left, right, or full join)
- Tables in the `FROM` clause must be unique
- Each table must have at least one join condition
- Join conditions use equality only: `Table1.column1 = Table2.column2`
- Join conditions must be placed in the `WHERE` clause, connected with `AND`
- Columns in join conditions must be indexed (unless the table is not archived)
