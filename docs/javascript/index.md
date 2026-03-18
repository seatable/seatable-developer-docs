# JavaScript -- Getting Started

SeaTable provides a JavaScript API that works in two contexts:

- **Inside SeaTable** (scripting): Scripts run in the browser, no installation or authentication needed. You get access to the active table, current row, and output functions.
- **External** (Node.js / frontend): Install the `seatable-api` npm package, authenticate with an API token, and interact with SeaTable from any JavaScript environment.

The core methods (tables, views, columns, rows, links, SQL) are **the same in both contexts**. A few features are only available in one context -- these are clearly marked on the respective pages.

## External setup

```shell
npm install seatable-api
```

```js
import { Base } from "seatable-api";

const base = new Base({
  server: "https://cloud.seatable.io",
  APIToken: "your-api-token",
});
await base.auth();
```

API tokens can be [generated in the SeaTable web interface](https://seatable.com/help/erzeugen-eines-api-tokens/).

## Scripting setup

No installation required. Create a new script in SeaTable and start using the `base` object directly:

```js
const tables = base.getTables();
output.text(tables.length);
```

## Async operations

External calls are asynchronous and return promises. Use `await` or `.then()`:

=== "await"

    ```js
    const views = await base.listViews('Table1');
    ```

=== ".then()"

    ```js
    base.listViews('Table1').then(views => {
      // use views
    });
    ```

In scripting context, `query()` and `getLinkedRecords()` also require `await`. All other scripting methods are synchronous.

## Common errors

- 400 Params invalid
- 403 Permission denied
- 413 Exceed limit (see the [API Reference](https://api.seatable.com/reference/limits) about limits)
- 500 Internal Server Error

!!! tip "Looking for examples?"

    Step-by-step JavaScript script examples are available in the [SeaTable User Manual](https://seatable.com/help/scripts/).
