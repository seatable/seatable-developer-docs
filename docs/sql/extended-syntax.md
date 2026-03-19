# Extended Syntax

## Formulas in SQL queries

You can use SeaTable formula syntax directly in SQL queries. A few differences from SeaTable's built-in formulas:

- Link formulas (e.g. `{link.age}`) are **not** supported
- Column references are **not** enclosed in curly brackets: use `abs(column)`, not `abs({column})`
- Use backticks for column names with spaces or hyphens: `` abs(`column-a`) ``
- Column aliases cannot be used in formulas: `abs(t.column)` is invalid
- Formulas can be used in `GROUP BY` and `ORDER BY` clauses

For the complete list of available functions, see the [function reference](./functions.md).

## Extended list operators

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

## Big Data storage indexes

SeaTable automatically creates indexes for rows in big data storage to improve query performance. Indexed column types: text, number, date, single select, multiple select, collaborators, creator, create date, modifier, modification date.

Indexes are updated when:

1. The table is archived the next time
2. A user triggers index management from the "Big data management" menu in the base
