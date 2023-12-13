# Date Utility Functions

We provide a set of functions for the date operations based on the datetime module of python. These functions have the same behavior as the functions provided by the formula column of SeaTable.

!!! warning "function import required"

    To use these functions, the dateutils module must be imported.

    ```
    from seatable_api.date_utils import dateutils
    ```

!!! tip "Timezone"

    If the input time string has a timezone info, it will be automatically converted to local time.

## date

!!! success "date"

    Return the ISO formatted date string.

    ``` python
    dateutils.date(year, month, day)
    ```

    __Example__

    ``` python
    custom_date = dateutils.date(2020, 5, 16)
    print(custom_date) # 2020-05-16
    ```

## now

!!! success "now"

    Return the ISO formatted date time of current and accurated to seconds.

    ``` python
    dateutils.now()
    ```

    __Example__

    ``` python
    now = dateutils.now()
    print(now) # 2022-02-07 09:44:00
    ```

## today

!!! success "today"

    Return the ISO formatted current date time in string

    ``` python
    dateutils.today()
    ```

    __Example__

    ``` python
    today = dateutils.today()
    print(today) # 2022-02-07
    ```

## dateadd

!!! success "dateadd"

    Addition operation for a datetime by different units such as years, months, weeks, days, hours, minutes and seconds, default by days.

    ``` python
    dateutils.dateadd(time_str, number, inverval)
    ```

    __Example__

    ``` python
    time_str = "2020-6-15"
    time_str_s = "2020-6-15 15:23:21"

    dateutils.dateadd(time_str, -2, 'years') # 2018-06-15
    dateutils.dateadd(time_str, 3, 'months') # 2020-09-15
    dateutils.dateadd(time_str_s, 44, 'minutes') # 2020-06-15 16:07:21
    dateutils.dateadd(time_str_s, 1000, 'days') # 2023-03-12 15:23:21
    dateutils.dateadd(time_str_s, 3, 'weeks') # 2020-07-06 15:23:21
    dateutils.dateadd(time_str_s, -3, 'hours') # 2020-06-15 12:23:21
    dateutils.dateadd(time_str_s, 3, 'seconds') # 2020-06-15 15:23:24
    ```

## datediff

!!! success "datediff"

    Caculation of the different between 2 date times by different units such as S, Y, D, H, M, YM, MD, YD.

    - __YM__: The difference between the months in start_date and end_date. The days and years of the dates are ignored.
    - __MD__: The difference between the days in start_date and end_date. The months and years of the dates are ignored.
    - __YD__: The difference between the days of start_date and end_date. The years of the dates are ignored.

    ``` python
    dateutils.datediff(start, end, unit)
    ```

    __Example__

    ``` python
    time_start = "2019-6-1"
    time_end = "2020-5-15"
    dateutils.datediff(start=time_start, end=time_end, unit='S') # seconds 30153600
    dateutils.datediff(start=time_start, end=time_end, unit='Y') # years 0
    dateutils.datediff(start=time_start, end=time_end, unit='D') # days 349
    dateutils.datediff(start=time_start, end=time_end, unit='H') # hours 8376
    dateutils.datediff(start=time_start, end=time_end, unit='M') # months 11
    dateutils.datediff(start=time_start, end=time_end, unit='YM') #  11
    dateutils.datediff(start=time_start, end=time_end, unit='MD') #  14
    dateutils.datediff("2019-1-28","2020-2-1", unit='YD') # 3
    ```

## eomonth

!!! success "eomonth"

    Return the last day of n months befor or after given date. Parameter months refers to n.

    ``` python
    dateutils.eomonth(date, months)
    ```

    __Example__

    ``` python
    date = "2022-7-4"
    dateutils.eomonth(date, months=0) # 2022-07-31
    dateutils.eomonth(date, months=2) # 2022-09-30
    dateutils.eomonth(date, months=-5) # 2022-02-28
    ```

## year

!!! success "year"

    Return the year of given date.

    ``` python
    dateutils.year(date)
    ```

    __Example__

    ``` python
    dateutils.year("2019-1-1") # 2019
    ```

## month

!!! success "month"

    Return the month of given date.

    ``` python
    dateutils.month(date)
    ```

    __Example__

    ``` python
    dateutils.month("2019-5-4") # 5
    ```

## months

!!! success "months"

    Return the months difference of two given date.

    ``` python
    dateutils.months(start, end)
    ```

    __Example__

    ``` python
    dateutils.months("2019-5-1","2020-5-4") # 12
    ```

## day

!!! success "day"

    Return the day of given date.

    ``` python
    dateutils.day(date)
    ```

    __Example__

    ``` python
    dateutils.day('2020-6-15 14:23:21') # 15
    ```

## days

!!! success "days"

    Return the days difference of two given date.

    ``` python
    dateutils.days(start, end)
    ```

    __Example__

    ``` python
    dateutils.days('2019-6-1', '2020-5-15') # 349
    ```

## hour

!!! success "hour"

    Return the hour of given datetime.

    ``` python
    dateutils.hour(date)
    ```

    __Example__

    ``` python
    dateutils.hour("2020-1-1 12:20:30") # 12
    ```

## hours

!!! success "hours"

    Return the hours difference of two given datetime.

    ``` python
    dateutils.hours(start, end)
    ```

    __Example__

    ``` python
    dateutils.hours("2019-6-3 20:1:12", "2020-5-3 13:13:13") # 8033
    ```

