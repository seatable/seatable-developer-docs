# JavaScript Client

The SeaTable JavaScript Client encapsulates SeaTable Server Restful API. You can call it in your front-end page or Node.js program.

!!! danger "JavaScript API cannot be used for scripts in SeaTable bases. For script programming with Javascript, there is a [separate chapter](/scripts/) in this documentation."

Note, JavaScript API calls SeaTable Server Restful API, while scripts in SeaTable bases interact with the base loaded in the browser, so the APIs of the two are somewhat different.

## Installation

```shell
npm install seatable-api
```

The source code of the JavaScript Client API is available at [GitHub](https://github.com/seatable/seatable-api-js).

## Reference

To use SeaTable APIs, you should first initialize a base object and call `base.auth()`. `base.auth()` is an async function, which needs to be executed in async functions. Other APIs all return a promise object. There are two ways to use them

The first way:

```
base.listViews(tableName).then(views => {
  // Use views to complete the requirements
}).catch(error => {
  // Exception handling
})
```

The second way:

```
try {
  const views = await base.listViews(tableName);
  // Use views to complete the requirements
} catch (error) {
  // Exception handling
}
```

SeaTable API Errors

- 400 Params invalid
- 403 Permission denied
- 413 exceed limit
- 500 Internal Server Error

## Authorization

Base represents a table. You can use the api token of the form to obtain the authorization to read and write the base. This token can be generated directly on the web side.

Use the API Token of the base to get access authorization.

##### Example

```javascript
import { Base } from "seatable-api";

const config = {
  server: "https://cloud.seatable.cn",
  APIToken: "c3c75dca2c369849455a39f4436147639cf02b2d",
};

const base = new Base(config);
await base.auth();
```
