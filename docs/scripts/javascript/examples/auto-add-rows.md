{%
    include-markdown "includes.md"
    start="<!--add-row-example-start-->"
    end="<!--add-row-example-end-->"
%}

With JavaScript scripts, you have to ensure **before** running the script that the options you want to add (in this case `Cloud service` and `Daily office`) already exist in your "single select"-type column.

``` javascript
// Record monthly repetitive expenses in a ledger

const table = base.getTableByName('Daily expenses');

// Get date objects on the 10th and 20th of the current month
var date = new Date();
var date10 = new Date(date.setDate(10));
var date20 = new Date(date.setDate(20));

// Check if the monthly expense items have already been created and eventually create them
const AWSCondition = "Name='Amazon Cloud Service' and Date='" + base.utils.formatDate(date10) + "'";
const feeAWSCurrentMonth = base.filter('Daily expenses', 'Default View', AWSCondition);
if (feeAWSCurrentMonth.count() == 0) {
  var feeAWS = { 'Name': 'Amazon Cloud Service', 
                 'Date': base.utils.formatDate(date10),
                 'Type': 'Cloud service',
                 'Type (single select)': 'Cloud service',
               };
}
const CleanCondition = "Name='Clean' and Date='" + base.utils.formatDate(date20) + "'";
const feeCleanCurrentMonth = base.filter('Daily expenses', 'Default View', CleanCondition);
if (feeCleanCurrentMonth.count() == 0) {
  var feeClean = { 'Name': 'Clean', 
                   'Date': base.utils.formatDate(date20),
                   'Type': 'Daily office',
                   'Type (single select)': 'Daily office',
                   'Fee': 260
                 };
}

// Auto add data (if needed)
if (feeAWS) {
  base.appendRow(table, feeAWS);
}
if (feeClean) {
  base.appendRow(table, feeClean);
}
```
