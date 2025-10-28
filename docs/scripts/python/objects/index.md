# Predefined objects and methods (Python)

This manual list all available objects and methods (also called functions) that are available within Python scripts in SeaTable. When running directly in SeaTable, Python scripts have the ability to access the [base context](context.md). [Date utilities](date-utils.md) are also available.

If you compare JavaScript and Python, you will notice that Python has no specific output methods. This is not necessary, because the output is either written into the base or directly returned by the methods. Besides, you'll see that **Python methods never accepts objects** for table, view or row selection arguments, but only their names/`_ids` as strings.  Unless otherwise stated, **all method arguments are required**.

## Data model

{%
    include-markdown "includes.md"
    start="<!--datamodel-start-->"
    end="<!--datamodel-end-->"
%}

!!! info "Need a specific function?"

    The Python library `seatable_api` does not yet cover all available functions of the SeaTable API. If you are missing a special function, please contact us at [support@seatable.io](mailto:support@seatable.io) and we will try to add the missing functions.

## Getting started

Let's make this concrete and let us look at some basic examples.

1. Jump to your SeaTable web interface
2. Create a new Python script
3. Copy the following code
4. Run the script

You will learn from these examples, that it is quite easy to read, output and even manipulate the data of a base inside SeaTable with the predefined objects and the corresponding methods.



=== "1. Add a table to a base"

    This examples shows how to add a table to an existing bases.

    ``` python
    from seatable_api import Base, context
    base = Base(context.api_token, context.server_url)
    base.auth() # (1)!

    columns=[
      {
        "column_type" : "text", 
        "column_name": "name"
      }, 
      {
      "column_type": "number",
      "column_name": "age"
      }
    ]

    base.add_table("ScriptTest", lang='en', columns=columns)
    ```

    1.   These three lines are always required to authorize against the base in SeaTable.

=== "2. Add a row to this new table"
    This examples shows how to add a a record to a table. The example script assumes that a table "ScriptTest" table with two columns "name" and "age" exists in the base.

    ``` python
    from seatable_api import Base, context
    base = Base(context.api_token, context.server_url)
    base.auth()

    row_data = {
      'name': 'Tom',
      'age': 18
      } 
    
    base.append_row('ScriptTest', row_data)
    ```
