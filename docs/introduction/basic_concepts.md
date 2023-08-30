# Basic concepts

SeaTable is the world leading self-hosted no-code platform. With seatable, you can digitize processes and workflows in the shortest possible time without having to write a line of code.

Even though you don't need any programming skills to use SeaTable, the digital Lego construction kit for developers offers various interfaces and automation options.

## Right solution for your purpose

Depending on what you want to do with seatable, this manual is divided into three major sections. This manual explains how you can build such solutions by yourself.

Here are **three examples**, one for each section of this documentation:

### Python script to get the structure of a base

You can take the following python code and copy&paste it to SeaTable. It will return the complete metastructure of your base. Easy or not?

=== "Python code"

    ```python
    from seatable_api import Base, context
    base = Base(context.api_token, context.server_url)
    base.auth()

    metadata = base.get_metadata()

    print("--- COMPLETE BASE STRUCTURE WITH ALL BASES AND COLUMNS ---")
    for table in metadata['tables']:
        print('.')
        print("Table: "+table['name']+" (ID: "+table['_id']+")")
    for column in table['columns']:
        link_target = ""
        if column['type'] == "link":
            link_target = " --> "+column['data']['other_table_id']
            if column['data']['other_table_id'] == table['_id']:
                link_target = " --> "+column['data']['table_id']
        print("  --> "+column['name']+" ("+column['type']+link_target+")")
    ```

=== "Output"

    ```
    --- COMPLETE BASE STRUCTURE WITH ALL BASES AND COLUMNS ---
    .
    Table: Opportunities (ID: 9g8f)
    --> Name (text)
    --> Status (single-select)
    --> Prio (single-select)
    --> Owner (collaborator)
    --> Customer (link --> deGa)
    --> Estimated value (number)
    --> Proposal deadline (date)
    --> Contacts (link --> lYb8)
    --> Interactions (link --> 0000)
    .
    Table: Interactions (ID: 0000)
    --> Interaction ID (auto-number)
    --> Opportunity (link --> 9g8f)
    --> Type (single-select)
    --> Interaction (formula)
    --> Opportunity status (formula)
    --> Date and time (date)
    --> Contact (link --> lYb8)
    --> Notes (long-text)#
    ```

### Gallery-Plugin

SeaTable provides some Plugins to visualize your data. Examples for such a plugin are the [Gallery](https://seatable.io/docs/plugins/anleitung-zum-galerie-plugin/?lang=auto), [Timeline](https://seatable.io/docs/plugins/anleitung-zum-timeline-plugin/?lang=auto), [Kanban](https://seatable.io/docs/plugins/anleitung-zum-kanban-plugin/?lang=auto) and so on. But SeaTable has everything that you build your own plugin. There are no limits to the imagination, it just requires some time and React skills.

![Screenshot of the Galery Plugin](https://seatable.io/wp-content/uploads/2022/10/Galerie.png)

### Custom app: SeaTable ideas

There are multiple API classes available for various programming languages. This enables you to build any app or website you want.

Our feature request tool [SeaTable Ideas](https://ideas.seatable.io) is an example for such a website. It uses SeaTable as database and the frontend is build completely with PHP and the [slim framework](https://www.slimframework.com/).

![Screenshot of ideas.seatable.io](https://forum.seatable.io/uploads/default/optimized/2X/0/0dabbe5b885a38b9fc178b66f63686322429b997_2_690x366.png).

## Data model

As a developer you typically interact with a single base. In SeaTable, a base can contain multiple tables, and each table contains multiple rows and columns. A row contains multiple fields.

The logic is like this:

```sh
SeaTable Base
├─ Table 1
│  └─ View A
|     └─ Row 1
|     └─ Row 2
|     └─ Row 3
│  └─ View B
|     └─ Row 3
|     └─ Row 4
└─ Table 2
|  └─ ...
```

SeaTable offers a visual interface, which can be operated with the browser.

![Screenshot of a SeaTable base](https://seatable.io/wp-content/uploads/2022/09/elements_seatable_base.png)

Look at the [SeaTable API Reference](https://api.seatable.io/reference/models) for more details about the different objects in SeaTable like:

- Table
- View
- Row & column
- Link

## Authentication

The actual authentication depends on the development approach one chooses.

=== "Scripts"

    Javascript Scripts does not require any authentication at all because these scripts are executed in the browser of the user and the user has to be authenticated already.

    Plugin Scripts require an authentication to get data from the base, but the `context` objects contains everything for an easy authentication.

=== "Plugins"

    Plugins interact with the data of one base. SeaTable provides all required functions for easy authentication.

=== "Client APIs"

    If you want to build your own application you always have to authenticate with a base token against the base.
