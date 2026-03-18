# SeaTable Developer Manual

You want to interact with SeaTable programmatically -- whether you're building an integration, automating workflows from external systems, or developing a SeaTable plugin? This manual covers everything you need.

## Who is this manual for?

This manual is for **developers** who want to:

- Build external applications that communicate with SeaTable (Python, JavaScript, PHP)
- Develop custom plugins for SeaTable
- Look up the complete function reference of the SeaTable API libraries

!!! tip "Looking to write scripts inside SeaTable?"

    If you want to create and run scripts directly within a SeaTable base, head to the [SeaTable User Manual](https://seatable.com/help/scripts/) for step-by-step examples and getting-started guides. The function reference for the scripting libraries is documented here.

## Choose your language

| Language | Use case | Get started |
|---|---|---|
| **Python** | External apps, data pipelines, automations, scripts in SeaTable | [Python](python/getting-started/) |
| **JavaScript** | Scripts in SeaTable, Node.js apps, frontend integrations | [JavaScript](javascript/) |
| **PHP** | Web applications, server-side integrations | [PHP](php/) |

The [Ruby community client](ruby/) is also available.

For other languages, use the [REST API](https://api.seatable.com) directly -- it provides interactive examples and code snippets for many languages.

## Plugin Development

Build custom plugins that visualize and interact with base data inside SeaTable. Requires JavaScript and React.

[Plugin Development](plugins/)

## API Reference

The complete REST API documentation with interactive examples is available at [api.seatable.com](https://api.seatable.com).

## Data model

{%
    include-markdown "includes.md"
    start="<!--datamodel-start-->"
    end="<!--datamodel-end-->"
%}
