# Output

Two functions are available to display results in the text editor window, allowing you to output strings in text or Markdown format.

!!! abstract "text"

    Prints the content of `anything` as normal text. Code Syntax is ignored and just printed.

    ``` js
    output.text(anything: String/Object/Array)
    ```

    __Output__ String

    __Example__

    ``` js
    const table = base.getActiveTable();
    output.text(table.name);
    ```

!!! abstract "markdown"

    Prints the content of `anything`, while using Markdown formatting to style the output.

    ``` js
    output.markdown(anything: String/Object/Array)
    ```

    __Output__ String

    __Example__

    ``` js
    const table = base.getActiveTable();
    output.markdown(`# This is a headline and prints the name of the table: ${table.name}`);
    ```
