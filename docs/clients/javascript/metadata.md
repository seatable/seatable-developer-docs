# Metadata

Metadata delivers the complete structure of a base with tables, views and columns.

!!! question "getMetadata"

    Get the complete metadata of a table. The metadata will not contain the concrete rows of the table.

    ``` js
    base.getMetadata();
    ```

    __Example__

    ```
    {
        'tables': [{
            '_id': '4krH',
            'name': 'Contact',
            'is_header_locked': false,
            'columns': [{
                'key': '0000',
                'type': 'text',
                'name': 'Name',
                'editable': true,
                'width': 200,
                'resizable': true,
                'draggable': true,
                'data': null,
                'permission_type': '',
                'permitted_users': []
            }, {
                'key': 'M31F',
                'type': 'text',
                'name': 'Email',
                'editable': true,
                'width': 200,
                'resizable': true,
                'draggable': true,
                'data': null,
                'permission_type': '',
                'permitted_users': []
            }],
            'views': [{
                '_id': '0000',
                'name': 'Default view',
                'type': 'table',
                'is_locked': false,
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
