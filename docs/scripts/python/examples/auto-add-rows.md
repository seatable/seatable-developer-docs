{%
    include-markdown "includes.md"
    start="<!--add-row-example-start-->"
    end="<!--add-row-example-end-->"
%}

Unlike JavaScript, Python scripts allow you to handle single- or multiple-select options, which make you capable of checking if the needed options exist and of creating them if necessary directly inside the script.

```python
from seatable_api import Base, context
from seatable_api.date_utils import dateutils
"""
This script add two expenses rows in a ledger. Before adding them, 
it checks if they have already been added for the current month.
"""

base = Base(context.api_token, context.server_url)
base.auth()

# Get date objects on the 10th and 20th of the current month
date = dateutils.today()
date10 = dateutils.date(dateutils.year(date), dateutils.month(date), 10)
date20 = dateutils.date(dateutils.year(date), dateutils.month(date), 20)

# Check if the options you will need already exist, and create them if necessary
options_to_add = []
current_options = base.get_column_by_name('Daily expenses', 'Type (single select)')['data']['options']
cloud_service_option = [o for o in current_options if o['name'] == 'Cloud service']
if not cloud_service_option :
    options_to_add.append({"name": "Cloud service", "color": "#aaa", "textColor": "#000000"})
daily_office_option = [o for o in current_options if o['name'] == 'Daily office']
if not daily_office_option :
    options_to_add.append({"name": "daily office", "color": "#aaa", "textColor": "#000000"})
if options_to_add :
    base.add_column_options('Daily expenses', 'Type (single select)', options_to_add)

# Check if the monthly expense items have already been created and eventually create them
feeAWS = {}
feeAWSCurrentMonth = base.query('select * from `Daily expenses` where Name="Amazon Cloud Service" and Date="' + date10 + '"')
if not feeAWSCurrentMonth :
    feeAWS = {'Name': 'Amazon Cloud Service', 
              'Date': date10,
              'Type': 'Cloud service',
              'Type (single select)': 'Cloud service',
             }
             
feeClean = {}
feeCleanCurrentMonth = base.query('select * from `Daily expenses` where Name="Clean" and Date ="' + date20 + '"')
if not feeCleanCurrentMonth :
    feeClean = {'Name': 'Clean', 
                'Date': date20,
                'Type': 'Daily office',
                'Type (single select)': 'Daily office',
                'Fee': 260
               }

# Create the monthly expense items (if needed)
if (feeAWS) :
    base.append_row('Daily expenses', feeAWS);
if (feeClean) :
    base.append_row('Daily expenses', feeClean);
```