# Data Types

## SeaTable to SQL mapping

| SeaTable column type | SQL data type | Query result format | WHERE | GROUP BY / ORDER BY | Writable via SQL |
|:---|:---|:---|:---|:---|:---|
| text | String | | Supported | Supported | Yes |
| long-text | String | Raw Markdown | Supported | Supported | Yes |
| number | Number | Integer or float | Supported | Supported | Yes |
| single-select | String | Option name | By option name | By definition order | Yes |
| multiple-select | List of strings | Option names | By option name | See list types | Yes |
| checkbox | Boolean | | Supported | Supported | Yes |
| date | Datetime | RFC 3339 format | ISO or RFC 3339 strings | Supported | Yes |
| duration | Number | In seconds | Supported | Supported | Yes |
| rate | Integer | 1 to max | Supported | Supported | Yes |
| url | String | | Supported | Supported | Yes |
| email | String | | Supported | Supported | Yes |
| image | List of URLs | JSON array | See list types | See list types | **No** |
| file | JSON string | | Not supported | Not supported | **No** |
| collaborator | List of user IDs | `xxx@auth.local` | See list types | See list types | Yes |
| link | List of linked rows | | See list types | See list types | **No** |
| link-formula | Depends on return value | | Depends on type | Depends on type | **No** |
| formula | Depends on return value | | Depends on type | Depends on type | **No** |
| geolocation | JSON object | `{"country_region": "..."}` or `{"lat": ..., "lng": ...}` | Not supported | Not supported | **No** |
| auto-number | String | | Supported | Supported | **No** |
| digital-sign | String | Username | Not supported | Not supported | **No** |
| button | — | Not queryable | — | — | **No** |
| \_creator | String (user ID) | `xxx@auth.local` | Supported | Supported | **No** |
| \_ctime | Datetime | RFC 3339 format | ISO or RFC 3339 strings | Supported | **No** |
| \_last\_modifier | String (user ID) | `xxx@auth.local` | Supported | Supported | **No** |
| \_mtime | Datetime | RFC 3339 format | ISO or RFC 3339 strings | Supported | **No** |

## List types

Two categories of columns have list values:

- **Built-in**: multiple select, image, file, collaborator, link to other records
- **Formula-based**: link formulas using `lookup`, `findmin`, or `findmax`

### WHERE clause rules for list types

| Element type | Operator | Rule |
|:---|:---|:---|
| string | `IN`, `HAS ANY OF`, etc. | Follow operator rules |
| string | `LIKE`, `ILIKE` | Uses first element; empty string if no element |
| string | `IS NULL` | True when list is empty |
| string | `=`, `!=` | Uses first element |
| float | `IN`, `HAS ANY OF`, etc. | Follow operator rules |
| float | `=`, `!=`, `<`, `<=`, `>`, `>=`, `BETWEEN` | Uses single element; only `!=` returns true for multiple |
| float | `IS NULL` | True when list is empty |
| float | `+`, `-`, `*`, `/` | Uses first element |
| datetime | Same rules as float | |
| bool | `IS TRUE` | Uses first element; false if empty |
| linked record | | Follows rules for the display column type |

Only the first ten elements are returned in query results.

### Sorting list types

In GROUP BY / ORDER BY, elements are first sorted ascending within each list, then lists are compared element by element. Shorter lists sort before longer lists when all compared elements are equal.

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
