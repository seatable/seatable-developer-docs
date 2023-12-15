# SeaTable MySQL Synchronization

This Python script facilitates the synchronization of data from a MySQL database to a SeaTable table.

## Functionality

- Configuration Setup: Defines configurations for SeaTable, specifying server URL and API token, as well as MySQL database connection details.
- Data Sync Process:

      - Establishes a connection to the SeaTable base and authenticates using the provided API token and server URL.
      - Retrieves existing rows from a designated SeaTable table (Table1) and extracts specific column (Name) data.
      - Connects to the MySQL database (seatable) and fetches data from the order table.
      - Compares MySQL data with SeaTable data to identify new records.
      - Appends new records found in MySQL but not present in SeaTable to ensure synchronization.

## Process Overview

1. Initializes connections to both SeaTable and MySQL databases.
1. Fetches existing rows and column data from the designated SeaTable table (Table1).
1. Retrieves data from the MySQL order table.
1. Compares MySQL data with SeaTable data to identify new records by matching the 'name' field.
1. Adds new records from MySQL to SeaTable (Table1) for synchronization.

This script enables the automated synchronization of data between a MySQL database and a SeaTable table, ensuring consistency and updating records seamlessly.

## Code

```python
import pymysql
from seatable_api import Base, context

# Base config
SERVER_URL = context.server_url or 'http://127.0.0.1:8000'
API_TOKEN = context.api_token or '...'

# Table config
TABLE_NAME = 'Table1'
NAME_COLUMN = 'Name'

# MySQL config
HOST = 'localhost'
USER = ''
PASSWORD = ''
DB = 'seatable'

def sync_mysql():
    """Sync database into the table
    """
    # base initiated and authed
    base = Base(API_TOKEN, SERVER_URL)
    base.auth()

    rows = base.list_rows(TABLE_NAME)
    row_keys = [row.get(NAME_COLUMN) for row in rows]

    # mysql data
    connection = pymysql.connect(host=HOST, user=USER, password=PASSWORD, db=DB)

    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = "SELECT * FROM order"
        cursor.execute(sql)
        mysql_data = cursor.fetchall()

    # sync
    for item in mysql_data:
        if item.get('name') not in row_keys:
            row_data = {
                'Name': item.get('name'),
            }
            base.append_row(TABLE_NAME, row_data)


if __name__ == '__main__':
    sync_mysql()
```
