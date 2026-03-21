---
description: SeaTable SQL limitations — read-only column types, list column behavior, NULL handling, and Big Data storage index management.
---

# Limitations

This page documents SQL-specific behavior and restrictions. For general column type definitions, see the [API column model reference](https://api.seatable.com/reference/models).

## Column writability

Not all column types can be written via SQL (`INSERT`, `UPDATE`). The following columns are **read-only** in SQL:

| Column type | Readable | Writable | Notes |
|:---|:---:|:---:|:---|
| image | Yes | **No** | Use API to upload/update |
| file | Limited | **No** | WHERE and ORDER BY not supported |
| link | Yes | **No** | Use API to manage links |
| link-formula | Yes | **No** | Computed from links |
| formula | Yes | **No** | Computed value |
| geolocation | Yes | **No** | WHERE and ORDER BY not supported; use `country()` function to query |
| auto-number | Yes | **No** | System-managed sequence |
| digital-sign | Limited | **No** | WHERE and ORDER BY not supported |
| button | **No** | **No** | Not queryable |
| \_creator, \_ctime | Yes | **No** | System-managed |
| \_last\_modifier, \_mtime | Yes | **No** | System-managed |

All other column types (text, long-text, number, single-select, multiple-select, checkbox, date, duration, rate, url, email, collaborator) are both readable and writable.

## List types

Several column types contain multiple values: multiple-select, image, file, collaborator, link, and link formulas using `lookup`, `findmin`, or `findmax`.

### WHERE rules for list types

| Element type | Operator | Rule |
|:---|:---|:---|
| string | `IN`, `HAS ANY OF`, etc. | Follow operator rules |
| string | `LIKE`, `ILIKE` | Uses first element; empty string if no element |
| string | `IS NULL` | True when list is empty |
| string | `=`, `!=` | Uses first element |
| float | `=`, `!=`, `<`, `<=`, `>`, `>=`, `BETWEEN` | Uses single element; only `!=` returns true for multiple |
| float | `IS NULL` | True when list is empty |
| float | `+`, `-`, `*`, `/` | Uses first element |
| datetime | Same rules as float | |
| bool | `IS TRUE` | Uses first element; false if empty |
| linked record | | Follows rules for the display column type |

### Sorting list types

In `GROUP BY` / `ORDER BY`, elements are first sorted ascending within each list, then lists are compared element by element. Shorter lists sort before longer lists when all compared elements are equal.

### Aggregation on list types

For `MIN`, `MAX`, `SUM`, `AVG`: if the list has exactly one element, that element is used. Otherwise the row is not aggregated.

## NULL values

NULL represents a missing value (distinct from 0). These are treated as NULL:

- Empty cells
- Values that cannot be converted to the column type
- Empty strings (`""`)
- Empty lists (see list types rules)
- Formulas that return an error

### NULL in WHERE

- Arithmetic on NULL returns NULL
- `!=`, `NOT LIKE`, `NOT IN`, `NOT BETWEEN`, `HAS NONE OF`, `IS NOT TRUE`, `IS NULL` return `true` for NULL
- `AND`, `OR`, `NOT` treat NULL as `false`
- Aggregate functions ignore NULL values

In formulas, NULL is converted to 0 or empty string.

## Big Data storage indexes

SeaTable automatically creates indexes for rows in big data storage to improve query performance. Indexed column types: text, number, date, single select, multiple select, collaborators, creator, create date, modifier, modification date.

Indexes are updated when:

1. The table is archived the next time
2. A user triggers index management from the "Big data management" menu in the base
