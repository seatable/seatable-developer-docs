# Metadata

Metadata delivers the complete structure of a base with tables, views and columns.

!!! abstract "get_metadata"

    Get the complete metadata of a table. The metadata will not contain the concrete rows of the table.

    === "Function call"

        ``` js
        base.get_metadata()
        ```

    === "Output structure"

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

    __Example__

    ```python
    from seatable_api import Base, context

    base = Base(context.api_token, context.server_url)
    base.auth()

    print(base.get_metadata())
    ```

!!! info "Displaying long and complex objects"

    If you have hard time reading the output of a function returning a long or complex object, please see [how to make a pretty print](../common_questions.md#printing-complex-elements-is-sometimes-difficult-to-read).
