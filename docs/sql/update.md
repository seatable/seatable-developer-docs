---
description: SeaTable SQL UPDATE syntax — modify rows with WHERE conditions and constant values.
---

# UPDATE

Updates one or more rows in a table. Works with both normal and Big Data storage.

## Syntax

```sql
UPDATE tableName
  SET column1 = value [, column2 = value, ...]
  [WHERE ...]
```

!!! warning "No WHERE = update all rows"

    If you omit the WHERE clause, **all rows** in the table will be updated.

The `value` in SET must be a **constant** (string, number, or boolean). Expressions and [functions](functions.md) are not supported in SET — see [not supported features](index.md#not-supported) for alternatives.

The same column restrictions and multi-value rules as [INSERT](insert.md) apply. Not all column types can be written via SQL — see [column writability](limitations.md#column-writability) for details.

`LIMIT` is not supported in `UPDATE` statements.

## Setting values to NULL

To clear a cell, set the column to `NULL`. Setting a text column to an empty string `""` also results in NULL — see [NULL values](limitations.md#null-values).

```sql
UPDATE Contacts SET City=NULL WHERE Name="Alice"
```

## Response

`UPDATE` returns `success: true` on success. The response does not include the number of affected rows. If no rows match the WHERE condition, the response is still `success: true`.

```json
{
  "success": true,
  "metadata": null,
  "results": null
}
```

## Examples

Update a single column:

```sql
UPDATE Contacts SET Adult=true WHERE Age>=18
```

Update multiple columns at once:

```sql
UPDATE Contacts SET Adult=true, `Age group`="18+" WHERE Age>=18
```
