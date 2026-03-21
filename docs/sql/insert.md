# INSERT

Appends a new row to a table via SQL.

!!! warning "Big Data storage only"

    `INSERT` **only** works with bases that have [Big Data storage](https://seatable.com/help/big-data-capabilities/) enabled. Rows are inserted into big data storage. This feature requires an [Enterprise subscription](https://seatable.com/help/subscription-plans/#seatable-cloud-enterprise-search).

For non-archived bases, use the API functions instead (e.g. [Python `append_row`](/python/objects/rows/#add-rows) or [JavaScript `appendRow`](/javascript/rows/)).

## Syntax

```sql
INSERT INTO tableName (column1, column2, ...)
  VALUES (value1, value2, ...)
```

- Values must be constants (strings, numbers, booleans) — functions and expressions are **not** supported in `VALUES`
- Multi-value columns (e.g. multiple select): use nested parentheses: `("foo", "bar")`
- Single/multiple select values must be option **names**, not keys
- Not all column types can be written via SQL — see [Limitations](limitations.md#column-writability) for details

__Example__

```sql
INSERT INTO Table1 (Name, Age) VALUES ('Erika', 38)
```
