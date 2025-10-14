# SeaTable MySQL Synchronization

This Python script facilitates the synchronization of data from a MySQL database to a SeaTable table, ensuring consistency and updating records seamlessly. Variables are present at the beginning of the script to easily adapt the names of both Seatable and MySQL tables and columns. The `Sync MySQL` table requires a single `Name` text-type column for the script to be able to run.

## Process Overview

1. **Initializes connections** to both (a) SeaTable and (b) MySQL databases.
2. **Fetches existing data** from the `Name` column of the `Sync MySQL` SeaTable table.
3. **Retrieves data** from the MySQL `order` table.
4. **Compares MySQL data with SeaTable data** to identify new records by matching the `name` field.
5. **Adds new records** from MySQL to SeaTable (`Sync MySQL`) for synchronization.


## Code

```python
import pymysql
from seatable_api import Base, context
"""
This Python script facilitates the synchronization of data 
from a MySQL database to a SeaTable table, ensuring consistency 
and updating records seamlessly.
"""

# SeaTable base config
SERVER_URL = context.server_url or 'http://127.0.0.1:8000'
API_TOKEN = context.api_token or '...'

# SeaTable table config
ST_TABLE_NAME = 'Sync MySQL'
ST_NAME_COLUMN = 'Name'

# MySQL config
HOST = 'localhost'
USER = 'username'
PASSWORD = 'topsecret'
MYSQL_DB = 'seatable'
MYSQL_TABLE = 'order'
MYSQL_NAME_COLUMN = 'name'

def sync_mysql():
    # 1. Initialize connection
    # 1. a) SeaTable authentication
    base = Base(API_TOKEN, SERVER_URL)
    base.auth()

    # 1. b) MySQL connection
    connection = pymysql.connect(host=HOST, user=USER, password=PASSWORD, db=MYSQL_DB)

    # 2. Fetch existing rows from seaTable
    rows = base.list_rows(ST_TABLE_NAME)
    row_keys = [row.get(ST_NAME_COLUMN) for row in rows]

    # 3. Retrieving data from MySQL
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = "SELECT * FROM " + MYSQL_TABLE
        cursor.execute(sql)
        mysql_data = cursor.fetchall()

    # Synchronization
    rows_data = []
    for item in mysql_data:
        # 4. Look for data from MySQL not present in SeaTable
        if item.get(MYSQL_NAME_COLUMN) not in row_keys:
            row_data = {
                ST_NAME_COLUMN: item.get(MYSQL_NAME_COLUMN),
            }
    # 5. Eventually add missing records
    if rows_data :
        base.batch_append_rows(TABLE_NAME, rows_data)


if __name__ == '__main__':
    sync_mysql()
```
