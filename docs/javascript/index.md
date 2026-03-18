# JavaScript

SeaTable offers two different JavaScript APIs depending on where your code runs:

## Scripting API (inside SeaTable)

Scripts written directly in a SeaTable base use the **Scripting API**. These scripts run in the browser, require no authentication, and interact directly with the loaded base data.

Methods like `base.getActiveTable()`, `base.getRows()`, and `output.text()` are only available in this context.

[Scripting API Reference](scripting/)

## Client API (external, seatable-api-js)

External applications (Node.js or frontend) use the **Client API** via the `seatable-api` npm package. This API communicates with the SeaTable server via REST and requires an API token for authentication.

```shell
npm install seatable-api
```

[Client API Reference](client/javascript_api/)

## Which one should I use?

| | Scripting API | Client API |
|---|---|---|
| Where it runs | In the browser (SeaTable script editor) | Node.js or frontend app |
| Authentication | Not needed (user is already logged in) | API token required |
| Installation | None | `npm install seatable-api` |
| Use case | Automate tasks inside SeaTable | Build external apps and integrations |
| Source code | Built into SeaTable | [GitHub](https://github.com/seatable/seatable-api-js) |

!!! tip "Looking for examples?"

    Step-by-step JavaScript script examples are available in the [SeaTable User Manual](https://seatable.com/help/scripts/).
