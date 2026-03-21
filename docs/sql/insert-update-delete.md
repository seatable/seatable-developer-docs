# UPDATE and DELETE

These statements modify existing data in a base. They work with both normal and Big Data storage.

## UPDATE

Updates one or multiple rows.

### Syntax

```
UPDATE tableName
  SET column1 = value [, ...]
  [WHERE ...]
```

!!! warning "No WHERE = update all rows"

    If you omit the WHERE clause, **all rows** will be updated.

!!! warning "Only constant values in SET"

    The `value` in SET must be a constant (string, number, or boolean). Functions, arithmetic expressions, and column references are **not supported** in SET. They can only be used in `SELECT`, `WHERE`, `GROUP BY`, `HAVING`, and `ORDER BY`.

The same column restrictions and multi-value rules as [INSERT](insert.md) apply.

__Example__

```
UPDATE Contacts SET Adult=true WHERE Age>=18
```

```
UPDATE Contacts SET Adult=true, `Age group`="18+" WHERE Age>=18
```

## DELETE

Deletes one or multiple rows.

### Syntax

```
DELETE FROM tableName
  [WHERE ...]
```

!!! warning "No WHERE = delete all rows"

    If you omit the WHERE clause, **all rows** will be deleted.

__Example__

```
DELETE FROM Contacts WHERE Age<18
```
