# Date utility functions

We provide a set of functions for the datetime (date and time) operations based on the datetime python library. These functions have the same behavior as the functions provided by the formula column of SeaTable.

!!! warning "Function import required"

    To use these functions, the dateutils module must be imported.

    ```
    from seatable_api.date_utils import dateutils
    ```

## Introduction

### Date and time formatting
    
The ISO format is used in date methods, both for input and output, which means:

- `YYYY-MM-DD` (or `%Y-%m-%d` referring to the [python datetime library format codes](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes)) for dates

- `YYYY-MM-DD HH:mm:ss` (or `%Y-%m-%d %H:%M:%S`) for datetimes. Please note that the hour is (24-hour based)

- Datetimes format with timezone info requires a specific format: `YYYY-MM-DDTHH:mm:ss±hh:mm` with the letter `T` separating the date from the time and `±hh:mm` representing the offset to UTC (here `+08:00` for UTC+8)

Of course, methods outputs with this format can be reused as input for other `dateutils` methods requiring the same format. You'll find below an overview example. Every methods are detailed in the following of this section.
    
!!! info "Timezone"
    
    If the input time string has a timezone info, it will be automatically converted to local time.

### Overview example

In this example as in the following of this section, the comment at the end of each line shows the expected result (what you should update if you `print` the result of the current line)

``` python
from seatable_api.date_utils import dateutils

dt_now = dateutils.now()  # 2025-09-30 15:47:00
# 1. date 10 days after dt_now
dt_10_days = dateutils.dateadd(dt_now, 10) # 2025-10-10 15:47:00
# 2. month 10 days after dt_now
dt_month_10_days = dateutils.month(dt_10_days) # 10
# 3. difference between 2 days
dt_10_days_before = dateutils.dateadd(dt_now, -10)
date_df = dateutils.datediff(dt_10_days_before, dt_10_days, unit="D") # 20
# 4. handle the time string with time-zone info with local timezone of "Asia/Shanghai" (UTC+8)
time_str = "2025-07-17T21:57:41+08:00"
time_day = dateutils.day(time_str) # 17
time_month = dateutils.month(time_str) # 7
time_year = dateutils.year(time_str) # 2025
time_hour = dateutils.hour(time_str) # 15 (! if local timezone is UTC+2 !)
time_minute = dateutils.minute(time_str) # 57
time_date = dateutils.date(time_year, time_month, time_day) # 2025-07-17
```

## Dealing with date and time 

### date

!!! abstract "date"

    Return the ISO formatted date string.

    ``` python
    dateutils.date(year, month, day)
    ```

    __Example__
    
    ``` python
    from seatable_api.date_utils import dateutils

    custom_date = dateutils.date(2025, 9, 16)
    print(custom_date) # 2025-09-16
    ```

### dateadd

!!! abstract "dateadd"

    Add a `number` of a specified `interval` to a datetime `datetime_str`. `interval` can represent the following units: `years`, `months`, `weeks`, `days`, `hours`, `minutes` and `seconds` (default is `days`). Negative values ​​can be used to subtract from `datetime_str`.

    ``` python
    dateutils.dateadd(datetime_str, number, interval)
    ```

    __Example__
    
    ``` python
    from seatable_api.date_utils import dateutils

    date_str = "2025-9-15"
    datetime_str = "2025-9-15 15:23:21"

    dateutils.dateadd(date_str, -2, 'years') # 2023-09-15
    dateutils.dateadd(date_str, 3, 'months') # 2025-12-15
    dateutils.dateadd(datetime_str, 44, 'minutes') # 2025-09-15 16:07:21
    dateutils.dateadd(datetime_str, 1000, 'days') # 2028-06-11 15:23:21
    dateutils.dateadd(datetime_str, 3, 'weeks') # 2025-10-06 15:23:21
    dateutils.dateadd(datetime_str, -3, 'hours') # 2025-09-15 12:23:21
    dateutils.dateadd(datetime_str, 3, 'seconds') # 2025-09-15 15:23:24
    ```

### datediff

