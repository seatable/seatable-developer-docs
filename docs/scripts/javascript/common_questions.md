# Common questions (JavaScript)

??? question "How to output the content of a variable?"

    To output the content of a variable you should use either no punctuation mark at all (for variable only) or dollar/brackets inside backticks `` `${}` ``.


    ```js
    const myVariable = 462;
    // variable-only output
    output.text(myVariable); /* (1)! */

    // prettier output formatting
    output.text(`the content of my variable is ${myVariable}`); /* (2)! */

    // Simple/Double quotes won't work as they are used to encapsulate strings
    output.text("myVariable"); /* (3)! */
    output.text('myVariable'); /* (4)! */
    ```

    1. Returns `462`

    2. Returns `the content of my variable is 462`

    3. Returns `myVariable`

    4. Returns `myVariable`

??? question "The display of complex elements (tables, arrays of rows) is sometimes difficult to read"

    Do not hesitate to use `console.log` and to check your browser console. Otherwise, you could try to use this function (or to create your own) at the beginning of your scripts:

    ```js
    function jsonPrettyFormat(json, indent=0) {
        const indenterChar = " "; /* (1)! */
        if (json instanceof Array) {
            output.text(indenterChar.repeat(indent) + "[");
            indent += 1;
            json.forEach((elem)=>jsonPrettyFormat(elem,indent));
            indent -= 1;
            output.text(indenterChar.repeat(indent) + "]");
        }
        else {
            if (!(typeof(json)=="object")) {
                output.text(indenterChar.repeat(indent) + json);
            } else {
                output.text(indenterChar.repeat(indent) + "{");
                indent += 1;
                for (const [key, value] of Object.entries(json)) {
                    if (!(typeof(value)=="object")) {
                        output.text(indenterChar.repeat(indent) + key + ": " + value)
                    } else {
                        output.text(indenterChar.repeat(indent) + key + ": ");
                        indent += 1;
                        jsonPrettyFormat(value,indent);
                    }
                }
                indent -= 1;
                output.text(indenterChar.repeat(indent) + "}");
            }
        }
    }
    ```

    1. Please note that the indent character is not a classic space character as the output window of SeaTable's script editor actually trims indent spaces.

    Just call it on an object to see the result

    ```js
    let rows = base.getRows('Daily expenses', 'Default View');
    jsonPrettyFormat(rows);
    ```
