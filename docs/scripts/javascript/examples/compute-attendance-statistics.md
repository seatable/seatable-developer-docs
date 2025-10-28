{%
    include-markdown "includes.md"
    start="<!--attendance-statistics-example-start-->"
    end="<!--attendance-statistics-example-end-->"
%}

``` javascript
// Computes, from a list of clocking times, daily clock in (earliest clocking) 
// and clock out (latest clocking) times for each day and staff member
const originTableName = 'Clocking table';
const originViewName = 'Default View';
const originNameColumnName = 'Name';
const originDepartmentColumnName = 'Department';
const originDateColumnName = 'Date';
const originTimeColumnName = 'Clocking time';

const targetTableName = 'Attendance statistics';
const targetNameColumnName = 'Name';
const targetDepartmentColumnName = 'Department';
const targetDateColumnName = 'Date';
const targetStartTimeColumnName = 'Clock-in';
const targetEndTimeColumnName = 'Clock-out';
const targetTable = base.getTableByName(targetTableName);

const table = base.getTableByName(originTableName);
const view = base.getViewByName(table, originViewName);
const rows = base.getRows(table, view);

// Sort the rows in the table according to the date column;
rows.sort((row1, row2) => {
    if (row1[originDateColumnName] < row2[originDateColumnName]) {
      return -1;
    } else if (row1[originDateColumnName] > row2[originDateColumnName]) {
      return 1; 
    } else {
      return 0;
    }
});

/*
 Group all rows via date and save them to groupedRows, the format
 of the object is {'2020-09-01': [row, ...], '2020-09-02': [row, ...]}
*/
const groupedRows = {};
rows.forEach((row) => {
  const date = row[originDateColumnName]; 
  if (!groupedRows[date]) {
    groupedRows[date] = [];
  }
  groupedRows[date].push(row);
});

const dateKeys = Object.keys(groupedRows);

// Traverse all the groups in groupedRows
dateKeys.forEach((dateKey) => { 
  // Get all clocking data of all members for the current date
  const dateRows = groupedRows[dateKey];
  const staffDateStatItem = {};
  // Traverse these rows and group by the name of the employee, get the clock-in and clock-out time of each employee that day, and save it to staffDateStatItem
  // the format is { EmployeeName: {Name: 'EmployeeName', Date: '2020-09-01', Clock-in: '08:00', Clock-out: '18:00'},... }
  dateRows.forEach((row)=> {
    const name = row[originNameColumnName];
    if (!staffDateStatItem[name]) {
      // Generate a new row based on the original row data, and add Clock-in and Clock-out columns in the newly generated row
      staffDateStatItem[name] = { [targetNameColumnName]: name, [targetDateColumnName]: row[originDateColumnName], [targetDepartmentColumnName]: row[originDepartmentColumnName], [targetEndTimeColumnName]: row[originTimeColumnName], [targetStartTimeColumnName]: row[originTimeColumnName]};
    } else {
      // When another record (same employee and same date) is found, compare the time, choose the latest one as the Clock-out time, and the earliest one as the Clock-in time
      const time = row[originTimeColumnName];
      const staffItem = staffDateStatItem[name];
      if (staffItem[targetStartTimeColumnName] > time) {
          staffItem[targetStartTimeColumnName] = time;
      } else if (staffItem[targetEndTimeColumnName] < time) {
          staffItem[targetEndTimeColumnName] = time;
      }
    }
  });
  // Write the attendance data of all employees on the current date into the table
  Object.keys(staffDateStatItem).forEach((name) => {
    base.appendRow(targetTable, staffDateStatItem[name]);
  });  
});
```