## minute

!!! success "minute"

    Return the minutes of given datetime.

    ``` python
    dateutils.minute(date)
    ```

    __Example__

    ``` python
    dateutils.minute("2020-5-3 13:13:13") # 13
    ```

## second

!!! success "second"

    Return the seconds of given datetime.

    ``` python
    ateutils.second(date)
    ```

    __Example__

    ``` python
    ateutils.second("2020-5-3 13:13:33") # 33
    ```

## weekday

!!! success "weekday"

    Return the weekday by recording 0 to 6 from Monday to Sunday.

    ``` python
    dateutils.weekday(date)
    ```

    __Example__

    ``` python
    dateutils.weekday("2019-6-3") # 0
    ```

## isoweekday

!!! success "isoweekday"

    Return the weekday by recording 1 to 7 from Monday to Sunday based on ISO standard.

    ``` python
    dateutils.isoweekday(date)
    ```

    __Example__

    ``` python
    dateutils.isoweekday("2019-6-3") # 1
    ```

## weeknum

!!! success "weeknum"

    Return the week number of given date by counting the 1st of Jan. as the first week.

    ``` python
    dateutils.weeknum(date)
    ```

    __Example__

    ``` python
    dateutils.weeknum('2012-1-2') # 2
    ```

## isoweeknum

!!! success "isoweeknum"

    Return the week number of given date based on ISO standard.

    ``` python
    dateutils.isoweeknum(date)
    ```

    __Example__

    ``` python
    dateutils.isoweeknum('2012-1-2') # 1
    ```

## isomonth

!!! success "isomonth"

    Return the ISO formatted month.

    ``` python
    dateutils.isomonth(date)
    ```

    __Example__

    ``` python
    dateutils.isomonth("2012-1-2") # 2012-01
    ```

## quarter_from_yq

!!! success "quarter_from_yq"

    Return a DateQuarter object, and params inlclude year and quarter..

    ``` python
    dateutils.quarter_from_yq(year, quarter)
    ```

    __Example__

    ``` python
    dateutils.quarter_from_yq(2022, 3) # DateQuarter obj:<DateQuarter-2022,3Q>
    ```

## quarter_from_ym

!!! success "quarter_from_ym"

    Return a DateQuarter object, and params include year and month.

    ``` python
    dateutils.quarter_from_ym(year, month)
    ```

    __Example__

    ``` python
    dateutils.quarter_from_ym(2022, 3) # DateQuarter obj:<DateQuarter-2022,3Q>
    ```

## to_quarter

!!! success "to_quarter"

    Return a DateQuarter object of a time string.

    ``` python
    dateutils.to_quarter(time_str)
    ```

    __Example__

    ``` python
    dateutils.to_quarter("2022-07-17") # DateQuarter obj: <DateQuarter-2022,3Q>
    ```

## quarters_within

!!! success "quarters_within"

    Return a generator which will generate the DateQuater objects between a start date and end date. You can get the last quarter in the generator if you set param `include_last=True` which is `False` by default.

    ``` python
    dateutils.quarters_within(start, end, include_last)
    ```

    __Example__

    ``` python
    qs = dateutils.quarters_within("2021-03-28", "2022-07-17", include_last=True)
    list(qs) # [<DateQuarter-2021,1Q>, <DateQuarter-2021,2Q>,...., <DateQuarter-2022,3Q>]
    ```

## Quarter operation

!!! success "Quarter operation"

    Some operations are supported based on DateQuater object. Please refer the examples below:

    ``` python
    q = dateutils.quarter_from_yq(2022, 3)

    q.year # 2022
    q.quarter # 3

    q.start_date # 2022-07-01
    q.end_date # 2022-09-30

    q.days()  # generator, which will generate the date in such quarter
    list(q.days()) # [datetime.date(2022, 7, 1), datetime.date(2022, 7, 2),....., datetime.date(2022, 9, 30)]

    q + 10 # <DateQuarter-2025,1Q>
    q1 = dateutils.quater_from_yq(2021, 1) # <DateQuarter-2021,1Q>
    q - q1 # 6
    q < q1 # False
    "2022-6-28" in q # False
    "2022-8-28" in q # True
    ```

## Other examples

!!! success "Other examples"

    The date info returned can also be assigned as a param of dateutils. Here are some examples:

    ``` python
    dt_now = dateutils.now()  # 2022-02-07 09:49:14
    # 1. date after 10 days
    dt_10_days = dateutils.dateadd(dt_now, 10) # 2022-02-17 09:49:14
    # 2. month after 10 days
    dt_month_10_days = dateutils.month(dt_10_days) # 2
    # 3. difference between 2 days
    dt_10_days_before = dateutils.dateadd(dt_now, -10)
    date_df = dateutils.datediff(dt_10_days_before, dt_10_days, unit="D") # 20
    # 4. handle the time string with time-zone info with local timezone of "Asia/Shanghai" (UTC+8)
    time_str = "2021-07-17T08:15:41.106+00:00"
    time_day = dateutils.day(time_str) # 17
    time_month = dateutils.month(time_str) # 7
    time_year = dateutils.year(time_str) # 2021
    time_hour = dateutils.hour(time_str) # 16
    time_date = dateuitls.date(time_year, time_month, time_day) # 2021-07-17
    ```
