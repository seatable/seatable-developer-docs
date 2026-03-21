---
description: Developer documentation for SeaTable's client libraries (Python, JavaScript, PHP), SQL interface, and plugin development. Build integrations, automate workflows, and extend SeaTable programmatically.
---

# SeaTable Developer Manual

This manual covers the programmatic interfaces to SeaTable: client libraries, the scripting API reference, and plugin development.

## Who is this manual for?

This manual is for **developers** who want to:

- Build external applications that communicate with SeaTable (Python, JavaScript, PHP)
- Develop custom plugins for SeaTable
- Look up the function reference of the SeaTable client libraries (Python, JavaScript, PHP)

!!! tip "Looking to write scripts inside SeaTable?"

    If you want to create and run scripts directly within a SeaTable base, head to the [SeaTable User Manual](https://seatable.com/help/scripts/) for step-by-step examples and getting-started guides. The function reference for the scripting libraries is documented in this developer manual.

## Languages

| Language | Use case |
|---|---|
| **[Python](python/)** | External apps, data pipelines, automations, scripts in SeaTable |
| **[JavaScript](javascript/)** | Scripts in SeaTable, Node.js apps, frontend integrations |
| **[PHP](php/)** | Web applications, server-side integrations |
| **[Ruby](ruby/)** | Community client |

!!! example "Other languages"

    For other languages, use the [REST API](https://api.seatable.com) directly. It provides interactive examples and code snippets.

## Data Model

SeaTable organizes data in bases, tables, columns, rows, and views. The complete schema definition is available at [api.seatable.com/reference/models](https://api.seatable.com/reference/models).

## Plugin Development

Custom plugins can visualize and interact with base data inside SeaTable. Plugin development requires JavaScript and React. See the [Plugin Development](plugins/) section for details.
