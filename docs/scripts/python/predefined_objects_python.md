# Predefined Objects and Methods (Python)

This is a list of all available objects and methods in SeaTable with python scripts.

For a more detailed description of the used parameters, refer to the data model at the [SeaTable API Reference](https://api.seatable.io/reference/models).

!!! tip "Don't forget to authenticate"

    Every python script requires an authorization. All the examples does not contain the required lines of code.

    ```
    from seatable_api import Base, context
    base = Base(context.api_token, context.server_url)
    base.auth()
    ```

## Base object

Base represents a table in SeaTable. The `base` object provide a way to read, manipulate and output data in/from your base. The following methods are available.

### Metadata

??? question "get_metadata"

    Get the complete metadata of a table. The metadata will not contain the concrete rows of the table.

    ``` js
    base.get_metadata() // (1)!
    ```

    1.  possible result:
        ```
        {
            'tables': [{
                '_id': '4krH',
                'name': 'Contact',
                'is_header_locked': False,
                'columns': [{
                    'key': '0000',
                    'type': 'text',
                    'name': 'Name',
                    'editable': True,
                    'width': 200,
                    'resizable': True,
                    'draggable': True,
                    'data': None,
                    'permission_type': '',
                    'permitted_users': []
                }, {
                    'key': 'M31F',
                    'type': 'text',
                    'name': 'Email',
                    'editable': True,
                    'width': 200,
                    'resizable': True,
                    'draggable': True,
                    'data': None,
                    'permission_type': '',
                    'permitted_users': []
                }],
                'views': [{
                    '_id': '0000',
                    'name': 'Default view',
                    'type': 'table',
                    'is_locked': False,
                    'filter_conjunction': 'And',
                    'filters': [],
                    'sorts': [],
                    'groupbys': [],
                    'group_rows': [],
                    'groups': [],
                    'colorbys': {},
                    'hidden_columns': [],
                    'rows': [],
                    'formula_rows': {},
                    'link_rows': {},
                    'summaries': {},
                    'colors': {}
                }]
            }]
        }
        ```

### Table

??? question "add_table"

    Add a table into a base.

    ``` python
    base.add_table(table_name, lang='en');
    ```

    __Example__
    ``` js
    const table = base.getActiveTable();
    output.text(`The name of the active table is: ${table.name}`);
    ```

### Column

??? question "List columns"

    List all rows of the table/view.

    ``` python
    base.list_columns(table_name, view_name=None);
    ```

    __Example__

    ``` python
    base.list_columns('Table1', default)
    ```

??? question "Insert column"

    Insert or append a column to a table.

    ``` python
    base.insert_column(table_name, column_name, column_type, column_key=None, column_data=None)
    ```

    __Examples__

    ``` python
    base.insert_column('Table1', 'New long text column', 'long text')
    ```

    ``` python
    from seatable_api.constants import ColumnTypes
    base.insert_column('Table1', 'Link', ColumnTypes.LINK, column_data={
        'table':'Table1',
        'other_table':'Test_User'
    })
    ```

??? question "Rename column"

    Rename a column.

    ``` python
    base.rename_column(table_name, column_key, new_column_name)
    ```

    __Example__

    ``` python
    base.rename_column('Table1', 'kSiR', 'new column name')
    ```

??? question "Freeze column"

    Freeze a column.

    ``` python
    base.freeze_column(table_name, column_key, frozen)
    ```

    __Example__

    ``` python
    base.freeze_column('Table1', '0000', True)
    ```

??? question "Move column"

    Move column. In this example, the column with the key `loPx` will be moved to the right of the column `0000`.

    ``` python
    base.move_column(table_name, column_key, target_column_key)
    ```

    __Example__

    ``` python
    base.move_column('Table1', 'loPx', '0000')
    ```

??? question "Modify column type"

    Change the column type of an existing column

    ``` python
    base.modify_column_type(table_name, column_key, new_column_type)
    ```

    __Example__

    ``` python
    base.modify_column_type('Table1', 'nePI', 'checkbox')
    ```

??? question "Add column options"

    Used by single-select or multiple-select type columns to add new options.

    ``` python
    add_column_options(self, table_name, column, options)
    ```

    __Example__

    ``` python
    base.add_column_options('Table1', 'My choices', [
        {"name": "ddd", "color": "#aaa", "textColor": "#000000"},
        {"name": "eee", "color": "#aaa", "textColor": "#000000"},
        {"name": "fff", "color": "#aaa", "textColor": "#000000"},
    ])
    ```

??? question "Add column cascade settings"

    Used by single-select column, to add a limitation of child column options according to the option of parent column.

    ``` python
    add_column_cascade_settings(table_name, child_column, parent_column, cascade_settings)
    ```

    __Example__

    ``` python
    base.add_column_cascade_settings("Table1", "single-op-col-c", "single-op-col", {
        "aaa": ["aaa-1", "aaa-2"], # If “aaa” is selected by parent column, the available options of child column are "aaa-1 and aaa-2"
        "bbb": ["bbb-1", "bbb-2"],
        "ccc": ["ccc-1", "ccc-2"]
    })
    ```

??? question "Delete column"

    Deletes a column from the table.

    ``` python
    base.delete_column(table_name, column_key)
    ```

    __Example__

    ``` python
    base.delete_column('Table1', 'bsKL')
    ```

### Rows

??? question "Get row"

    Get a row of a table by its row ID..

    ``` python
    base.get_row(table_name, row_id)
    ```

    __Example__

    ``` python
    row = base.get_row('Table1', 'U_eTV7mDSmSd-K2P535Wzw')
    ```
    
??? question "Get rows"

    Get rows of a table.

    ``` python
    base.list_rows(table_name, view_name=None, order_by=None, desc=False, start=None, limit=None)
    ```

    __Examples__

    ``` python
    rows = base.list_rows('Table1')
    rows = base.list_rows('Table1', view_name='default', order_by='Age', desc=True, start=5, limit=20)
    ```

    __Hint__: The query with SQL allows to retrieve more rows and offers more filter options.


??? question "Query"

    Query a base using SQL.

    ``` python
    base.query(sql-statement)
    ```

    __Example: Get everything with a wildcard__

    ``` js
    json_data = base.query('select * from Users') // (1)!
    print(json.dumps(json_data, indent=2))
    ```

    1.  Returns for example the following:
        ``` json
        [
            {
                "Name": "Thomas",
                "_id": "VkyADGkFRiif0bEVHd-CtA",
                "_ctime": "2023-08-16T15:04:56.018Z",
                "_mtime": "2023-08-17T07:02:59.585Z",
                "_creator": "a5adebe279e04415a28b2c7e256e9e8d@auth.local",
                "_last_modifier": "a5adebe279e04415a28b2c7e256e9e8d@auth.local",
                "_locked": null,
                "_locked_by": null,
                "_archived": false
            },
            {
                "Name": "Steve",
                "_id": "UevpAVOjRrmbfqMmpsuTEg",
                "_ctime": "2023-08-17T07:03:00.292Z",
                "_mtime": "2023-08-17T07:03:00.801Z",
                "_creator": "a5adebe279e04415a28b2c7e256e9e8d@auth.local",
                "_last_modifier": "a5adebe279e04415a28b2c7e256e9e8d@auth.local",
                "_locked": null,
                "_locked_by": null,
                "_archived": false
            },
        ]
        ```

    __Example: WHERE__

    ``` python
    json_data = base.query('select name, price from Bill where year = 2021')
    print(json.dumps(json_data, indent=2))
    ```

    __Example: ORDER BY__

    ``` python
    json_data = base.query('select name, price, year from Bill order by year')
    print(json.dumps(json_data, indent=2))
    ```

    __Example: GROUP BY__

    ``` python
    json_data = base.query('select name, sum(price) from Bill group by name')
    print(json.dumps(json_data, indent=2))
    ```

    __Example: DISTINCT__

    ``` python
    json_data = base.query('select distinct name from Bill')
    print(json.dumps(json_data, indent=2))
    ```

??? question "Append row"

    Append a row to a table.

    ``` python
    base.append_row(table_name, row_data)
    ```

    __Example__

    ``` python
    row_data = {
        "Name": "Ron"
    }
    base.append_row('Table1', row_data)
    ```

??? question "Insert row"

    Insert a row to a table.

    ``` python
    base.insert_row(table_name, row_data, row_id)
    ```

    __Example__

    ``` python
    row_data = {
        "Name": "Ron"
    }

    base.insert_row('Table1', row_data, 'U_eTV7mDSmSd-K2P535Wzw')
    ```

??? question "Update row"

    Update a row in a table.

    ``` python
    base.update_row(table_name, row_id, row_data)
    ```

    __Example__

    ``` python
    row_data = {
        "Name": "Ron"
    }

    base.update_row('Table1', 'U_eTV7mDSmSd-K2P535Wzw', row_data)
    ```

??? question "Batch append rows"

    Append multiple rows to a table.

    ``` python
    base.batch_append_rows(table_name, rows_data)
    ```

    __Example__

    ``` python
    rows_data = [{
        'Name': 'Ron',
        'Birthday': '1975-01-01'
    }, {
        'Name': 'Richard',
        'Birthday': '1978-10-08'
    }]
    base.batch_append_rows('Table6', rows_data)
    ```

??? question "Delete row"

    Delete a row in a table.

    ``` python
    base.delete_row(table_name, row_id)
    ```

    __Example__

    ``` python
    base.delete_row('Table1', 'U_eTV7mDSmSd-K2P535Wzw')
    ```

??? question "Batch delete rows"

    Delete multiple rows in a table.

    ``` python
    base.batch_delete_rows(table_name, row_ids)
    ```

    __Example__

    ``` python
    del_rows = rows[:3]
    row_ids = [row['_id'] for row in del_rows]
    base.batch_delete_rows('Table1', row_ids)
    ```

### Links

??? question "Get link id"

    Get the link id by column name

    ``` python
    base.get_column_link_id(table_name, column_name)
    ```

    __Example__

    ``` python
    base.get_column_link_id('Table1', 'Record')
    ```

??? question "Get linked records"

    List the linked records of rows. You can get the linked records of multiple rows.

    ``` python
    base.get_linked_records(table_id, link_column_key, rows)
    ```

    __Example__

    ``` python
    # rows: a list, each item of the which contains a row info including row_id, offset (defualt by 0) and limit (default by 10) of link table.
    base.get_linked_records('0000', '89o4', rows=[
        {'row_id': 'FzNqJxVUT8KrRjewBkPp8Q', 'limit': 2, 'offset': 0},
        {'row_id': 'Jmnrkn6TQdyRg1KmOM4zZg', 'limit': 20}
    ])
    # a key-value data structure returned as below
    # key: row_id of link table
    # value: a list which includes the row info of linked table
    {
        'FzNqJxVUT8KrRjewBkPp8Q': [
            {'row_id': 'LocPgVvsRm6bmnzjFDP9bA', 'display_value': '1'},
            {'row_id': 'OA6x7CYoRuyc2pT52Znfmw', 'display_value': '3'},
            ...
        ],
        'Jmnrkn6TQdyRg1KmOM4zZg': [
            {'row_id': 'LocPgVvsRm6bmnzjFDP9bA', 'display_value': '1'},
            {'row_id': 'OA6x7CYoRuyc2pT52Znfmw', 'display_value': '3'},
             ...
        ]
    }
    ```

??? question "Add link"

    Add links, link other table records. A link column must already exist.

    ``` python
    base.add_link(link_id, table_name, other_table_name, row_id, other_row_id)
    ```

    __Example__

    ``` python
    base.add_link('5WeC', 'Table1', 'Table2', 'CGtoJB1oQM60RiKT-c5J-g', 'PALm2wPKTCy-jdJNv_UWaQ')
    ```

??? question "Update link"

    Modify the info of link-type column.

    ``` python
    update_link(self, link_id, table_name, other_table_name, row_id, other_rows_ids)
    ```

    __Example__

    ``` python
    base.update_link(
        link_id='r4IJ',
        table_name='Table1',
        other_table_name='Table2',
        row_id='BXhEm9ucTNu3FjupIk7Xug',
        other_rows_ids=[
          'exkb56fAT66j8R0w6wD9Qg',
          'DjHjwmlRRB6WgU9uPnrWeA'
        ]
    )
    ```

??? question "Batch update links"

    Batch update infos of link-type columns.

    ``` python
    base.batch_update_links(link_id, table_name, other_table_name, row_id_list, other_rows_ids_map)
    ```

    __Example__

    ``` python
    link_id = "WaW5"
    table_name = "Table1"
    other_table_name ="Table2"
    row_id_list = ["fRLglslWQYSGmkU7o6KyHw","FseN8ygVTzq1CHDqI4NjjQ"]
    other_rows_ids_map = {
        "FseN8ygVTzq1CHDqI4NjjQ":["OcCE8aX8T7a4dvJr-qNh3g","JckTyhN0TeS8yvH8D3EN7g"],
        "fRLglslWQYSGmkU7o6KyHw":["MdfUQiWcTL--uMlrGtqqgw","E7Sh3FboSPmfBlDsrj_Fhg","UcZ7w9wDT-uVq4Ohtwgy9w"]
    }
    base.batch_update_links(link_id, table_name, other_table_name, row_id_list, other_rows_ids_map)
    ```

??? question "Remove link"

    Delete the link row.

    ``` python
    base.remove_link(link_id, table_name, other_table_name, row_id, other_row_id)
    ```

    __Example__

    ``` python
    base.remove_link('5WeC', 'Table1', 'Table2', 'CGtoJB1oQM60RiKT-c5J-g', 'PALm2wPKTCy-jdJNv_UWaQ')
    ```


### Files

??? question "Download (simple method)"

    Download a file to a local path.

    ``` python
    base.download_file(file_url, save_path)
    ```

    __Example__

    ``` python
    file_url = "https://cloud.seatable.io/workspace/74/asset-preview/41cd05da-b29a-4428-bc31-bd66f4600817/files/2020-10/invoice.pdf"
    save_path = "/tmp/invoice.pdf"
    base.download_file(file_url, save_path)
    ```

??? question "Download (detailed method)"

    This detailed method is for handling complex situations where the file is extremly large or the internet connection is slow. In this example I assume that there exist a file like `https://cloud.seatable.io/dtable-web/workspace/74/asset-preview/41cd05da-b29a-4428-bc31-bd66f4600817/files/2020-10/invoice.pdf`.

    ``` python
    download_link = base.get_file_download_link(file_url)
    ```

    __Example__

    ``` python
    import requests
    download_link = base.get_file_download_link('files/2020-10/invoice.pdf')
    response = requests.get(download_link)
    ```

??? question "Upload (simple method)"

    Upload a file from your local drive, memory or a website.

    ``` python
    base.upload_local_file(file_path, name=None, file_type='file', replace=False)
    # or
    base.upload_bytes_file(name, content, file_type='file', replace=False)
    ```

     __Example: Upload a file from local hard drive__

    ``` python
    local_file = '/Users/Markus/Downloads/seatable-logo.png'
    info_dict = base.upload_local_file(local_file, name='seatable-logo.png', file_type='image', replace=True)
    ```

    __Example: Upload a file from memory__

    ``` python
    local_file = '/Users/Markus/Downloads/seatable-logo.png'
    with open (local_file, 'rb') as f:
      content = f.read()
    info_dict = base.upload_bytes_file = ('seatable-logo.png', content, file_type='image')
    ```

    __Example: Upload a file from a website__

    ``` python
    import requests
    file_url = 'https://seatable.io/wp-content/uploads/2021/09/seatable-logo.png'
    response = requests.get(file_url)
    info_dict = base.upload_bytes_file = ('seatable-logo.png', response.content)
    ```

??? question "Upload (detailed method)"

    Get a file upload link.

    ``` python
    base.get_file_upload_link()
    ```

    __Example__

    ``` python
    # Get the upload link and file path allocated by server
    upload_link_dict = base.get_file_upload_link()
    parent_dir = upload_link_dict['parent_path']
    upload_link = upload_link_dict['upload_link'] + '?ret-json=1'

    # Upload the file
    upload_file_name = "file_uploaded.txt"
    replace = 1
    response = requests.post(upload_link, data={
        'parent_dir': parent_dir,
        'replace': 1 if replace else 0
    }, files={
        'file': (upload_file_name, open('/User/Desktop/file.txt', 'rb'))
    })
    ```

??? question "List files"

    List files in custom folders.

    ``` python
    base.list_custom_assets(path)
    ```

    __Example__

    ``` python
    folder_dir = "/Main/photos"
    base.list_custom_assets(folder_dir)
    # A dict will be returned including dir and file
    {
    "dir": [{'name': "MyDir"}, ...]
    "file":[{'name': "sky.png"}, ....]
    }
    ```

??? question "Get file info"

    The data structure returned can be used to updated cells of file column.

    ``` python
    base.get_custom_file_info(path, name)
    ```

    __Example__

    ``` python
    folder_dir = "/Main/"
    file_name = "sky.png"
    info_dict = base.get_custom_file_info(path, name)
    row_id = "xxxx"
    file_col_name = "File"
    base.update_row('Table1', row_id, {"File": [info_dict]})
    ```

??? question "Download file to local"

    ``` python
    base.download_custom_file(path, save_path)
    ```

    __Example__

    ``` python
    custom_file_path = "/Main/sky.png"
    local_path = "/Users/Desktop/sky.png"
    base.download_custom_file(custom_file_path, local_path)
    ```

??? question "Upload local file to custom folders"

    ``` python
    base.upload_local_file_to_custom_folder(self, local_path, custom_folder_path=None, name=None)
    ```

    __Example__

    ``` python
    local_path = "/Users/Desktop/sky.png"
    custom_path = "/Main/"

    info_dict = base.upload_local_file_to_custom_folder(local_path， custom_path)
    row_id = "xxxx"
    file_col_name = "File"
    base.update_row('Table1', row_id, {"File": [info_dict]})
    ```

### Big data storage

??? question "Insert rows into big data storage"

    Batch insert rows into big data storage.

    ``` python
    base.big_data_insert_rows(table_name, rows_data)
    ```

    __Example__

    ``` python
    rows = [
            {'Name': "A"},
            {'Name': "B"}
        ]
    base.big_data_insert_rows('Table1', rows_data=rows)
    ```

### User

??? question "Get a user info"

    Returns the name of the user and his `id_in_org`.

    ``` python
    base.get_user_info(username)
    ```

    __Example__

    ``` python
    base.get_user_info("aea9e807bcfd4f3481d60294df74f6ee@auth.local")
    ```

## Account

Account provides an interface to list all Workspaces, add/copy/delete Bases, and obtain access rights to a Base.

!!! tip "Separate Authentication required"

    Account requires a separate authentication.

    ```
    from seatable_api import Account
    username = 'xiongxxx@xxx.com'
    password = 'xxxxxxx'
    server_url = 'https://cloud.seatable.cn/'
    account = Account(username, password, server_url)
    account.auth()
    ```

??? abstract "List workspaces"

    Get all your workspaces and its Bases.

    ``` python
    account.list_workspaces()
    ```

    __Example__

    ``` python

    ```

??? abstract "Add a base"

    Add a base to a Workspace.

    ``` python
    account.add_base(name, workspace_id=None)
    ```

    __Example__

    ``` python
    account.add_base('new-base', 35)
    ```

??? abstract "Copy a base"

    Copy a base to a workspace.

    ``` python
    account.copy_base(src_workspace_id, base_name, dst_workspace_id)
    ```

    __Example__

    ``` python
    account.copy_base(35, 'img-file', 74)
    ```

??? abstract "Get a base"

    Get a base object. Get the Base object named base_name that exists in the workspace whose id is workspace_id.

    ``` python
    account.get_base(workspace_id, base_name)
    ```

    __Example__

    ``` python
    base = account.get_base(35, 'new-base')
    ```

## Date Utility Functions

We provide a set of functions for the date operations based on the datetime module of python. These functions have the same behavior as the functions provided by the formula column of SeaTable.

!!! warning "function import required"

    To use these functions, the dateutils module must be imported.

    ```
    from seatable_api.date_utils import dateutils
    ```

!!! tip "Timezone"

    If the input time string has a timezone info, it will be automatically converted to local time.

??? success "date"

    Return the ISO formatted date string.

    ``` python
    dateutils.date(year, month, day)
    ```

    __Example__

    ``` python
    custom_date = dateutils.date(2020, 5, 16)
    print(custom_date) # 2020-05-16
    ```

??? success "now"

    Return the ISO formatted date time of current and accurated to seconds.

    ``` python
    dateutils.now()
    ```

    __Example__

    ``` python
    now = dateutils.now()
    print(now) # 2022-02-07 09:44:00
    ```

??? success "today"

    Return the ISO formatted current date time in string

    ``` python
    dateutils.today()
    ```

    __Example__

    ``` python
    today = dateutils.today()
    print(today) # 2022-02-07
    ```

??? success "dateadd"

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

??? success "datediff"

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

??? success "eomonth"

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

??? success "year"

    Return the year of given date.

    ``` python
    dateutils.year(date)
    ```

    __Example__

    ``` python
    dateutils.year("2019-1-1") # 2019
    ```

??? success "month"

    Return the month of given date.

    ``` python
    dateutils.month(date)
    ```

    __Example__

    ``` python
    dateutils.month("2019-5-4") # 5
    ```

??? success "months"

    Return the months difference of two given date.

    ``` python
    dateutils.months(start, end)
    ```

    __Example__

    ``` python
    dateutils.months("2019-5-1","2020-5-4") # 12
    ```

??? success "day"

    Return the day of given date.

    ``` python
    dateutils.day(date)
    ```

    __Example__

    ``` python
    dateutils.day('2020-6-15 14:23:21') # 15
    ```

??? success "days"

    Return the days difference of two given date.

    ``` python
    dateutils.days(start, end)
    ```

    __Example__

    ``` python
    dateutils.days('2019-6-1', '2020-5-15') # 349
    ```

??? success "hour"

    Return the hour of given datetime.

    ``` python
    dateutils.hour(date)
    ```

    __Example__

    ``` python
    dateutils.hour("2020-1-1 12:20:30") # 12
    ```

??? success "hours"

    Return the hours difference of two given datetime.

    ``` python
    dateutils.hours(start, end)
    ```

    __Example__

    ``` python
    dateutils.hours("2019-6-3 20:1:12", "2020-5-3 13:13:13") # 8033
    ```

??? success "minute"

    Return the minutes of given datetime.

    ``` python
    dateutils.minute(date)
    ```

    __Example__

    ``` python
    dateutils.minute("2020-5-3 13:13:13") # 13
    ```

??? success "second"

    Return the seconds of given datetime.

    ``` python
    ateutils.second(date)
    ```

    __Example__

    ``` python
    ateutils.second("2020-5-3 13:13:33") # 33
    ```

??? success "weekday"

    Return the weekday by recording 0 to 6 from Monday to Sunday.

    ``` python
    dateutils.weekday(date)
    ```

    __Example__

    ``` python
    dateutils.weekday("2019-6-3") # 0
    ```

??? success "isoweekday"

    Return the weekday by recording 1 to 7 from Monday to Sunday based on ISO standard.

    ``` python
    dateutils.isoweekday(date)
    ```

    __Example__

    ``` python
    dateutils.isoweekday("2019-6-3") # 1
    ```

??? success "weeknum"

    Return the week number of given date by counting the 1st of Jan. as the first week.

    ``` python
    dateutils.weeknum(date)
    ```

    __Example__

    ``` python
    dateutils.weeknum('2012-1-2') # 2
    ```

??? success "isoweeknum"

    Return the week number of given date based on ISO standard.

    ``` python
    dateutils.isoweeknum(date)
    ```

    __Example__

    ``` python
    dateutils.isoweeknum('2012-1-2') # 1
    ```

??? success "isomonth"

    Return the ISO formatted month.

    ``` python
    dateutils.isomonth(date)
    ```

    __Example__

    ``` python
    dateutils.isomonth("2012-1-2") # 2012-01
    ```

??? success "quarter_from_yq"

    Return a DateQuarter object, and params inlclude year and quarter..

    ``` python
    dateutils.quarter_from_yq(year, quarter)
    ```

    __Example__

    ``` python
    dateutils.quarter_from_yq(2022, 3) # DateQuarter obj:<DateQuarter-2022,3Q>
    ```

??? success "quarter_from_ym"

    Return a DateQuarter object, and params include year and month.

    ``` python
    dateutils.quarter_from_ym(year, month)
    ```

    __Example__

    ``` python
    dateutils.quarter_from_ym(2022, 3) # DateQuarter obj:<DateQuarter-2022,3Q>
    ```

??? success "to_quarter"

    Return a DateQuarter object of a time string.

    ``` python
    dateutils.to_quarter(time_str)
    ```

    __Example__

    ``` python
    dateutils.to_quarter("2022-07-17") # DateQuarter obj: <DateQuarter-2022,3Q>
    ```

??? success "quarters_within"

    Return a generator which will generate the DateQuater objects between a start date and end date. You can get the last quarter in the generator if you set param `include_last=True` which is `False` by default.

    ``` python
    dateutils.quarters_within(start, end, include_last)
    ```

    __Example__

    ``` python
    qs = dateutils.quarters_within("2021-03-28", "2022-07-17", include_last=True)
    list(qs) # [<DateQuarter-2021,1Q>, <DateQuarter-2021,2Q>,...., <DateQuarter-2022,3Q>]
    ```

??? success "Quarter operation"

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

??? success "Other examples"

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

## Context

When the script is running in the cloud, the context object provides a context environment. Here's how to use it

??? info "server_url"

    Server URL, used to initialize Base.

    ``` python
    context.server_url
    ```

    __Example__

    ``` python
    from seatable_api import context
    print(context.server_url)
    ```

??? info "api_token"

    API token for access a base.

    ``` python
    context.api_token
    ```

    __Example__

    ``` python
    from seatable_api import context
    print(context.api_token)
    ```

??? info "current_table"

    The name of the table that the current user is viewing when the user runs a script manually.

    ``` python
    context.current_table
    ```

    __Example__

    ``` python
    from seatable_api import context
    print(context.current_table)
    ```

??? info "current_row"

    When the user manually runs a script, the line where the cursor is currently located.

    ``` python
    context.current_row
    ```

    __Example__

    ``` python
    from seatable_api import context
    print(context.current_row)
    ```

??? info "current_username"

    The System ID of the user who runs the script manually (in old verison, it is called current_user_id).

    ``` python
    context.current_username
    ```

    __Example__

    ``` python
    from seatable_api import context
    print(context.current_username)
    ```

??? info "current_id_in_org"

    The id of the user in the team, it can be set by the team admin via Web UI.

    ``` python
    context.current_id_in_org
    ```

    __Example__

    ``` python
    from seatable_api import context
    print(context.current_id_in_org)
    ```

## Constants

In the script there may be some constants we need to know

??? question "ColumnTypes"

    Column type, when insert/add columns, change column types, etc. need to be used

    ```python
    from seatable_api.constants import ColumnTypes

    ColumnTypes.NUMBER              # number
    ColumnTypes.TEXT                # text
    ColumnTypes.LONG_TEXT           # long text
    ColumnTypes.CHECKBOX            # checkbox
    ColumnTypes.DATE                # date & time
    ColumnTypes.SINGLE_SELECT       # single select
    ColumnTypes.MULTIPLE_SELECT     # multiple select
    ColumnTypes.IMAGE               # image
    ColumnTypes.FILE                # file
    ColumnTypes.COLLABORATOR        # collaborator
    ColumnTypes.LINK                # link to other records
    ColumnTypes.FORMULA             # formula
    ColumnTypes.CREATOR             # creator
    ColumnTypes.CTIME               # create time
    ColumnTypes.LAST_MODIFIER       # last modifier
    ColumnTypes.MTIME               # modify time
    ColumnTypes.GEOLOCATION         # geolocation
    ColumnTypes.AUTO_NUMBER         # auto munber
    ColumnTypes.URL                 # URL
    ```

## Notifications

??? question "send_toast_notification"

    Send a nofication message which can be toasted on web page to a user.

    ```python
    base.send_toast_notification(username, msg, toast_type='success')
    # toast_type: one of "success", "warning" or "danger"
    ```

    __Example__

    ```python
    base.send_toast_notifation(
    "aea9e807bcfd4f3481d60294df74f6ee@auth.local",
    "error request",
    "danger"
    )
    ```

## Websockets

??? question "socketIO"

    By using websocket, you can get __realtime data update notifications__ of a base.

    ```python
    from seatable_api import Base

    server_url = 'https://cloud.seatable.cn'
    api_token = 'c3c75dca2c369849455a39f4436147639cf02b2d'

    base = Base(api_token, server_url)
    base.auth(with_socket_io=True)

    base.socketIO.wait()
    ```

    When Base has data updated, the following will be output in the terminal.

    ```log
    2022-07-19 11:48:37.803956 [ SeaTable SocketIO connection established ]
    2022-07-19 11:48:39.953150 [ SeaTable SocketIO on UPDATE_DTABLE ]
    {"op_type":"insert_row","table_id":"0000","row_id":"YFK9bD1XReSuQ7WP1YYjMA","row_insert_position":"insert_below","row_data":{"_id":"RngJuRa0SMGXyiA-SHDiAw","_participants":[],"_creator":"seatable@seatable.com","_ctime":"","_last_modifier":"seatable@seatable.com","_mtime":""},"links_data":{}}
    ```

    After getting data update notifications, performance self-defined actions by listen to the UPDATE_DTABLE event.

    ```python
    import json
    from seatable_api import Base
    from seatable_api.constants import UPDATE_DTABLE

    server_url = 'https://cloud.seatable.cn'
    api_token = 'c3c75dca2c369849455a39f4436147639cf02b2d'

    def on_update(data, index, *args):
        try:
            operation = json.loads(data)
            print(operation)
            op_type = operation['op_type']
            table_id = operation['table_id']
            row_id = operation['row_id']
            # ... do something
        except Exception as e:
            print(e)

    base = Base(api_token, server_url)
    base.auth(with_socket_io=True)

    base.socketIO.on(UPDATE_DTABLE, on_update)
    base.socketIO.wait()
    ```
