# SQL in SeaTable

SQL queries are the most powerful way access data stored in a base. If your not familiar with SQL syntax, we recommend using first the [SQL query plugin](https://seatable.com/help/anleitung-zum-sql-abfrage-plugin/). If some tables in a base are archived, archived rows are also queried, as well as rows that are not archived yet.

!!! info "Backticks for table or column names containing or special characters or using reserved words"
    For SQL queries, you can use numbers, special characters or spaces in the names of your tables and columns. However, you'll **have to** escape these names with backticks in order for your query to be correctly interpreted, for example `` SELECT * FROM `My Table` ``. 

    Similarly, if some of your of table or column names are the same as [SQL function](./functions.md) names (for example a date-type column named `date`), you'll also **have to** escape them in order for the query interpreter to understand that it's not a function call missing parameters, but rather a table or column name.

## Supported SQL Syntax

Currently only `SELECT`, `INSERT`, `UPDATE`, and `DELETE` statements are supported (the last three require version 2.7 or later). You'll find below the syntax for these statements. 

Please note that the SQL syntax is case insensitive: we use only upper-cased instructions here for ease of reading (differentiating SQL instructions from table or column names).

### Retrieving row(s)

!!! abstract "SELECT"
    The `SELECT` statement allows you to retrieve an eventually filtered, sorted and/or grouped list of the rows from a specific table. Each returned row is a JSON object. The keys of the object are the column **keys, NOT the column names**. To use column names as keys, the `convert_keys` parameter (available since version 2.4) in query request should be `true` (which is the default value when using `base.query` for both JavaScript and Python scripts).
    The syntax of `SELECT` statement is:

    ```
    SELECT [Column List] FROM tableName [Where Clause] [Group By Clause] [Having Clause] [Order By Clause] [Limit Option]
    ```

    `[Column List]` is the list of columns you want to retrieve, separated by commas. If you want to retrieve all the columns, you can use a wildcard (`*`).
    You can consult specific sections for [Where, Group By, Having or Order By clauses](#where-group-by-having-and-order-by-clauses)
    `Limit Option` uses MySQL format. The general syntax is `LIMIT ... OFFSET ...`. This parameters are optional. Unless you specify a higher limit, the method returns **a maximum of 100 rows**. The maximum number of rows returned is **10000** no matter the limit specified in the SQL statement. The `OFFSET` will help you retrieving the following rows in other queries

    __Example__ `SELECT * FROM Table1 LIMIT 10000` returns the first 10000 rows, `SELECT * FROM Table1 LIMIT 10000 OFFSET 10000` returns the next 10000 rows


    Since version 4.3, basic **implicit** *join* query is supported, for example:

    ```
    SELECT ... FROM Table1, Table2 WHERE Table1.column1 = Table2.column2 AND ...
    ```

    The *join* queries have the following restrictions:

    - You **must not** explicitly write JOIN keyword
    - Only *inner join* is supported; *left join*, *right join*, and *full join* are not supported.
    - Tables in the `FROM` clause should be unique (no duplicate tables).
    - Each table in the `FROM` clause should be associated with at least one join condition.
    - Join conditions should be placed in the `WHERE` clause, and eventually connected with one or more `AND` operators.
    - Join conditions can only use **equality operator** on columns, e.g. `Table1.column1 = Table2.column2`.
    - Columns in join conditions must be indexed, unless the table is not archived.

!!! info "Field aliases"
    Field alias with `AS` syntax is supported. For example, `SELECT table.a as a FROM table` returns rows whose first column is keyed by "a". There are two important points to note however:

    - Field alias can be referred in `GROUP BY`, `HAVING` and `ORDER BY` clauses. For example, `SELECT i.amount AS a, COUNT(*) FROM Invoices AS i GROUP BY a HAVING a > 100` is valid.
    - Field alias cannot be referred in `where` clause. E.g., `select t.registration as r, count(*) from t group by r where r > "2020-01-01"` will report syntax error.

!!! info "Aggregation functions"
    While retrieving rows, you can add aggregation functions to the list of columns if you specify a [GroupByClause](#where-group-by-having-and-order-by-clauses). The available functions are:

    - `COUNT` returns the number of non-empty values in a specific column or for all columns with `COUNT(*)`
    - `SUM` computes the sum of values in a specific column, for example `SUM(Invoices.Amount)`
    - `MAX` retrieves the greatest value in a specific column, for example `MAX(Invoices.Amount)`
    - `MIN` retrieves the smallest value in a specific column, for example `MIN(Invoices.Amount)`
    - `AVG` computes the average of non-empty values in a specific column, for example `AVG(Invoices.Amount)`

    __Example__

    ```
    SELECT Customer, SUM(Amount) from Invoices GROUP BY Customer
    ```

### Modifying database content

!!! abstract "INSERT"

    !!! warning "Enterprise subscription needed"

        `INSERT` requires [Big Data](https://seatable.com/help/big-data-capabilities/) storage support, which is available only with an [Enterprise subscription](https://seatable.com/help/subscription-plans/#seatable-cloud-enterprise-search).

    `INSERT` allows you to append a new row to a table. `INSERT` statement **only** supports bases that have been [archived](https://seatable.com/help/aktivieren-des-big-data-backends-in-einer-base/#designation-as-archivebackend-search). The rows will be inserted into big-data storage. It'll return error if the base is not archived yet. 
    
    
    If you want to insert rows in a non-archived base, please use the API dedicated functions (e.g. the [Python API](../python/objects/rows.md#add-rows)).

    ```
    INSERT INTO table_name [column_list] VALUES value_list [, ...]
    ```

    - `column_list` is a list of column names surrounded by parentheses. If omitted, it defaults to all updatable columns.
    - `value_list` is a list of values surrounded by parentheses. Values must be in the same order as the column list, for example: `(1, "2", 3.0)`.
    - Columns with multiple values, such as "multiple select"-type column , requires values to be surrounded by parentheses, for example: `(1, "2", 3.0, ("foo", "bar"))`.
    - Values of "single select" and "multiple select"-type columns must be option names, not option keys.
    - Few column types are **not allowed** to insert:

        - built-in columns, such as `_id`, `_ctime`.
        - image, file, formula, link, link-formula, geolocation, auto-number, button

    __Example__

    ```
    INSERT INTO Table1 (Name, Age) values ('Erika', 38)
    ```

!!! abstract "UPDATE"
    `UPDATE` allows you to update one or multiple existing rows of a table. Unlike the `INSERT` statement, `UPDATE` allows you to update rows in both normal and big-data storage. `WhereClause` is optional. However, keep in mind that if omitted, **all rows** will be updated!

      ```
      UPDATE table_name SET column_name = value [, ...] [WhereClause]
      ```

    - Columns with multiple values, such as "multiple select"-type column , requires values to be surrounded by parentheses, for example: `("foo", "bar")`.
    - Values of "single select" and "multiple select"-type columns must be option names, not option keys.
      - Few column types are **not allowed** to update:

        - built-in columns, such as `_id`, `_ctime`.
        - image, file, formula, link, link-formula, geolocation, auto-number, button

      __Example__

      ```
      UPDATE INTO Contacts SET Adult=true WHERE Age>=18
      ```

      __Example__

      ```
      UPDATE INTO Contacts SET Adult=true, `Age group`="18+" WHERE Age>=18
      ```

      If `Age group` is a "single select"-type column, the option you want to select (here "18+") has to exist already.

!!! abstract "DELETE"
    `DELETE` allows you to delete one or multiple existing rows of a table. Unlike the `INSERT` statement, `DELETE` allows you to delete rows in both normal and big-data storage. `WhereClause` is optional. However, keep in mind that if omitted, **all rows** will be deleted!

    ```
    DELETE FROM table_name [WhereClause]
    ```

    __Example__

    ```
    DELETE FROM Contacts WHERE Age<18
    ```


### WHERE, GROUP BY, HAVING and ORDER BY clauses

!!! abstract "WHERE clause"
    Most SQL syntax can be used in the `WHERE` clause, including arithmetic expressions, comparison operators, `[NOT] LIKE`, `IN`, `BETWEEN ... AND ...`, `AND`, `OR`, `NOT`, `IS [NOT] TRUE`, `IS [NOT] NULL`.
    
    - Arithmetic expressions only support numbers.
    - Time constants should be strings in ISO format (e.g. "2020-09-08 00:11:23"). Since 2.8 version, strings in RFC 3339 format are supported (such as "2020-12-31T23:59:60Z").

!!! abstract "GROUP BY clause"
    `GROUP BY` uses strict syntax. The selected fields must appear in the clause list, except for aggregation functions (`COUNT`, `SUM`, `MAX`, `MIN`, `AVG`) and formulas (see extended syntax section below).

!!! abstract "HAVING clause"
    `HAVING` filters rows resulting from the `GROUP BY` clause. Only fields referred in the `GROUP BY` clause or aggregation functions (such as "SUM") can be used in `HAVING` clause. Other syntax is the same as specified for the `WHERE` clause.

!!! abstract "ORDER BY clause"
    Fields in `ORDER BY` list must be a column or an expression in the selected fields. For example, `select a from table order by b` is invalid; while `select a, b from table order by b` and `select abs(a), b from table order by abs(a)` are valid.

### LIKE and BETWEEN operators

!!! abstract "LIKE operator"
    `LIKE` only supports strings. The key word `ILIKE` can be used instead of `LIKE` to make the match case insensitive. The percent sign `%` you will use in the `LIKE` expression represents zero, one, or multiple characters.

    __Example__ 
    ```
    SELECT `Full Name` from Contacts WHERE `Full Name` LIKE "% M%"
    ```
    returns every records with a last name starting with M (considering that the `Full Name` fields is actually composed like "`First Name` `Last Name`")

!!! abstract "BETWEEN operator"
    `BETWEEN lowerLimit AND upperLimit` only supports numbers and time. `lowerLimit` and `upperLimit` are included in the search. They have to be in the right order (if `upperLimit`<`lowerLimit`, no records will be found).

    __Example__ 
    ```
    SELECT * from Contacts WHERE Age BETWEEN 18 AND 25
    ``` 
    returns every records with a last name starting with M (considering that the `Full Name` fields is actually composed like `First Name` `Last Name`)


## Data types

### SeaTable <> SQL mapping

Below is the mapping of SeaTable column types to SQL data types.

| SeaTable column type  | SQL data type                                      | Query result format                                                                                                                                                     | Use in WHERE clause                                                                                                                                                                     | Use in GROUP BY / ORDER BY clause                      |
| :-------------------- | :--------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------- |
| text                  | String                                               |                                                                                                                                                                         | Supported                                                                                                                                                                               | Supported                                             |
| long-text             | String                                               | Raw text in Markdown format                                                                                                                                             | Supported                                                                                                                                                                               | Supported                                              |
| number                | Float                                                |                                                                                                                                                                         | Supported                                                                                                                                                                               | Supported                                              |
| single-select         | String                                               | Returned rows contain the option name. | Supported. Refer an option by its name. E.g. `WHERE single_select = "New York"`.                                                                                                                   | Order by the definition order of the options                 |
| multiple-select       | List of strings                                      | Returned rows contain the option names. | Supported. Refer an option by its name. E.g. `WHERE multi_select = "New York"`. More details in the "List types" section below.                                                                        | More details in the "List types" section below.            |
| checkbox              | Boolean                                                 |                                                                                                                                                                         | Supported                                                                                                                                                                               | Supported                                              |
| date                  | Datetime                                             | Time strings in RFC 3339 format                                                                                                                                         | Supported. Constants are expressed in strings in ISO format. e.g. "2006-1-2" or "2006-1-2 15:04:05". Since 2.8 version, strings in RFC 3339 format are supported (such as "2020-12-31T23:59:60Z"). | Supported                                              |
| image                 | List of URL for images                               | A JSON array with image URLs as elements                                                                                                                                | Supported. More details in the "List types" section below.                                                                                                                                  | Supported. More details in the "List types" section below. |
| file                  | Will be returned as JSON format string when queried. | Not supported                                                                                                                                                           | Not Supported                                                                                                                                                                           | Not Supported                                          |
| collaborator          | List of user IDs                                     | Format is like 5758ec...6d3388@auth.local. If you need user names, you have to convert with SeaTable APIs.                                             | Supported. More details in the "List types" section below.                                                                                                                                  | Supported. More details in the "List types" section below. |
| link to other records | List of linked rows                                  | Supported. More details in the "List types" section below.                                                                                                                  | Supported. More details in the "List types" section below.                                                                                                                                  | Supported. More details in the "List types" section below. |
| formula               | The type depends on the return value of the formula. | Depends on the type of the return value                                                                                                                                 | Depends on the type of the return value                                                                                                                                                 | Depends on the type of the return value                |
| \_creator             | User ID as string                                    | Format is like 5758ec...6d3388@auth.local. If you need user names, you have to convert with SeaTable APIs.                                             | Supported                                                                                                                                                                               | Supported                                              |
| \_ctime               | Datetime                                             | Time strings in RFC 3339 format                                                                                                                                         | Supported. Constants are expressed in strings in ISO format. e.g. "2006-1-2" or "2006-1-2 15:04:05". Since 2.8 version, strings in RFC 3339 format are supported (such as "2020-12-31T23:59:60Z"). | Supported                                              |
| \_last_modifier       | User ID as string                                    | Format is like 5758ec...6d3388@auth.local. If you need user names, you have to convert with SeaTable APIs.                                             | Supported                                                                                                                                                                               | Supported                                              |
| \_mtime               | Datetime                                             | Time strings in RFC 3339 format                                                                                                                                         | Supported. Constants are expressed in strings in ISO format. e.g. "2006-1-2" or "2006-1-2 15:04:05". Since 2.8 version, strings in RFC 3339 format are supported (such as "2020-12-31T23:59:60Z"). | Supported                                              |
| auto number           | String                                               |                                                                                                                                                                         | Supported                                                                                                                                                                               | Supported                                             |
| url                   | String                                               |                                                                                                                                                                         | Supported                                                                                                                                                                               | Supported                                             |
| email                 | String                                               |                                                                                                                                                                         | Supported                                                                                                                                                                               | Supported                                             |
| duration              | Float                                                | Returned in seconds                                                                                                                                         | Supported                                                                                                                                                                               | Supported                                             |

### List types

In SeaTable, two categories of column types are list types (columns with multiple values):

- Built-in list types: including multiple selection, image, file, collaborator and link to other records.
- Formula columns dealing with linked records (using either `{link.column}` or `lookup`) and link formula columns whose formula is `lookup`, `findmin` or `findmax`.

When referring to a list-type column in a `WHERE` clause, the following rules apply, depending on the type for the list elements. If an operator is not listed below, it's unsupported.

| Element Type  | Operator                                        | Rule                                                                                                                                                   |
| :------------ | :---------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------- |
| string        | `IN`, extended list operators (e.g. `HAS ANY OF`) | Follow the rules of the operator.                                                                                                                      |
| string        | `LIKE`, `ILIKE`                                     | Always take the first element for comparison; if there is no element, use an empty string (""). 
                                                  |
| string        | `IS NULL`                                         | Return `true` when the list is empty or when there is no data in the cell.                                                                                           |
| string        | =, !=                                           | Always take the first element for comparison; if there is no element, use an empty string ("").                                                           |
| float         | `IN`, extended list operators (e.g. `HAS ANY OF`) | Follow the rules of the operator.                                                                                                                      |
| float         | =, !=, <, <=, >, >=, between                  | If there is only 1 element, use that element; otherwise only return `true` for `!=` operator.                                                          |
| float         | `IS NULL`                                         | Return `true` when the list is empty or when there is no data in the cell.                                                                                           |
| float         | Arithmetics operations such as +, -, * or /                   | Use the first element for calculation.                                                                                                                 |
| Datetime      | `IN`, extended list operators (e.g. `HAS ANY OF`) | Follow the rules of the operator.                                                                                                                      |
| Datetime      | =, !=, <, <=, >, >=, between                  | If there is only 1 element, use that element; otherwise only return `true` for `!=` operator.                                                          |
| Datetime      | `IS NULL`                                         | Return `true` when the list is empty or when there is no data in the cell.                                                                                           |
| bool          | `IS TRUE`                                         | Always take the first element for comparison; return false if there are no elements.
| linked record |                                                 | Follow the rules for the type of the display column.                                                                                                   |

When a list column is returned in a selected field, only the ten first elements are returned.

When used in `GROUP BY` or `ORDER BY` clauses, the elements for each list will first be sorted in ascending order, then the lists will be sorted by the rules below:

- Compare the elements one by one, list with smaller element is sorted before list with larger element.
- If all elements compared in step 1 are equal, shorter list is sorted before longer list.
- Otherwise the tow lists are equal.

If a list column is passed as parameter to a formula, and the parameter expects a scalar value, the first element will be used. And if the element is a linked record, the value of its display column will be used.

When applying aggregate functions (min, max, sum, avg) to a list column, if there is only 1 element in the list, use that element; otherwise this row will not be aggregated.

### NULL values

NULL value is distinct from 0. It represents a missing value. The following values are treated as NULL:

- Empty cells in a table.
- Values which cannot be converted to the column type.
- Empty strings (""). This is different from standard SQL.
- Lists are treated as NULL based on the rules described in the "List Types" section.
- Functions or formula columns that return error.

In the `WHERE` clause:

- Arithmetics operations such as +, -, * or / on NULL values will return NULL.
- `!=`, `NOT LIKE`, `NOT IN`, `NOT BETWEEN`, `HAS NONE OF`, `IS NOT TRUE`, and `IS NULL` operations will return `true` when the value is NULL.
- `AND`, `OR`, `NOT` treat NULL values as `false`.
- Aggregate functions (min, max, sum, avg) will ignore NULL values.

In formulas, NULL values will be converted to 0 or an empty string.

## Extended syntax

### Using formulas in SQL query

You may use a formula syntax that's almost the same as SeaTable's formulas in SQL queries. There are a few special notes:

- Link formulas are not supported. e.g. {link.age} is invalid.
- Reference to columns should not be enclosed by curly brackets ("{}"). Don't write `SELECT abs({column}) FROM table`. Write `SELECT abs(column) FROM table`. This is consistent with standard SQL syntax.
- You have to use backticks ("\`\`") to enclose column references, when column name contains space or "-". E.g. ```SELECT abs(`column-a`) FROM table```.
- You cannot use column alias in formulas. E.g. `SELECT abs(t.column) FROM table AS t;` is invalid.
- Formulas can be used in `GROUP BY` and `ORDER BY` clauses.

For an exhaustive list of available functions, please refer to the complete [function reference](./functions.md).

### Extended list operators

Some column types in SeaTable have list values. The SeaTable UI supports a few special filters for such types, which are `HAS ANY OF`, `HAS ALL OF`, `HAS NONE OF` and `IS EXACTLY`. You can use the same syntax to filter such columns with SQL. For all these operators, the list of string constant are enclosed with brackets, just like the syntax for `IN`. Please note that the order of values in the list is not taken into account.

__Example__ `SELECT * FROM table WHERE city HAS ANY OF ("New York", "Paris")` will retrieve all rows that contain either "New York" or "Paris" in the "multiple select"-type column `city`

## Big Data storage indexes

To improve query performance, SeaTable will automatically create indexes for the rows stored in big data storage engine. Currently, text, number, date, single select, multiple select, collaborators, creator, create date, modifier and modification date columns are indexed.

When you add or delete a column in a table, the index for this column is not added/removed immediately. Indexes creation and deletion are triggered in two cases:

1. When you archive the table for the next time, indexes are created for new columns and indexes for removed columns are removed.
2. Users may manage indexes from "index management" UI. You can open it from the "Big data management" menu in the base.
