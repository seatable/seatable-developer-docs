# Output

Output object supports output strings in text or Markdown format.

!!! quote "text"

    Prints the content of the passed variable as normal text. Code Syntax is ignored and just printed.

    ``` js
    output.text(anything: String/Object/Array)
    ```

    __Example__

    ``` js
    const table = base.getActiveTable();
    output.text(table.name);
    ```

!!! quote "markdown"

    Prints the content of the passed variable. Markdown formating is used to style the output.

    ``` js
    output.markdown(anything: String/Object/Array)
    ```

    __Example__

    ``` js
    const table = base.getActiveTable();
    output.markdown(`# This is a headline and prints the name of the table: ${table.name}`);
    ```
