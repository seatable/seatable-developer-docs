# INSERT, UPDATE, DELETE

These statements modify data in a base. Available since SeaTable version 2.7.

## INSERT

Appends a new row to a table. `INSERT` **only** works with bases that have [Big Data storage](https://seatable.com/help/big-data-capabilities/) enabled. Rows are inserted into big data storage.

!!! warning "Enterprise subscription needed"

    `INSERT` requires Big Data storage support, which is available only with an [Enterprise subscription](https://seatable.com/help/subscription-plans/#seatable-cloud-enterprise-search).

For non-archived bases, use the API functions instead (e.g. [Python `append_row`](/python/objects/rows/#add-rows) or [JavaScript `appendRow`](/javascript/rows/)).

### Syntax

```
INSERT INTO table_name [column_list] VALUES value_list [, ...]
```

- `column_list`: column names in parentheses. If omitted, defaults to all updatable columns.
- `value_list`: values in parentheses, matching the column order: `(1, "text", 3.0)`
- Multi-value columns (e.g. multiple select): use nested parentheses: `(1, "text", ("foo", "bar"))`
- Single/multiple select values must be option **names**, not keys

### Column restrictions

These column types cannot be inserted: `_id`, `_ctime` (built-in), image, file, formula, link, link-formula, geolocation, auto-number, button.

__Example__

```
INSERT INTO Table1 (Name, Age) VALUES ('Erika', 38)
```

## UPDATE

Updates one or multiple rows. Works with both normal and big data storage.

### Syntax

```
UPDATE table_name SET column_name = value [, ...] [WHERE ...]
```

!!! warning "No WHERE = update all rows"

    If you omit the WHERE clause, **all rows** will be updated.

!!! warning "Only constant values in SET"

    The `value` in SET must be a constant (string, number, or boolean). Functions, arithmetic expressions, and column references are **not supported** in SET. They can only be used in SELECT and WHERE.

The same column restrictions and multi-value rules as INSERT apply.

__Example__

```
UPDATE Contacts SET Adult=true WHERE Age>=18
```

```
UPDATE Contacts SET Adult=true, `Age group`="18+" WHERE Age>=18
```

## DELETE

Deletes one or multiple rows. Works with both normal and big data storage.

### Syntax

```
DELETE FROM table_name [WHERE ...]
```

!!! warning "No WHERE = delete all rows"

    If you omit the WHERE clause, **all rows** will be deleted.

__Example__

```
DELETE FROM Contacts WHERE Age<18
```
