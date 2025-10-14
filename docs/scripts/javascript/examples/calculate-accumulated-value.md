{%
    include-markdown "includes.md"
    start="<!--accumulated-value-example-start-->"
    end="<!--accumulated-value-example-end-->"
%}

``` javascript
// Accumulates the values of the current row and the previous rows, and records the result to the current row
const tableName = 'Accumulated value';
const viewName = 'Default View';

// Name of the column that records total number at a specific time
const valueColumnName = 'Value to add';
// Name of the column that need to calculate incremental value
const incrementalColumnName = 'Incremental total';

const table = base.getTableByName(tableName);
const view = base.getViewByName(table, viewName);

// If current view is a grouped view
if (view.groupbys && view.groupbys.length > 0) {
  // Get group view rows
  const groupViewRows = base.getGroupedRows(table, view);

  groupViewRows.map((group) => {
    let incrementalTotal = 0;
    group.rows.map((row, rowIndex, rows) => {
        // Get current row value
        const currentNumber = row[valueColumnName];
        if (!currentNumber) return;
        // Calculate increment
        const previousRow = rows[rowIndex - 1];
        // If there is no previousRow, set increaseCount to 0
        const previousNumber = rowIndex>0 ? incrementalTotal : 0;
        const increaseCount = currentNumber + previousNumber;
        incrementalTotal = increaseCount;
        // Set calculated increment to row
        base.updateRow(table, row, {[incrementalColumnName]: increaseCount});
    });
  });
} else {
    // Get current view rows
    let incrementalTotal = 0;
    const rows = base.getRows(table, view);
    rows.forEach((row, rowIndex, rows) => {
    // Calculate increment
    const currentNumber = row[valueColumnName];
    if (!currentNumber) return;
    const previousRow = rows[rowIndex - 1];
    // If there is no previousRow, set increaseCount to 0
    const previousNumber = rowIndex>0 ? incrementalTotal : 0;
    const increaseCount = currentNumber + previousNumber;
    incrementalTotal = increaseCount;
    // Set calculated increment to row
    base.updateRow(table, row, {[incrementalColumnName]: increaseCount});
  });
}
```