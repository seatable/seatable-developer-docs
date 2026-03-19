# Clauses

## WHERE

Most SQL syntax can be used in the `WHERE` clause: arithmetic expressions, comparison operators, `[NOT] LIKE`, `IN`, `BETWEEN ... AND ...`, `AND`, `OR`, `NOT`, `IS [NOT] TRUE`, `IS [NOT] NULL`.

- Arithmetic expressions only support numbers
- Time constants must be strings in ISO format (e.g. `"2020-09-08 00:11:23"`). Since version 2.8, RFC 3339 format is also supported (e.g. `"2020-12-31T23:59:60Z"`)

## GROUP BY

`GROUP BY` uses strict syntax. Selected fields must appear in the GROUP BY list, except for aggregation functions (`COUNT`, `SUM`, `MAX`, `MIN`, `AVG`) and formulas.

## HAVING

`HAVING` filters rows resulting from `GROUP BY`. Only fields in the GROUP BY list or aggregation functions can be used. Other syntax is the same as WHERE.

## ORDER BY

Fields in the `ORDER BY` list must be a column or expression that appears in the selected fields.

__Valid:__
```
SELECT a, b FROM table ORDER BY b
SELECT abs(a), b FROM table ORDER BY abs(a)
```

__Invalid:__
```
SELECT a FROM table ORDER BY b
```

## LIKE

`LIKE` only supports strings. Use `ILIKE` for case-insensitive matching. The percent sign `%` represents zero, one, or multiple characters.

__Example__

```
SELECT `Full Name` FROM Contacts WHERE `Full Name` LIKE "% M%"
```

Returns every record with a last name starting with M.

## BETWEEN

`BETWEEN lowerLimit AND upperLimit` supports numbers and time. Both limits are included. They must be in the correct order.

__Example__

```
SELECT * FROM Contacts WHERE Age BETWEEN 18 AND 25
```
