# JavaScript client

The SeaTable JavaScript client encapsulates SeaTable Server Restful API. You can call it in your front-end page or Node.js program.

!!! warning "Two different clients"
    JavaScript API cannot be used for scripts in SeaTable bases. For script programming with JavaScript, there is a [separate chapter](../../scripts/javascript/objects/index.md) in this documentation.

Note that JavaScript API calls SeaTable Server Restful API, whereas scripts in SeaTable bases interact with the base loaded in the browser, so the APIs of the two are somewhat different.

## Installation

```shell
npm install seatable-api
```

The source code of the JavaScript Client API is available at [GitHub](https://github.com/seatable/seatable-api-js).

## Reference

To use SeaTable APIs, you should first initialize a base object and call `base.auth()`. `base.auth()` is an async function, which needs to be executed in async functions. Other APIs all return a promise object. There are two ways to use them:

=== "First way using then"

    ```js
    base.listViews(tableName).then(views => {
      // Use views to complete the requirements
    }).catch(error => {
      // Exception handling
    })
    ```

=== "Second way using await"

    ```js
    try {
      const views = await base.listViews(tableName);
      // Use views to complete the requirements
    } catch (error) {
      // Exception handling
    }
    ```

Here are the main SeaTable API errors you might encounter:

- 400 Params invalid
- 403 Permission denied
- 413 Exceed limit (see the [API Reference](https://api.seatable.com/reference/limits) about limits)
- 500 Internal Server Error

## Authorization

The `Base` object represents a table. You need to specify an `APIToken` to get access authorization and to be able to read and write the base. API tokens can be directly [generated in the web interface](https://seatable.com/help/erzeugen-eines-api-tokens/).

__Example__

```js
import { Base } from "seatable-api";

const config = {
  server: "https://cloud.seatable.cn",
  APIToken: "c3c75dca2c369849455a39f4436147639cf02b2d",
};

const base = new Base(config);
await base.auth();
```