!!! abstract "datediff"

    Compute the time between two datetimes in one of the following units:`S`, `Y`, `D`, `H`, `M`, `YM`, `MD`, `YD`. The result can be negative if `end_date` is before `start_date`.

    For date units (`Y`,`M` and `D`), unit might include two characters:

    - `YM`: The difference between the months in `start_date` and `end_date`. The days and years of the dates are ignored.
    - `MD`: The difference between the days in `start_date` and `end_date`. The months and years of the dates are ignored.
    - `YD`: The difference between the days of `start_date` and `end_date`. The years of the dates are ignored.

    ``` python
    dateutils.datediff(start=start_date, end=end_date, unit=datetime_unit)
    dateutils.datediff(start_date, end_date, datetime_unit) # (1)!
    ```

    1. Depending on your preferences, you can either specify the name of each parameter (longer but easier to reread) or not

    __Example__
    
    ``` python
    from seatable_api.date_utils import dateutils as dt # (1)!

    start_date = "2025-5-16"
    end_date = "2026-5-15"

    dt.datediff(start=start_date, end=end_date, unit='S') # 31449600 (seconds)
    dt.datediff(start=start_date, end=end_date, unit='Y') # 0 (years)
    dt.datediff(start=start_date, end=end_date, unit='D') # 364 (days)
    dt.datediff(start=start_date, end=end_date, unit='H') # 8736 (hours)
    dt.datediff(start=start_date, end=end_date, unit='M') # 12 (months) (from 2025-5 to 2026-5)
    dt.datediff(start=start_date, end=end_date, unit='YM') # 0 (months) (from May to May)
    dt.datediff(start=start_date, end=end_date, unit='MD') # -1 (days) (from 16 of 15)
    dt.datediff("2025-1-28","2026-2-1", unit='YD') # 4 (days) (from January 28 to February 1)
    ```

    1. To make calls shorter or more explicit, feel free to use an alternative name using `as` keyword. Here, we use `dt` instead of the default `dateutils`

### day

!!! abstract "day"

    Return the day of a given `date`.

    ``` python
    dateutils.day(date)
    ```

    __Example__
    
    ``` python
    from seatable_api.date_utils import dateutils
 
    dateutils.day('2025-6-15 14:23:21') # 15
    ```

### days

!!! abstract "days"

    Return the days difference between two given date. The result can be negative if `end` is before `start`.

    ``` python
    dateutils.days(start, end)
    ```

    __Example__
    
    ``` python
    from seatable_api.date_utils import dateutils

    dateutils.days('2024-6-1', '2025-5-15') # 348
    ```

### eomonth

!!! abstract "eomonth"

    Return the ISO formatted last day of the `n`th month before or after given date (depending on the sign of `n`).

    ``` python
    dateutils.eomonth(date, months=n)
    ```

    __Example__
    
    ``` python
    from seatable_api.date_utils import dateutils

    date = "2025-7-4"
    dateutils.eomonth(date, months=0) # 2025-07-31 (months=0 => current month) 
    dateutils.eomonth(date, months=2) # 2025-09-30 (2 months after July => September)
    dateutils.eomonth(date, months=-5) # 2025-02-28 (5 months before July => February)
    ```

### hour

!!! abstract "hour"

    Return the hour of a given `datetime`.

    ``` python
    dateutils.hour(datetime)
    ```

    __Example__
    
    ``` python
    from seatable_api.date_utils import dateutils
  
    dateutils.hour("2025-1-1 12:13:14") # 12
    ```

### hours

!!! abstract "hours"

    Return the hours difference between two given datetime. The result can be negative if `end` is before `start`.

    ``` python
    dateutils.hours(start, end)
    ```

    __Example__
    
    ``` python
    from seatable_api.date_utils import dateutils

    dateutils.hours("2019-6-3 20:01:12", "2020-5-3 13:13:13") # 8009
    ```

### minute

!!! abstract "minute"

    Return the minutes of a given `datetime`.

    ``` python
    dateutils.minute(datetime)
    ```

    __Example__
    
    ``` python
    from seatable_api.date_utils import dateutils

    dateutils.minute("2025-5-3 13:14:15") # 13
    ```

### month

