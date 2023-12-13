# Metadata

Metadata delivers the complete structure of a base with tables, views and columns.

!!! question "get_metadata"

    Get the complete metadata of a table. The metadata will not contain the concrete rows of the table.

    ``` js
    base.get_metadata()
    ```

    Example result of this call.

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
