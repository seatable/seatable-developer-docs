# INSERT

Appends a new row to a table via SQL.

!!! warning "Big Data storage only"

    `INSERT` **only** works with bases that have [Big Data storage](https://seatable.com/help/big-data-capabilities/) enabled. Rows are inserted into big data storage. This feature requires an [Enterprise subscription](https://seatable.com/help/subscription-plans/#seatable-cloud-enterprise-search).

For non-archived bases, use the API functions instead (e.g. [Python `append_row`](/python/objects/rows/#add-rows) or [JavaScript `appendRow`](/javascript/rows/)).

Available since SeaTable version 2.7.

## Syntax

```
INSERT INTO table_name [column_list] VALUES value_list [, ...]
```

- `column_list`: column names in parentheses. If omitted, defaults to all updatable columns.
- `value_list`: values in parentheses, matching the column order: `(1, "text", 3.0)`
- Multi-value columns (e.g. multiple select): use nested parentheses: `(1, "text", ("foo", "bar"))`
- Single/multiple select values must be option **names**, not keys

## Column restrictions

These column types cannot be inserted: `_id`, `_ctime` (built-in), image, file, formula, link, link-formula, geolocation, auto-number, button.

__Example__

```
INSERT INTO Table1 (Name, Age) VALUES ('Erika', 38)
```
