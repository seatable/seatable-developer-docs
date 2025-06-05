# Basic structure of a Python script

Python scripts can be and executed directly in a base using a SeaTable component called Python Pipeline. You can also choose to run scripts locally. Where you run your Python script has consequences on the available libraries and authentication. 

## Libraries

The current Python Pipeline ships with Python 3.11 and a bundle of [third party libraries](/scripts/python/common_questions/#list-of-libraries-supported-in-the-cloud-environment). One of the bundled library and the main library to interact with SeaTable bases is [seatable-api](https://github.com/seatable/seatable-api-python).

At a minimum, the Base and context function from the seatable-api library must be imported. Additionally, you can import functions from the bundled libraries.

```python
from seatable_api import Base, context
from datetime import datetime
```

When running Python scripts locally, you can take advantages of the uncountable number of Python libraries. 

## Authentication

As a general rule, Python script must authenticate. 

Within SeaTable's integrated Python editor, authentication can be done using these two lines of code at the beginning of the script thanks to the [context object](https://developer.seatable.com/scripts/python/objects/context/):

```python
base = Base(context.api_token, context.server_url)
base.auth()
```

Read here all details about [authentication in Python scripts](/scripts/python/authorization_python/).

!!! warning "Multiple tokens in SeaTable"

    SeaTable provides multiple tokens to authenticate. But let's keep things simple! If you develop Python scripts in SeaTable, just use the context object `context.api_token` or provide a so called `API-Token` of a base.

    All details can be found in the [SeaTable API Reference](https://api.seatable.com/reference/authentication).

It is even possible to develop a Python in the way that it could be [executed in the cloud and local](/scripts/python/common_questions/#install-and-use-custom-python-libraries) without changing the code.

## Objects and methods

There are a lot of predefined objects and methods in Python. If you compare JavaScript and Python, you will notice that Python has no output object. This is not necessary, because the output is either written directly into the base or printed.

## Let's get concrete

Let's make this concrete and let us look at some basic examples.

1. Jump to your SeaTable web interface
2. Create a new script of the type Python
3. Copy the following code
4. Run the script

You will learn from these examples, that it is quite easy to read, output and even manipulate the data of a base inside SeaTable with the predefined objects and the corresponding methods.

!!! danger "Indents are important"

    Please take care of indentations! Indentation is mandatory in Python to define the blocks of statements. The number of spaces must be uniform in a block of code. It is preferred to use whitespaces instead of tabs to indent in Python. If the indentations are wrong, the scripts will throw errors or not work as expected!

=== "Add a table to a base"

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

=== "Add a row to a table"
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