!!! abstract "month"

    Return the month of a given `date`. The month number starts at 1, like when writing a date.

    ``` python
    dateutils.month(date)
    ```

    __Example__
    
    ``` python
    from seatable_api.date_utils import dateutils

    dateutils.month("2025-5-4") # 5
    ```

### isomonth

!!! abstract "isomonth"

    Return the ISO formatted (`YYYY-MM`) month of a given `date`.

    ``` python
    dateutils.isomonth(date)
    ```

    __Example__
    
    ``` python
    from seatable_api.date_utils import dateutils
    
    dateutils.isomonth("2025-1-2") # 2025-01
    ```

### months

!!! abstract "months"

    Return the months difference between two given date. The result can be negative if `end` is before `start`. 

    ``` python
    dateutils.months(start, end)
    ```

    __Example__
    
    ``` python
    from seatable_api.date_utils import dateutils

    dateutils.months("2024-5-1","2025-5-4") # 12
    ```
    
### now

!!! abstract "now"

    Return the ISO formatted current date and time,accurate to seconds.

    ``` python
    dateutils.now()
    ```

    __Example__
    
    ``` python
    from seatable_api.date_utils import dateutils

    now = dateutils.now()
    print(now) # 2025-09-30 12:56:41
    ```

### second

!!! abstract "second"

    Return the seconds of given datetime.

    ``` python
    dateutils.second(date)
    ```

    __Example__
    
    ``` python
    from seatable_api.date_utils import dateutils

    dateutils.second("2025-5-3 13:13:33") # 33
    ```

### today

!!! abstract "today"

    Return the ISO formatted current date time in string

    ``` python
    dateutils.today()
    ```

    __Example__
    
    ``` python
    from seatable_api.date_utils import dateutils

    today = dateutils.today()
    print(today) # 2025-09-30
    ```

### weekday

!!! abstract "weekday"

    Return the weekday of a `date`. The result (from 0 to 6) consider a week starting on Monday (returns 0) and ending on Sunday (returns 6).

    ``` python
    dateutils.weekday(date)
    ```

    __Example__
    
    ``` python
    from seatable_api.date_utils import dateutils

    dateutils.weekday("2025-6-2") # 0 (June 2,2025 was a Monday)
    ```

### isoweekday

!!! abstract "isoweekday"

    Return the weekday of a `date` from 1 to 7 and considering a week starting on Monday (based on ISO standard).

    ``` python
    dateutils.isoweekday(date)
    ```

    __Example__
    
    ``` python
    from seatable_api.date_utils import dateutils

    dateutils.isoweekday("2025-6-2") # 1
    ```

### weeknum

!!! abstract "weeknum"

    Return the week number of a given `date`, considering the week including January 1st as the first week.

    ``` python
    dateutils.weeknum(date)
    ```

    __Example__
    
    ``` python
    from seatable_api.date_utils import dateutils

    dateutils.weeknum('2027-1-2') # 1
    ```

### isoweeknum

!!! abstract "isoweeknum"

    Return the week number of a given `date` based on ISO standard.

    ``` python
    dateutils.isoweeknum(date)
    ```

    __Example__
    
    ``` python
    from seatable_api.date_utils import dateutils
    
    dateutils.isoweeknum('2027-1-2') # 53
    ```

### year

!!! abstract "year"

    Return the year of a given `date`.

    ``` python
    dateutils.year(date)
    ```

    __Example__
    
    ``` python
    from seatable_api.date_utils import dateutils

    dateutils.year("2030-1-1") # 2030
    ```

## Dealing with quarters

A specific DateQuarter object exists to deal with quarters. The operations/properties/methods available this object are presented below.

### quarter_from_yq

!!! abstract "quarter_from_yq"

    Return a DateQuarter object, from a given `year` and `quarter` (1 to 4 for current year). if `quarter` is n less than 1 (or n greater than 4), the returned DateQuarter object will correspond to the year and quarter shifted by n quarters before the first quarter (or n quarters after the fourth quarter) of the `year`.

    ``` python
    dateutils.quarter_from_yq(year, quarter)
    ```

    __Example__
    
    ``` python
    from seatable_api.date_utils import dateutils
    
    dateutils.quarter_from_yq(2025, 3) # DateQuarter obj:<DateQuarter-2025,3Q>
    dateutils.quarter_from_yq(2025, 0) # DateQuarter obj:<DateQuarter-2024,4Q>
    dateutils.quarter_from_yq(2025, 6) # DateQuarter obj:<DateQuarter-2026,2Q>
    ```

