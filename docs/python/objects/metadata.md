# Metadata

Metadata delivers the complete structure of a base with tables, views and columns.

!!! abstract "get_metadata"

    Get the complete metadata of a table. The metadata will not contain the concrete rows of the table.

    === "Function call"

        ```python
        base.get_metadata()
        ```

    === "Output structure"

        ```json
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

    __Example__

    ```python
    from seatable_api import Base, context

    base = Base(context.api_token, context.server_url)
    base.auth()

    print(base.get_metadata())
    ```

!!! info "Displaying long and complex objects"

    If you have a hard time reading the output of a complex object, use `json.dumps(result, indent=2)` for pretty printing.
