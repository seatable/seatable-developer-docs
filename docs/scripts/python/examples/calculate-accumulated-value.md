{%
    include-markdown "includes.md"
    start="<!--accumulated-value-example-start-->"
    end="<!--accumulated-value-example-end-->"
%}

```python
from seatable_api import Base, context
from seatable_api.date_utils import dateutils
"""
This script accumulates the values of the current row and the previous rows, 
and records the result to the current row (as the *Calculate accumulated value*
operation from the data processing menu).
"""

base = Base(context.api_token, context.server_url)
base.auth()

table_name = 'Accumulated value'
view_name = 'Default View'

# Name of the column that records total number at a specific time
value_column_name = 'Value to add'
# Name of the column that need to calculate incremental value
incremental_column_name = 'Incremental total'

view = base.get_view_by_name(table_name, view_name)
rows = base.list_rows(table_name, view_name)

# If current view is a grouped view
if 'groupbys' in view and len(view['groupbys']) > 0 :
#    # Get group view rows
    grouping_column = [c for c in base.list_columns(table_name) if 'column_key' in view['groupbys'][0] and c['key'] == view['groupbys'][0]['column_key']]
    if grouping_column and len(grouping_column) == 1 :
            grouping_column_name = grouping_column[0]['name']
    group_values = []
    for row in rows :
        if row[grouping_column_name] not in group_values :
            group_values.append(row[grouping_column_name])
    for value in group_values :
        group_rows = [r for r in rows if r[grouping_column_name] == value]
        incremental_total = 0
        for row_index, row in enumerate(group_rows) :
            current_number = row[value_column_name];
            if current_number :
                # Calculate increment
                # If there is no previous row, set increase_count to 0
                previous_number = 0 if row_index == 0 else incremental_total
                increase_count = current_number + previous_number
                incremental_total = increase_count
                # Set calculated increment to row
                base.update_row(table_name, row['_id'], {incremental_column_name: increase_count})
else :
    incremental_total = 0
    for row_index, row in enumerate(rows) :
        current_number = row[value_column_name];
        if current_number :
            # Calculate increment
            # If there is no previous row, set increase_count to 0
            previous_number = 0 if row_index == 0 else incremental_total
            increase_count = current_number + previous_number
            incremental_total = increase_count
            # Set calculated increment to row
            base.update_row(table_name, row['_id'], {incremental_column_name: increase_count})
```