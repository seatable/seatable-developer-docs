# Scripting

## Supported scripting languages and requirements

Scripts are used to interact with the data in a base. SeaTable supports scripts written in JavaScript and Python. Both languages have different requirements and abilities. Let's try to summarize these to help you make the right choice depending on your needs.

|                       | JavaScript  | Python     |
|-----------------------|-------------|------------|
| Requirements          | None        | Eventually `seatable-api` library or [Python Pipeline](https://admin.seatable.com/installation/components/python-pipeline/) (see Execution environment) |
| Data operations       | Simple (mainly tailored for single-line operations)      | More complex (more available operations, possibility of using external libraries) |
| Execution environment | In SeaTable | - In SeaTable (self-hosted with the [Python Pipeline](https://admin.seatable.com/installation/components/python-pipeline/) installed, or Cloud)<br>- [Locally](https://developer.seatable.com/scripts/python/common_questions/#how-to-make-the-script-support-both-local-and-cloud-run) or on a server (need to install `seatable-api` library) |
| Authentication        | Not needed  | Needed |
| Main advantage        | - Ready to use (no requirement, no authentication)<br>- Rather simple (both advantage and disadvantage) | - Local execution convenient for development and debugging purposes<br>- Easily integrated into larger projects |

## How to start?

Both JavaScript and Python scripts can be composed and executed directly in a SeaTable base.

![Screenshot of script icon in SeaTable](/media/Anlegen-eines-Skriptes.jpg)

Here are some additional help articles from the [User Manual's scripts section](https://seatable.com/help/scripts) explaining how to create, execute and monitor a script in SeaTable:

- [Creating and deleting a script](https://seatable.com/help/anlegen-und-loeschen-eines-skriptes/)
- [Run script manually, by button or by automation](https://seatable.com/help/skript-manuell-per-schaltflaeche-oder-automation-ausfuehren/)
- [The execution log of scripts](https://seatable.com/help/das-ausfuehrungslog-von-skripten/)

You'll find in this manual a JavaScript and a Python section. For both of them, each chapter provides you with explanations about the available objects and methods (description with the eventual arguments and one or more simple use cases). 

Multiple [JavaScript](../scripts/javascript/examples/index.md) and [Python](../scripts/python/examples/index.md) examples should help you to start immediately and get a feeling about the possibilities.