### quarter_from_ym

!!! abstract "quarter_from_ym"

    Return a DateQuarter object, for specified `year` and `month`.

    ``` python
    dateutils.quarter_from_ym(year, month)
    ```

    __Example__
    
    ``` python
    from seatable_api.date_utils import dateutils
    
    dateutils.quarter_from_ym(2025, 3) # DateQuarter obj:<DateQuarter-2025,1Q>
    ```

### to_quarter

!!! abstract "to_quarter"

    Return a DateQuarter object from an ISO formatted date or datetime string `datetime_str`.

    ``` python
    dateutils.to_quarter(datetime_str)
    ```

    __Example__
    
    ``` python
    from seatable_api.date_utils import dateutils
    
    dateutils.to_quarter("2025-07-17") # DateQuarter obj: <DateQuarter-2025,3Q>
    ```

### quarters_within

!!! abstract "quarters_within"

    Return a generator which will generate the DateQuater objects between a `start` date and an `end` date. The last (not necessarily full) quarter isn't included by default. You can get it in the generator if you set param `include_last` to `True` (`False` by default).

    ``` python
    dateutils.quarters_within(start, end, include_last=False)
    ```

    __Example__
    
    ``` python
    from seatable_api.date_utils import dateutils
    
    qs1 = dateutils.quarters_within("2024-03-28", "2025-07-17")
    print(list(qs1)) # [<DateQuarter-2024,1Q>, <DateQuarter-2024,2Q>,...., <DateQuarter-2025,2Q>]
    
    qs2 = dateutils.quarters_within("2024-03-28", "2025-07-17", include_last=True)
    print(list(qs2)) # [<DateQuarter-2024,1Q>, <DateQuarter-2024,2Q>,...., <DateQuarter-2025,2Q>, <DateQuarter-2025,3Q>]
    ```

### DateQuarter properties and methods

Some operations/properties/methods are available for DateQuarter objects.
    
!!! abstract "DateQuarter properties and methods"

    - `year`: The year of the considered DateQuarter
    - `quarter`: The quarter of the considered DateQuarter (1 to 4)
    - `start_date`: The ISO formatted first day of the considered DateQuarter
    - `end_date`: The ISO formatted last day of the considered DateQuarter
    - `days()`: A generator, which will generate every dates (`datetime.date` objects) in the considered DateQuarter

    __Example__

    ```python
    from seatable_api.date_utils import dateutils

    q = dateutils.quarter_from_yq(2025, 3)

    q.year # 2025
    q.quarter # 3

    q.start_date # 2025-07-01
    q.end_date # 2025-09-30

    q.days() 
    list(q.days()) # [datetime.date(2025, 7, 1), datetime.date(2025, 7, 2),....., datetime.date(2025, 9, 30)]
    ```

### DateQuarter operations

!!! abstract "DateQuarter operations"

    Classical operators are available for DateQuarter objects:

    - **Arithmetic operators**: `+` (adds a number of quarters to a DateQuarter object), `-` (returns the number of quarters between two quarters, or the quarter shifted by the number of quarters if used with a number)
    - **Comparison operators**: `<`, `<=`, `==`, `>=`, `>`, `!=`
    - **Membership operators**: `in`, `not in`


     __Example__

    ``` python
    from seatable_api.date_utils import dateutils

    q = dateutils.quarter_from_yq(2026, 3)

    q + 10 # <DateQuarter-2029,1Q>
    q1 = dateutils.quarter_from_yq(2025, 1) # <DateQuarter-2025,1Q>
    q - q1 # 6
    q - 7  # <DateQuarter-2024,4Q>
    q < q1 # False
    "2026-28" in q # False
    "2026-8-28" in q # True
    ```
