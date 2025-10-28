# SQL function reference

With functions you can transform, calculate, combine or merge the values of other columns from the current table. On top of that, functions can refer to each other. In this article, we will show you a complete overview of all functions with examples. If you are looking for a specific function, you can use Ctrl+F or ⌘+F to quickly find an entry on this page.

The functions supported in SQL are roughly the same as the set of functions supported by formulas in SeaTable. The function parameters can be numbers, strings, constants, column names or other functions. Column name cannot be an alias. The function can be classified into the following categories: 

- [Operators](#operators)
- [Mathematical functions](#mathematical-functions)
- [Text functions](#text-functions)
- [Date functions](#date-functions)
- [Geo functions](#geo-functions)
- [Logical functions](#logical-functions)
- [Statistical functions](#statistical-functions)

!!! info "Backticks for table or column names containing or special characters or using reserved words"
    For SQL queries, you can use numbers, special characters or spaces in the names of your tables and columns. However, you'll **have to** escape these names with backticks in order for your query to be correctly interpreted, for example `` select * from `My Table` ``. 

    Similarly, if some of your of table or column names are the same as SQL function names (for example a date-type column named `date`), you'll also **have to** escape them in order for the query interpreter to understand that it's not a function call missing parameters, but rather a table or column name.


## Constants

You can use the following constants in the functions:

| VARIABLE | DESCRIPTION                             |
| :------- | :-------------------------------------- |
| `e`      | Returns the Euler number e=2.71828...   |
| `pi`     | Returns the circle number π=3.14159...  |
| `true`   | Returns the logical value `true`.       |
| `false`  | Returns the logical value `false`.      |

## Operators

Parameters must be strings or numbers. If a number is passed to a parameter that expects a string, it'll be converted to string, and vice versa.

### Arithmetic operators

!!! abstract "add"
    Adds two numeric values (`num1` and `num2`) and returns the result.

    ```
    add(num1,num2)
    ```

    __Example__ `add(1,2)` returns `3`

!!! abstract "substract"
    Subtracts one numeric value (`num2`) from another (`num1`).

    ```
    substract(num1,num2)
    ```

    __Example__ `substract(5,4)` returns `1`

!!! abstract "multiply"
    Multiplies two numeric values.

    ```
    multiply(num1,num2)
    ```

    __Example__ `multiply(3,4)` returns `12`

!!! abstract "divide"
    Divides one numeric value (`num1`) by another (`num2`).

    ```
    divide(num1,num2)
    ```

    __Example__ `divide(3,2)` returns `1.5`

!!! abstract "mod"
    Calculates the remainder of a division.

    ```
    mod(num1,num2)
    ```

    __Example__ `divide(15,7)` returns `1`

!!! abstract "power"
    Calculates the power (`num2`) of a number (`num1`).

    ```
    power(num1,num2)
    ```

    __Example__ `power(3,2)` returns `9`

### Greater-Less comparisons

!!! abstract "greater"
    Checks if a numeric value (`num1`) is greater than another (`num2`) and returns the logical value `true` or `false`.

    ```
    greater(num1,num2)
    ```

    __Example__ `greater(2,3)` returns `false`

!!! abstract "lessthan"
    Checks if a numeric value (`num1`) is less than another (`num2`) and returns the logical value `true` or `false`.

    ```
    lessthan(num1,num2)
    ```

    __Example__ `lessthan(2,3)` returns `true`

!!! abstract "greatereq"
    Checks if a numeric value (`num1`) is greater than or equal to another (`num2`) and returns the logical value `true` or `false`.

    ```
    greatereq(num1,num2)
    ```

    __Example__ `greatereq(2,2)` returns `true`

!!! abstract "lessthaneq"
    Checks if a numeric value (`num1`) is less than or equal to another (`num2`) and returns the logical value `true` or `false`.

    ```
    lessthaneq(num1,num2)
    ```

    __Example__ `lessthaneq(2,2)` returns `true`


### Equal-Not equal comparisons

The functions work for both numbers and strings.

!!! abstract "equal"
    Checks if two values (`num1`, `num2`) are equal and returns the logical value `true` or `false`.

    ```
    equal(num1,num2)
    ```

    __Example__  ```equal(`Old price`,`New price`)``` compares the content of the `Old price` and the `New price` columns and returns `true` or `false` accordingly

!!! abstract "unequal"
    Checks if two values (`num1`, `num2`) are not equal and returns the logical value `true` or `false`.

    ```
    unequal(num1,num2)
    ```

    __Example__ ```unequal(`Single select`,"Option 1")``` compares the content of the `Single select` column to the string "Option 1" and returns `true` or `false` accordingly

## Mathematical functions

Parameters must be numbers. If a string is passed as parameter, it will be converted to number.

!!! abstract "abs"
    Returns the absolute value of a `number`.
    
    ```
    abs(number)
    ```
    
    __Example__ `abs(-2)` returns `2`

!!! abstract "ceiling"
    Rounds a `number` to the nearest greater integer or to the nearest greater multiple of the specified `significance`. If either argument is non-numeric, the formula returns an empty value.
    
    ```
    ceiling(number, significance)
    ```
    
    __Example__ `ceiling(2.14)` returns `3`

    If the `number` is an exact multiple of the `significance`, then no rounding occurs. If the `number` and the `significance` are negative, then the rounding is away from 0. If the `number` is negative and the `significance` is positive, then the rounding is towards 0.
    
    
    __Example__ `ceiling(-2.14, 4)` returns `0`

!!! abstract "even"
    Returns the nearest greater even `number`.
    
    ```
    even(number)
    ```
    
    __Example__ `even(2.14)` returns `4`

!!! abstract "exp"
    Exponential function for Euler's `number` e. Returns the value of e to the power of `number`.
    
    ```
    exp(number)
    ```
    
    __Example__ `exp(1)` returns `2.71828...`

!!! abstract "floor"
    Rounds a `number` to the nearest smaller integer or to the nearest smaller multiple of the specified `significance`. If either argument is non-numeric, the formula returns an empty value.
    
    ```
    floor(number, significance)
    ```
    
    __Example__ `floor(2.86)` returns `2`

    If the `number` is an exact multiple of the `significance`, then no rounding takes place. If the sign of the `number` is positive, then the rounding is towards 0. If the sign of the `number` is negative, then the rounding is away from 0.
    
    
    __Example__ `floor(-3.14, 5)` returns `-5`

!!! abstract "int"
    Assigns the nearest smaller integer to a real `number`.
    
    ```
    int(number)
    ```
    
    __Example__ `int(-3.14)` returns `-4`

!!! abstract "lg"
    Logarithm function with 10 as base.
    
    ```
    lg(number)
    ```
    
    __Example__ `lg(100)` returns `2`

!!! abstract "log"
    Logarithm function with a definable `base`.
    
    ```
    log(number, base)
    ```
    
    __Example__ `log(81, 3)` returns `4`

    But if no `base` is given, this function works exactly like lg(), with 10 as `base`.
    
    
    __Example__ `log(1000)` returns `3`

!!! abstract "odd"
    Returns the nearest greater odd `number`.
    
    ```
    odd(number)
    ```
    
    __Example__ `odd(-2.14)` returns `-1`

!!! abstract "round"
    Rounds a `number` to the nearest integer. If no decimal place (`digits`) is specified, the `number` is rounded to an integer.
    
    ```
    round(number, digits)
    ```
    
    __Example__ `round(3.14)` returns `3`

    If a positive decimal place (`digits`) is given, the result will have `digits` decimals.
    
    
    __Example__ `round(3.14, 1)` returns `3.1`

    If a negative decimal place (`digits`) is given, the result is rounded to the left of the decimal point.
    
    
    __Example__ `round(3.14, -3)` returns `0`

!!! abstract "rounddown"
    Rounds a `number` towards zero. If no decimal place (`digits`) is given, the `number` is rounded to an integer.
    
    ```
    rounddown(number, digits)
    ```
    
    __Example__ `rounddown(3.12, 1)` returns `3.1`

!!! abstract "roundup"
    Rounds a `number` away from zero. If no decimal place (`digits`) is given, the `number` is rounded to an integer.
    
    ```
    roundup(number, digits)
    ```
    
    __Example__ `roundup(-3.15)` returns `-4`

!!! abstract "sign"
    Checks whether a `number` is greater, equal or less than 0. Returns the values 1, 0 and -1 respectively. In other words: it returns the sign of a `number`, for '+', 'zero' and '-' with 1, 0, and -1 respectively.
    
    ```
    sign(number)
    ```
    
    __Example__ `sign(-2)` returns `-1`

!!! abstract "sqrt"
    Returns the square root of a `number`.
    
    ```
    sqrt(number)
    ```
    
    __Example__ `sqrt(81)` returns `9`

## Text functions

!!! abstract "concatenate"
    Combines several strings (`string1`, `string 2`, ...) into one single string.
    
    ```
    concatenate(string1, string2, ...)
    ```
    
    __Example__ `concatenate(`Supplier`, " has the product ", `Product`)` returns for example `Microsoft has the product GitHub` if `Supplier` column contains "Microsoft" and `Product` column contains "GitHub"

!!! abstract "exact (A≠a case sensitive)"
    Checks whether two strings (`string1`, `string2`) are exactly identical. Returns the values `true` or `false` respectively.
    
    ```
    exact(string1, string2)
    ```
    
    __Example__ `exact('SeaTable', 'Seatable')` returns `false`

!!! abstract "find (A≠a case sensitive)"
    Returns the start position of a string (`findString`) within another string (`sourceString`). The numbering starts at 1. If not found, 0 is returned. If the start position (`startPosition`) is given as decimal, it is rounded down. If the cell in the column for the keyword (`findString`) is empty, 1 is returned. If the cell in the column for the target string (`sourceString`) is empty, an empty value ('') is returned.
    
    ```
    find(findString, sourceString, startPosition)
    ```
    
    __Example__ `find('Sea', 'seaTable', 1)` returns `0`

    The search will start from the given `startPosition`. This startPosition` has no influence on the result: it always returns the absolute start position. If the '`startPosition`' of the string to be searched for (`findString`) is given after the actual start position of the string (`sourceString`), 0 is returned, since nothing was found from this position.
    
    
    __Example__ `find('table', 'big table', 4)` returns `5`

!!! abstract "left"
    Returns the specified number (`count`) of characters at the beginning of a `string`.
    
    ```
    left(string, count)
    ```
    
    __Example__ `left('SeaTable', 3)` returns `Sea`

!!! abstract "len"
    Returns the number of characters in a `string`.
    
    ```
    len(string)
    ```
    
    __Example__ `len('SeaTable')` returns `8`

!!! abstract "lower"
    Converts a character `string` to lower case letters.
    
    ```
    lower(string)
    ```
    
    __Example__ `lower('German)` returns `german`

!!! abstract "mid"
    Returns the specified number (`count`) of characters from the specified start position (`startPosition`) of a `string`.
    
    ```
    mid(string, startPosition, count)
    ```
    
    __Example__ `mid('SeaTable is the best', 1, 8)` returns `SeaTable`

    Start position (`startPosition`) and `count` must not be empty, negative or zero. However, if start position (`startPosition`) and number (`count`) are given as decimal, they are rounded down. Too much `count` is ignored.
    
    
    __Example__ `mid('SeaTable is the best.', 10.9, 27.3)` returns `is the best.`

!!! abstract "replace"
    Replaces a part (`count`) of a character string (`sourceString`) from a certain start position (`startPosition`) with another character string (`newString`). The number (`count`) of characters is only taken into account for the old string (`sourceString`), but not for the new string (`newString`).
    
    ```
    replace(sourceString, startPosition, count, newString)
    ```
    
    __Example__ `replace('SeaTable is the best.', 1, 8, 'Seafile')` returns `Seafile is the best.`

    If number (`count`) is given as zero, the new string (`newString`) is simply added to the old string (`sourceString`) from the start position (`startPosition`).
    
    
    __Example__ `replace('SeaTable is the best.', 1, 0, 'Seafile')` returns `SeafileSeaTable is the best.`

!!! abstract "rept"
    Repeats a `string` as often (`number`) as specified.
    
    ```
    rept(string, number)
    ```
    
    __Example__ `rept('Sea ', 3)` returns `SeaSeaSea`

!!! abstract "right"
    Returns the specified number (`count`) of characters at the end of a `string`.
    
    ```
    right(string, count)
    ```
    
    __Example__ `right('SeaTable', 5)` returns `Table`

!!! abstract "search ((A=a NOT case sensitive))"
    Returns the start position of a string (`findString`) within another string (`sourceString`). The numbering starts at 1. If not found, 0 is returned. If the start position (`startPosition`) is given as decimal, it is rounded down. If the cell in the column for the keyword (`findString`) is empty, 1 is returned. If the cell in the column for the target string (`sourceString`) is empty, an empty value ('') is returned.
    
    ```
    search(findString, sourceString, startPosition)
    ```
    
    __Example__ `search('Sea', 'seaTable', 1)` returns `1`

    The search will start from the given `startPosition`. This `startPosition` has no influence on the result: it always returns the absolute start position. If the `startPosition` of the character string to be searched for (`findString`) is given after the actual start position of the character string (`sourceString`), 0 is returned, since nothing was found from this position.
    
    
    __Example__ `search('table', 'big table', 6)` returns `0`

!!! abstract "substitute (A≠a case sensitive)"
    Replaces existing text (`oldString`) with new text (`newString`) in a string (`sourceString`). If there is more than one text (`oldString`) in the string (`sourceString`), only the `index`-th text is replaced.
    
    ```
    substitute(sourceString, oldString, newString, index)
    ```
    
    __Example__ `substitute('SeaTableTable', 'Table', 'file', 1)` returns `SeafileTable`

    If the `index` is given as 0 or not, all found text (`oldString`) will be replaced by the new text (`newString`).
    
    
    __Example__ `substitute('SeaTableTable', 'Table', 'file')` returns `Seafilefile`

!!! abstract "T"
    Checks whether a `value` is text. If so, the text is returned. If no, the return `value` is empty.
    
    ```
    T(value)
    ```
    
    __Example__ `T('123')` returns `123`

!!! abstract "text"
    Converts a `number` into text and `format`s it in the specified `format`. The `format` can be percent, number, dollar, euro or yuan.
    
    ```
    text(number, format)
    ```
    
    __Example__ `text(150, 'euro')` returns `€150`

    When a `number` is converted directly to percent, its absolute value is retained. In other words, 50 is converted into 5000%. But if you want 50%, you have to divide the `number` by 100 before the conversion.
    
    
    __Example__ `text(50, 'percent')` returns `5000%`

!!! abstract "trim"
    Removes spaces at both the beginning and the end of a `string`.
    
    ```
    trim(string)
    ```
    
    __Example__ `trim(' SeaTable ')` returns `SeaTable`

!!! abstract "upper"
    Converts a `string` to uppercase letters.
    
    ```
    upper(string)
    ```
    
    __Example__ `upper('German)` returns `GERMAN`

!!! abstract "value"
    Converts a text (`string`) representing a number into a number.
    
    ```
    value(string)
    ```
    
    __Example__ `value('123')` returns `123`


## Date functions

When passing a parameter with time or date type, you can specify a constant in "2025-09-01 12:00:01" or "2025-09-01" format. When you query the result of a date function in SQL, the result will be converted to a string in RFC3339 format, e.g. "2025-09-03T00:00:00+02:00". Please note that if a date function returns a date, it cannot be used as parameter for text or maths functions.

!!! abstract "date"
    Returns a date in international format (ISO) from entered `year`, `month` and `day`. If the `year` is entered with two digits, it is automatically understood as a year in the 1900s. If the number of the `month` or `day` is too large (greater than 12 or 31 respectively), these months or days are automatically converted to the next year or month.
    
    ```
    date(year, month, day)
    ```
    
    __Example__ `date(2025, 1, 3)` returns `2025-01-03T00:00:00+02:00`

!!! abstract "dateAdd"
    Adds the specified number (`count`) of years ('years'), months ('months'), weeks ('weeks'), days ('days'), hours ('hours'), minutes ('minutes') or seconds ('seconds') to a datetime (`date`).
    
    ```
    dateAdd(date, count, unit)
    ```
    
    __Example__ `dateAdd('2024-02-03', 2, 'days')` returns `2024-02-05T00:00:00+02:00`

    Tip: if you want to add a complex duration (`count`) such as 1 day 12 hours, you can convert it to e.g. 24+12=36 hours ('hours') and enter it into the formula as a uniform duration (`count`). The duration is converted to the smallest `unit`: in this case, hours.
    
    
    __Example__ `dateAdd('2024-09-04 13:05:18', 36, 'hours') OR dateAdd(`form submission`, 36, 'hours')` returns `2024-09-06T01:05:18+02:00`

!!! abstract "dateDif"
    Calculates the seconds, days, months, or years between two date values. The optional `unit` argument can be one of the following: S (seconds), D (full days), M (full months), Y (full years), YD (full days, ignoring years), YM (full months, ignoring days and years), MD (full days, ignoring months and years). If the `startDate` is empty, a default value of "1900-01-01" will be set. If both date values are empty, it will return 0.
    
    ```
    dateDif(startDate, endDate, unit)
    ```
    
    __Example__ `dateDif('2023-01-01', '2025-01-01','Y')` returns `2`
    
    
    __Example__ `dateDif('2024-10-11', '2025-12-12', 'M')` returns `14`

!!! abstract "day"
    Returns the day of a `date` as a number. The returned number is between 1 and 31.
    
    ```
    day(date)
    ```
    
    __Example__ `day('2025-01-03')` returns `3`

!!! abstract "eomonth"
    Determines the date of the last day of `n`th month before or after (depending on the sign of `n`) the specified date (`startDate`). If `n` is 0, the last day of the month is simply determined.
    
    ```
    eomonth(startDate, n)
    ```
    
    __Example__ `eomonth('2025-01-01', 1)` returns `2025-02-28T00:00:00+02:00`

    
    
    __Example__ `eomonth('2025-01-01', -1)` returns `2024-12-31T00:00:00+02:00`

!!! abstract "hour"
    Returns the hour of a `date` as a number. The number returned is between 0 and 23.
    
    ```
    hour(date)
    ```
    
    __Example__ `hour('2025-02-14 13:14:52')` returns `13`

    If no hour is contained in the time specification (`date`), 0 is returned.
    
    
    __Example__ `hour('2025-02-14')` returns `0`

!!! abstract "hours"
    Returns the number of hours between two date values (`startDate` and `endDate`). The minutes in the date values are not taken into account.
    
    ```
    hours(startDate, endDate)
    ```
    
    __Example__ `hours('2025-02-14 13:14', '2025-02-14 15:14')` returns `2`

    If no hours are included in the time specification (`startDate` or `endDate`), 0 o'clock on this day is automatically assumed.
    
    
    __Example__ `hours('2020-02-14', '2020-02-14 15:14')` returns `15`

!!! abstract "minute"
    Returns the minutes of a time specification (`date`) as a number. The number returned is between 0 and 59.
    
    ```
    minute(date)
    ```
    
    __Example__ `minute('2025-02-14 13:14:52')` returns `14`

    If no minutes are included in the time (`date`), 0 is returned.
    
    
    __Example__ `minute('2025-02-14)` returns `0`

!!! abstract "month"
    Returns the month of a `date` as a number. The returned number is between 1 (January) and 12 (December).
    
    ```
    month(date)
    ```
    
    __Example__ `month('2025-02-14 13:14:52')` returns `2`

!!! abstract "months"
    Returns the number of months between two date values (`startDate` and `endDate`). The days and time in the date values are not taken into account.
    
    ```
    months(startDate, endDate)
    ```
    
    __Example__ `months('2025-02-01 13:14', '2025-03-31 15:54')` returns `1`


!!! abstract "networkdays"
    Returns the number of full working days between two dates (`startDate` and `endDate`). You can also define holidays other than Saturday and Sunday (`holiday1`, `holiday2`, etc.), which are also deducted. If you do not want to include public holidays, you can simply omit these parameters.
    
    ```
    networkdays(startDate, endDate, holiday1, holiday2, ...)
    ```
    
    __Example__ `networkdays('2025-01-01', '2025-01-07','2025-01-01')` returns `4`

    Please note that the specified last day (`endDate`) is also included in the formula. Thus, for the following example, three working days are counted: the 7th, 8th and 9th of September, 2025.
    
    
    __Example__ `networkdays('2025-09-08', '2025-09-10')` returns `3`

!!! abstract "now"
    Returns the current date and time.
    
    ```
    now()
    ```
    
    __Example__ `now()` returns `2025-09-07T12:59+02:00`

!!! abstract "second"
    Returns the seconds of a time (`date`) as a number. The number returned is between 0 and 59.
    
    ```
    second(date)
    ```
    
    __Example__ `second('2025-02-14 13:14:52')` returns `52`

!!! abstract "today"
    Returns the current date.
    
    ```
    today()
    ```
    
    __Example__ `today()` returns `2020-09-07T00:00:00+02:00`

    This function is handy for calculating time between a certain datetime and now. On each reload of the Base or recalculation, the calculation is updated.
    
    __Example__ `networkdays('2025-10-01', today())` returns `4`

!!! abstract "weekday"
    Returns the weekday of a `date` as a number. The returned number between 1 and 7, where you can define the first day of the week (`weekStart`). `weekStart` is Sunday by default, it can also be set to Monday ('Monday' or 'monday', not case sensitive).
    
    ```
    weekday(date, weekStart)
    ```
    
    __Example__ `weekday('2025-01-01', 'Monday')` returns `3`

    If no `weekStart` is given or if a `weekStart` other than 'Monday' or 'Sunday' is given, the default value ('Sunday') is used. So if it should be 'Monday', enter 'Monday'; if it should be 'Sunday', you can omit this parameter.
    
    
    __Example__ `weekday('2025-01-01', 'Thursday') OR weekday('2025-01-01')` returns `4`

!!! abstract "weeknum"
    Returns the absolute week number of a `date` as a number. The returned number is between 1 and 53, where you can define the first day of the week (`return_type`). Enter the number 1 or 2, or 11 to 17, and 21 as `return_type` to define the start of a week: 1/Sunday, 2/Monday, 11/Monday, 12/Tuesday, 13/Wednesday, 14/Thursday, 15/Friday, 16/Saturday, 17/Sunday. If you want the week number to be returned according to ISO standard, specify the number of 21 as `return_type`, or use the function `isoweeknum`.
    
    ```
    weeknum(date, return_type)
    ```
    
    __Example__ `weeknum('2025-01-12', 11)` returns `2`

    If no '`return_type`' is given, it is always assumed to be 'Sunday'.
    
    
    __Example__ `weeknum('2025-01-12')` returns `3`

!!! abstract "year"
    Returns the year of a `date` as a number.
    
    ```
    year(date)
    ```
    
    __Example__ `year('2025-01-01')` returns `2025`

!!! abstract "startofweek"
    Returns the first day of the week in which the `date` is located. `weekStart` is Sunday by default, it can also be set to Monday ('Monday' or 'monday', not case sensitive).
    
    ```
    startofweek(date, weekStart)
    ```
    
    __Example__ `startofweek('2025-04-28')` returns `2021-4-27T00:00:00+02:00`

!!! abstract "quarter"
    Returns the quarter of the `date`, the return value is 1, 2, 3, 4.
    
    ```
    quarter(date)
    ```
    
    __Example__ `quarter('2025-01-01')` returns `1`

!!! abstract "isodate"
    Returns the ISO string representation of the `date`.
    
    ```
    isodate(date)
    ```
    
    __Example__ `isodate('2025-01-01 11:00:00')` returns `2025-01-01`

!!! abstract "isomonth"
    Returns the ISO string representation (of the )year and month) of the month of a specified `date`.
    
    ```
    isomonth(date)
    ```
    
    __Example__ `isomonth('2025-01-01 11:00:00')` returns `2025-01`


## Geo functions

!!! abstract "country"
    Returns the country or region of a geolocation-type column. (Since version 5.1.0)
    
    ```
    country(geolocation)
    ```
    
    __Example__ ```country(`Country of residence`)``` returns `Germany`

## Logical functions

!!! abstract "and"
    Checks if all arguments (`logical1`, `logical2`, ...) are true (valid, not empty and not equal to zero). If yes, `true` is returned, otherwise `false`.
    
    ```
    and(logical1, logical2, ...)
    ```
    
    __Example__ `and(1, '', 2)` returns `false`

!!! abstract "if"
    Checks if an argument (`logical`) is true and returns `trueValue` or `falseValue` accordingly.
    
    ```
    if(logical, trueValue, falseValue)
    ```
    
    __Example__ `if(1>2, 3, 4)` returns `4`

    For the condition (`logical`) only a comparison is allowed. If `falseValue` is omitted`: it will return the first value (`trueValue`) if the condition (`logical`) is true; and it will return an empty value ('') if the condition (`logical`) is false.
    
    
    __Example__ `if(`Budget`>`Price`, 'Yes')` returns `Yes` or ''

!!! abstract "ifs"
    Checks if one or more conditions (`logical1`, `logical2`, ...) are true and returns a value (`value1`, `value2`, ...) that matches the **first** true condition.
    
    ```
    ifs(logical1, value1, logical2, value2, ...)
    ```
    
    __Example__ `ifs( 1>2, 3, 5>4, 9)` returns `9`

!!! abstract "not"
    Inverts the logical value (`boolean`). In other words: converts true to false and false to true.
    
    ```
    not(boolean)
    ```
    
    __Example__ `not(and(1, '', 2))` returns `true`

!!! abstract "or"
    Checks if at least 1 of the arguments (`logical1`, `logical2`, ...) is true (valid, not empty and not equal to zero), and returns `true` in this case. If all arguments are false, then returns `false`.
    
    ```
    or(logical1, logical2, ...)
    ```
    
    __Example__ `or(1,'',2)` returns `true`

!!! abstract "switch"
    Evaluates an expression (`logical`) against a list of values (matcher) and returns the result (value) corresponding to the **first** matching value. If there is no match, an optional `default` value is returned. At least 3 parameters (`logical`, matcher, value) must be specified.
    
    ```
    switch(logical, matcher1, value1, matcher2, value2, ..., default)
    ```
    
    __Example__ `switch(`grades`, 1, 'very good', 2, 'good', 3, 'satisfactory', 4, 'passed', 'failed')` returns `very good`

    If there are several identical values in the value list (matcher), only the first hit is taken into account.
    
    
    __Example__ `switch(int(68/10), 6, 'OK', 6, 'KO')` returns `OK`

!!! abstract "xor"
    Returns the logical inequality of all arguments. In other words, returns `true` fi the number of true arguments is odd.
    
    ```
    xor(logical1, logical2, ...)
    ```
    
    __Example__ `xor(1, 0, 2<1)` returns `true`

## Statistical functions

!!! abstract "average"
    Returns the average of the numbers (`number1`, `number2`, ...).
    
    ```
    average(number1, number2, ...)
    ```
    
    __Example__ `average(1, 2, 3, 4, 5)` returns `3`

!!! abstract "counta"
    Counts the number of non-empty cells (`textORnumber1`, `textORnumber2`, ...). These cells can be text or numbers. In this example, 1 and 2 are numbers, '3' is text, and '' is an empty value.
    
    ```
    counta(textORnumber1, textORnumber2, ...)
    ```
    
    __Example__ `counta(1, '', 2, '3')` returns `3`

!!! abstract "countall"
    Counts the number of elements (`textORnumber1`, `textORnumber2`, ...) including numbers (1, 2), text ('3') and empty cells ('').
    
    ```
    countall(textORnumber1, textORnumber2, ...)
    ```
    
    __Example__ `countall(1, '', 2, '3')` returns `4`

!!! abstract "countblank"
    Counts the number of empty cells.
    
    ```
    countblank(textORnumber1, textORnumber2, ...)
    ```
    
    __Example__ `countblank(1, '', 2, '3')` returns `1`

!!! abstract "countItems"
    Counts the number of items in a `column`. The supported `column` types are multiple select, collaborator, file, image (available since version 2.7.0).
    
    ```
    countItems(column)
    ```
    
    __Example__ `countItems(column_name)` returns `2`
