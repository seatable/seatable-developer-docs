{%
    include-markdown "includes.md"
    start="<!--attendance-statistics-example-start-->"
    end="<!--attendance-statistics-example-end-->"
%}

```python
from seatable_api import Base, context
"""
This script computes, from a list of clocking times, 
daily clock in  (earliest clocking) and clock out 
(latest clocking) times for each day and staff member.
"""

base = Base(context.api_token, context.server_url)
base.auth()

origin_table_name = 'Clocking table'
origin_view_name = 'Default View'
origin_name_column_name = 'Name'
origin_department_column_name = 'Department'
origin_date_column_name = 'Date'
origin_time_column_name = 'Clocking time'

target_table_name = 'Attendance statistics'
target_name_column_name = 'Name'
target_department_column_name = 'Department'
target_date_column_name = 'Date'
target_start_time_column_name = 'Clock-in'
target_end_time_column_name = 'Clock-out'

def get_date(e):
  return e[origin_date_column_name]

#table = base.getTableByName(origin_table_name)
#view = base.getViewByName(table, origin_view_name)
rows = base.list_rows(origin_table_name, origin_view_name)

# Sort the rows in the Clocking table according to the date column
rows.sort(key=get_date)

# Group all rows via date and save them to groupedRows, the format
# of the object is {'2020-09-01': [row, ...], '2020-09-02': [row, ...]}
grouped_rows = {}
date_stat_items = []
for row in rows :
    date = row[origin_date_column_name]
    if date not in grouped_rows :
        grouped_rows[date] = []
    grouped_rows[date].append(row)

# Traverse all the groups in grouped_rows
for date_key in grouped_rows :
    # Get all clocking data of all members for the current date
    date_rows = grouped_rows[date_key]
    staff_date_stat_item = {}
    # Traverse these rows and group by the name of the employee, get the clock-in and clock-out time of each employee that day, and save it to staffDateStatItem
    # the format is { EmployeeName: {Name: 'EmployeeName', Date: '2020-09-01', Clock-in: '08:00', Clock-out: '18:00'},... }
    for row in date_rows :
        name = row[origin_name_column_name]
        if name not in staff_date_stat_item :
            # Generate a new row based on the original row data, and add Clock-in and Clock-out columns in the newly generated row
            staff_date_stat_item[name] = { 
                target_name_column_name: name, 
                target_date_column_name: row[origin_date_column_name],
                target_department_column_name: row[origin_department_column_name],
                target_end_time_column_name: row[origin_time_column_name],
                target_start_time_column_name: row[origin_time_column_name]
            }
        else :
            # When another record (same employee and same date) is found, compare the time, choose the latest one as the Clock-out time, and the earliest one as the Clock-in time
            time = row[origin_time_column_name]
            staff_item = staff_date_stat_item[name]
            if staff_item[target_start_time_column_name] > time :
                staff_item[target_start_time_column_name] = time
            elif staff_item[target_end_time_column_name] < time :
                staff_item[target_end_time_column_name] = time
    for staff in staff_date_stat_item :
        date_stat_items.append(staff_date_stat_item[staff])

# Write the attendance data of all employees on the current date into the table
base.batch_append_rows(target_table_name,date_stat_items)
```