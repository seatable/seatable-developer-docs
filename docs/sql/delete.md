---
description: SeaTable SQL DELETE syntax — remove rows with WHERE conditions.
---

# DELETE

Deletes one or more rows from a table. Works with both normal and Big Data storage.

## Syntax

```sql
DELETE FROM tableName
  [WHERE ...]
```

!!! warning "No WHERE = delete all rows"

    If you omit the WHERE clause, **all rows** in the table will be deleted.

`LIMIT` is not supported in `DELETE` statements.

## Response

`DELETE` returns `success: true` on success. The response does not include the number of deleted rows. If no rows match the WHERE condition, the response is still `success: true`.

```json
{
  "success": true,
  "metadata": null,
  "results": null
}
```

## Examples

Delete rows matching a condition:

```sql
DELETE FROM Contacts WHERE Age<18
```

Delete rows with empty values:

```sql
DELETE FROM Contacts WHERE City IS NULL
```
